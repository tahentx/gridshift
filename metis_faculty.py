import csv
from collections import Counter
import re
fac = open('faculty.csv')
facReader = csv.reader(fac)
next(facReader)
data = list(facReader)
names = [name[0] for name in data]
print(names)
# x = dict.fromkeys([])