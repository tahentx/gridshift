import csv
from collections import Counter
import re
fac = open('faculty.csv')
facReader = csv.reader(fac)
next(facReader)
data = list(facReader)
keys = [name[0] for name in data]
values = [x[1:] for x in data]
f = dict(zip(keys,values))
return f
# x = dict.fromkeys([])