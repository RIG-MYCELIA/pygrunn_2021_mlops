import json

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
