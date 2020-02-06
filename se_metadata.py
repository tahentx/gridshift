import json
from collections import namedtuple
path = '/Users/toddhendricks/Public/code/gridshift/metdata.json'
with open(path, 'r') as j:
     contents = json.loads(j.read())
dataset = namedtuple('dataSet', ['Access','Code', 'modified'])
tucson = dataset(contents['accessLevel'],contents['bureauCode'],contents['modified'])
print(tucson)