import csv
from collections import Counter
import re
fac = open('faculty.csv')
facReader = csv.reader(fac)
next(facReader)
data = list(facReader)
# keys = [name[0] for name in data]
# values = [x[1:] for x in data]
# f = dict(zip(keys,values))
# return f
# x = dict.fromkeys([])
# name_list = [n[0] for n in data]
# name_split = [tuple(name.split()) for name in name_list]
# values = [entry[1:] for entry in data]
# faculty_names = dict(zip(name_split,values))
# return faculty_names
from collections import Counter
def paint(start,end):
    jobs = range(start,end + 1)
    total = [job for job in jobs]
    broke = [[int(x) for x in str(val)] for val in total]
    flat_list = [item for sublist in broke for item in sublist]
    return c.values()

# paint(99,160)

def interval_insert(myl):
    l = [list(entry) for entry in myl] 
    flat = [item for sublist in l for item in sublist]
    flat.sort()
    bounds = range(min(flat),max(flat))
    print(bounds)
# interval_insert([(1,3,5),(4,5,2)])

def calculate(s):
    import re
    operator = re.sub(r'\dminus\d','-',s)
    print(operator)
# calculate('1minus2minus3minus4')

