import torch
import json
from transformers import AutoTokenizer
from sklearn.model_selection import train_test_split

# Create the dataset in the format of a Torch Dataset
class GrunnOpenDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


def add_extra_feature_to_tracked_dataset():
    filename_source_dataset = 'data/data_grunn.json'
    with open(filename_source_dataset, 'r') as f:
        source_dataset = json.loads(f.read())

    filename_extra_dataset = 'data/extra_data_grunn_features.json'
    with open(filename_extra_dataset, 'r') as f:
        extra_dataset = json.loads(f.read())
    
    new_dataset = source_dataset + extra_dataset
    with open(filename_source_dataset, 'w') as f:
        f.write(json.dumps(new_dataset))


def create_extra_dataset():
    tokenizer = AutoTokenizer.from_pretrained('GroNLP/bert-base-dutch-cased')

    filename_texts = 'data/extra_data_grunn_features.json'
    with open(filename_texts, 'r') as f:
        texts = json.loads(f.read())

    filename_labels = 'data/extra_data_grunn_labels.json'
    with open(filename_labels, 'r') as f:
        labels = json.loads(f.read())

    train_texts = texts[:-1]
    train_labels = labels[:-1]
    test_texts = texts[-1:]
    test_labels = labels[-1:]
    train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=.2)

    train_encodings = tokenizer(train_texts, truncation=True, padding=True)
    val_encodings = tokenizer(val_texts, truncation=True, padding=True)
    test_encodings = tokenizer(test_texts, truncation=True, padding=True)

    train_dataset = GrunnOpenDataset(train_encodings, train_labels)
    val_dataset = GrunnOpenDataset(val_encodings, val_labels)
    test_dataset = GrunnOpenDataset(test_encodings, test_labels)

    return train_dataset, val_dataset, test_dataset

# TODO 3.B: Create a training, validation and test dataset within the Torch Dataset format