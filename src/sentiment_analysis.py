import mlflow
from transformers import pipeline

# Wrapper class for the sentiment analysis task pipeline
class SentimentAnalysis(mlflow.pyfunc.PythonModel):
    '''
    Any MLflow Python model is expected to be loadable as a python_function model.
    '''

    def __init__(self, local_model_path=None):
        from transformers import (AutoModelForSequenceClassification,
                                  AutoTokenizer)
        huggingface_hub_model_name = "wietsedv/bert-base-dutch-cased-finetuned-sentiment"

        if local_model_path:
            model_path = local_model_path
        else:
            model_path = huggingface_hub_model_name
           
        self.tokenizer = AutoTokenizer.from_pretrained(huggingface_hub_model_name)
        self.sentiment_analysis = AutoModelForSequenceClassification.from_pretrained(model_path)

    def predict(self, context, model_input):
        classifier = pipeline('sentiment-analysis', model=self.sentiment_analysis, tokenizer=self.tokenizer)
        model_input['name'] = model_input['text'].apply(classifier)

        return model_input
