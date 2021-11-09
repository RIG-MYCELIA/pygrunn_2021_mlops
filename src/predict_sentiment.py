import json

import mlflow
import pandas as pd

def predict_sentiment(mlflow_run_id, output_filename):
    # Load in the data
    filename = 'data/data_text_only_grunn.json'
    dict1 = []

    with open(filename, 'r') as f:
        descriptions = json.loads(f.read())
        descriptions = descriptions[:20]
        for des in descriptions:
            dict1.append({"text": des})

    # Load model as a PyFuncModel.
    logged_model = mlflow_run_id
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    # Predict on a Pandas DataFrame.
    df_data = pd.DataFrame(dict1)
    res = loaded_model.predict(df_data)
    with open(output_filename, 'w') as f:
        f.write(json.dumps(res.to_json()))

# TODO Step 2.B : rung prediction with the hugging face model
predict_sentiment(mlflow_run_id='runs:/xxx/model',
                  output_name='data/outputs_huggingface_grunn.json')

# TODO Step 4.C: run prediction with the new model
predict_sentiment(mlflow_run_id='runs:/xxx/model',
                  output_name='data/outputs_finetuned_grunn.json')

# TODO Step 6: run prediction with the new model on the old data
predict_sentiment(mlflow_run_id='runs:/xxx/model',
                  output_name='data/outputs_finetuned_grunn_old_data.json')
