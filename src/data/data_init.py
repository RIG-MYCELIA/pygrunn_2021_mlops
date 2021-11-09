import urllib3
import json

http = urllib3.PoolManager()
resource_id_grunn = 'edc8db66-8dc3-4819-9935-e6c8f55388ab'
limit = 2000
url = 'https://ckan.dataplatform.nl/api/action/datastore_search?limit={}&resource_id={}'.format(limit, resource_id_grunn)
response = http.request('GET', url)
data = json.loads(response.data)

# Write away the open data to a json file
with open('data/data_grunn.json', 'w') as fp:
    json.dump(data, fp)

def preprocess_grunn():
    with open('data/data_grunn.json') as f:
        data = json.loads(f.read())
    
    data_text_only = []
    for record in data['result']['records']:
        if record['description']:
            data_text_only.append(record['description'])
    
    with open('data/data_text_only_grunn.json', 'w') as f:
        f.write(json.dumps(data_text_only))

preprocess_grunn()
# TODO STEP 1.A: Download the dataset