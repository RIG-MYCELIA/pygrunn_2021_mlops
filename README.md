# pygrunn_2021_mlops
Live demo about the usage of MLflow &amp; DVC for the talk at Pygrunn Groningen '21. In this talk Bertje (Dutch Transformer model created by Groningen University) will be applied to an open dataset of the City Groningen. This [dataset](https://ckan.dataplatform.nl/dataset/mor-slim-melden-groningen/resource/edc8db66-8dc3-4819-9935-e6c8f55388ab) contains the remarks from citizens about the public spaces in the city, and is a goldmine about what people really think about the city. 

0. pip install the requirements.txt in a virtual environment :) -> this has been tested on Windows 11 (sorry for not dockerizing this demo :( ). 

Follow the todo's in this repository belonging to the steps below to follow along with the representer, some steps have multiple todo's in multiple files.

1. Download dataset & init DVC
2. Run experiment with model
3. Manually label a few features  
4. Train model & Run experiment with new model
5. Change back the dataset
6. Run experiment with old data and new model
