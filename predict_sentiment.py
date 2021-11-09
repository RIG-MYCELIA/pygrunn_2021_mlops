import json

import mlflow
import pandas as pd


def predict_sentiment_huggingface_model():
    # Load in the data
    filename = 'data/data_text_only_grunn.json'
    dict1 = []

    with open(filename, 'r') as f:
        descriptions = json.loads(f.read())
        descriptions = descriptions[:20]
        for des in descriptions:
            dict1.append({"text": des})

    # Load model as a PyFuncModel.
    logged_model = 'runs:/fad5ab2a7126432a8a01c0a95086bcc0/model'
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    # Predict on a Pandas DataFrame.
    df_data = pd.DataFrame(dict1)
    res = loaded_model.predict(df_data)
    with open('data/outputs_grunn.json', 'w') as f:
        f.write(json.dumps(res.to_json()))

def predict_sentiment_finetuned_model():
    # Load in the data
    filename = 'data/data_text_only_grunn.json'
    dict1 = []

    with open(filename, 'r') as f:
        descriptions = json.loads(f.read())
        descriptions = descriptions[:20]
        for des in descriptions:
            dict1.append({"text": des})

    # Load model as a PyFuncModel.
    logged_model = 'runs:/b1adc125a59d4cbeb7afc2baba3b2e1a/model'
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    # Predict on a Pandas DataFrame.
    df_data = pd.DataFrame(dict1)
    res = loaded_model.predict(df_data)
    with open('data/outputs_finetuned_grunn.json', 'w') as f:
        f.write(json.dumps(res.to_json()))

predict_sentiment_huggingface_model()
# predict_sentiment_finetuned_model()

# TODO Step 4.C: run prediction with the new model
