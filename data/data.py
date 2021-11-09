import urllib3
import json

http = urllib3.PoolManager()
resource_id_grunn = 'edc8db66-8dc3-4819-9935-e6c8f55388ab'
limit = 50000
url = 'https://ckan.dataplatform.nl/api/action/datastore_search?limit={}&resource_id={}'.format(limit, resource_id_grunn)
response = http.request('GET', url)
data = json.loads(response.data)

# Write away the open data to a json file
with open('data_grunn.json', 'w') as fp:
    json.dump(data, fp)

# TODO STEP 1.A: Download the dataset