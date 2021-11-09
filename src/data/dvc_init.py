import dvc.api
import json
import subprocess

def init_dvc():
    subprocess.call(["dvc", "init"])

def init_remote_storage_dvc(connection_string):
    subprocess.call(['dvc', 'remote', 'add', '-d', 'azure_storage', 'azure://dvc'])
    subprocess.call(['dvc', 'remote', 'modify', '--local', 'azure_storage', 'azure_storage', connection_string])

def download_dataset():
    with dvc.api.open(
        'data_grunn.json',
        remote='azure_storage') as fd:
        data = json.loads(fd.read())
        print(data['result']['records'][0])

print("initializing dvc now, and commit the data")
init_dvc()
subprocess.call(["dvc", "add", "data/data_grunn.json"])
subprocess.call(["dvc", "add", "data/data_text_only_grunn.json"])

print("setting-up remote storage and push the data")
init_remote_storage_dvc(connection_string=) # TODO fill in this step with azure connection string :)
subprocess.call(['dvc', 'push'])

# TODO STEP 1.B: initialize dvc and add version control the dataset

# TODO Step 5: checkout the old dataset
# subprocess.call(['dvc checkout data/data_grunn.json'])
# subprocess.call(['dvc checkout data/data_text_only_grunn.json'])
