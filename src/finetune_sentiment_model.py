from data.grunn_dataset import create_extra_dataset
from transformers import (AutoModelForSequenceClassification, Trainer,
                          TrainingArguments)

model = AutoModelForSequenceClassification.from_pretrained("wietsedv/bert-base-dutch-cased-finetuned-sentiment")  # PyTorch
train_dataset, val_dataset, _ = create_extra_dataset()

training_args = TrainingArguments(
    output_dir='./data/training/results',          # output directory
    num_train_epochs=3,              # total number of training epochs
    per_device_train_batch_size=16,  # batch size per device during training
    per_device_eval_batch_size=64,   # batch size for evaluation
    warmup_steps=500,                # number of warmup steps for learning rate scheduler
    weight_decay=0.01,               # strength of weight decay
    logging_dir='.data/training/logs',            # directory for storing logs
    logging_steps=10,
)

trainer = Trainer(
    model=model,                         # the instantiated 🤗 Transformers model to be trained
    args=training_args,                  # training arguments, defined above
    train_dataset=train_dataset,         # training dataset
    eval_dataset=val_dataset,            # evaluation dataset
    # callbacks=[MLflowCallback]
)

trainer.train()
trainer.save_model('data/model/finetuned_bertje')

# TODO Step 4.A: Finetune the model with the new data and save the model
