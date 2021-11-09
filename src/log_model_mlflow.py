import json

import mlflow
from mlflow.models import ModelSignature

from sentiment_analysis import SentimentAnalysis

# Input and Output formats
input = json.dumps([{'name': 'text', 'type': 'string'}])
output = json.dumps([{'name': 'text', 'type': 'string'}])
# Load model from spec
signature = ModelSignature.from_dict({'inputs': input, 'outputs': output})

# Start tracking
with mlflow.start_run(run_name="groningen_sentiment_analysis") as run:
    print(run.info.run_id)
    runner = run.info.run_id
    mlflow.pyfunc.log_model('model', loader_module=None, data_path=None,
                            code_path=None, conda_env=None,
                            python_model=SentimentAnalysis(), artifacts=None,
                            registered_model_name=None, signature=signature,
                            input_example=None, await_registration_for=0)

# TODO STEP 2: Log the hugging face model in MLflow
# To see the locally logged model, enter `mlflow ui` in the command line

# with mlflow.start_run(run_name="groningen_sentiment_analysis_finetuned_bertje") as run:
#     print(run.info.run_id)
#     runner = run.info.run_id
#     mlflow.pyfunc.log_model('model', loader_module=None, data_path=None,
#                             code_path=None, conda_env=None,
#                             python_model=SentimentAnalysis('data/model/finetuned_bertje'), artifacts=None,
#                             registered_model_name=None, signature=signature,
#                             input_example=None, await_registration_for=0)

# TODO STEP 4.B: Log the new model to MLFlow (As the Pytorch model is not in a flexible MLflow model format)
