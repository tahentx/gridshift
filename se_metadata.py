import json
path = '/Users/toddhendricks/Public/code/gridshift/metdata.json'
with open(path, 'r') as j:
     contents = json.loads(j.read())
