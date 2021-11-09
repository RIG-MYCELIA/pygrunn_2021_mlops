import dvc.api
import json
import subprocess

def init_dvc():
    subprocess.call(["dvc", "init"])
    # dvc add data_grunn

def init_remote_storage_dvc(connection_string):
    subprocess.call(['dvc', 'remote', 'add', '-d', 'azure_storage', 'azure://dvc'])
    subprocess.call(['dvc', 'remote', 'modify', '--local', 'azure_storage', 'azure_storage', connection_string])
    # dvc push

def download_dataset():
    with dvc.api.open(
        'data_grunn.json',
        remote='azure_storage') as fd:
        data = json.loads(fd.read())
        print(data['result']['records'][0])

# TODO STEP 1.B: initialize dvc and add version control the dataset

