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

import random
import time

# def guess_num(num):
#     numbers = list(range(1,101))
#     count = 1
#     while len(numbers) > 1:
#         half = len(numbers)// 2
#         if num > half:
#             numbers = numbers[half:]
#             count += 1
#         elif num < half:
#             numbers = numbers[:half]
#             count += 1
#     return count

# def slippin(word):
#     half = len(word) // 2
#     print(word[:half])
# slippin("breads")

from math import sqrt
def outlier_removal(sample,cutoff):
    mean = (sum(sample)) / len(sample)
    standard_devs = list(map(lambda x: (x - mean) ** 2, sample))
    print(standard_devs)


outlier_removal([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4],5)
