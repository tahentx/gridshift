import csv
from collections import Counter
fac = open('faculty.csv')
facReader = csv.reader(fac)
data = list(facReader)

creds = [x[1] for x in data]
c = Counter(creds)
c["PhD/Ph.D."] = c['PhD'] + c['Ph.D.']


        
print(c["PhD/Ph.D."])
print(c)