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

def paint(start,end):
    jobs = range(start,end + 1)
    total = [job for job in jobs]
    broke = [[int(x) for x in str(val)] for val in total]
    print(broke)
paint(99,160)
