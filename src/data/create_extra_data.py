import json

texts = [
    "Het is echt ontzettend gevaarlijk om hier te fietsen in het donker 's nachts",
    "Ik heb er zo'n ontzettende hekel aan dat mijn buren steeds mijn parkeerplekje innemen, waarom realiseert de gemeente niet gewoon meer plekken? Zeker ten koste van die lindenbomen hier in de straat.",
    "Er zit een zinkgat in het troittoir, mijn oma is hier al ingevallen :( Help a.u.b.",
    "Zeer donker pad ik zou graag extra straatverlichting aan dit pad willen.",
    "Deze straatverlichting is kapot",
    "Ik schaam mij diep om in deze stad te wonen, alles is kapot hier!",
    "De verkeerslichten zijn kapot, ik zou graag willen dat dit gerepareerd word",
    "Er zijn niet voldoende parkeerplekken aanwezig",
    "Mijn kat zit al de hele dag te miauwen, ik word er gek van. Deze app is de enige contact met de buiten wereld :(",
    "Gemeente, je word weer bedankt!",
    "De vuilnisbakken zitten weer vol :)",
    "Al die rot studenten hier maken de buurt onleefbaar, ik kan niet eens meer op zondag mijn afval weggooien"]
labels = [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]


# Store the data locally in JSON format
with open('data/extra_data_grunn_features.json', 'w') as fp:
    json.dump(texts, fp)

with open('data/extra_data_grunn_labels.json', 'w') as fp:
    json.dump(labels, fp)

def add_extra_feature_to_tracked_dataset():
    filename_source_dataset = 'data/data_text_only_grunn.json'
    with open(filename_source_dataset, 'r') as f:
        source_dataset = json.loads(f.read())

    filename_extra_dataset = 'data/extra_data_grunn_features.json'
    with open(filename_extra_dataset, 'r') as f:
        extra_dataset = json.loads(f.read())
    
    new_dataset = extra_dataset + source_dataset
    with open(filename_source_dataset, 'w') as f:
        f.write(json.dumps(new_dataset))

add_extra_feature_to_tracked_dataset()

# TODO Step 3.A: Manually add new features & labels to fine tune the model
