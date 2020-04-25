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
    # find sample standard deviation
    mean = (sum(sample)) / len(sample)
    sq = list(map(lambda x: (x - mean) ** 2, sample))
    sigma = sum(sq) / len(sq)
    standard_dev = sqrt(sigma)
    # calculate boundary using cutoff value
    boundary = standard_dev * cutoff
    print(boundary)
    for x in sample:
        y = abs(x - (sum(sample)/len(sample)))
        if y > boundary:
            sample.remove(x)
        else:
            pass


        
    
# outlier_removal([9, 2, 5, 4, 120, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4],2)




from functools import reduce
def find_closest(l,j):
    product = reduce((lambda x,j: x - j), l)
    print(product)

# find_closest([1, -1, -5, 2, 4, -2, 1],3)


import functools
def OneEditAway(s1,s2):
    # compare the two lists to see if there is just one letter different
    res = [x for x in s1 + s2 if x not in s1 or x not in s2]
    if len(res) == 2:
        return True 
    # compare the two to see if there is one additional letter, or one less
    s1 = list(s1)
    s2 = list(s2)
    if len(s1) + 1 == len(s2):
        return True
    elif len(s1) - 1 == len(s2):
        return True
    else:
        return False
# assert OneEditAway('pea', 'peas') == True

# assert OneEditAway('pea', 'fleas') == False

# assert OneEditAway('pea', 'lea') == True

# assert OneEditAway('pea', 'seas') == False
# OneEditAway("pea","lea")

# https://www.codewars.com/kata/529e2e1f16cb0fcccb000a6b/train/python

# def split_integer(num,parts):
#     assert isinstance(num,int)
#     assert isinstance(parts,int)
#     x = (num/parts) * parts
#     print(x)
    
    # group = list(base * len(parts))
    # if thresh < num:
    #     diff = num - thresh
    #     while diff > 0:
            
    # elif thresh > num:
    #     print("above")
    # else:
    #     return base

# split_integer(20,6)
from collections import namedtuple
def disperse_change(cost, paid):
    Denomination = namedtuple('Denomination', 'name value')
    denominations = [
        Denomination("Twenties", 20.00),
        Denomination("Tens", 10.00),
        Denomination("Fives", 5.00),
        Denomination("Ones", 1.00),
        Denomination("Quarters", 0.25),
        Denomination("Dimes", 0.10),
        Denomination("Nickles", 0.05),
        Denomination("Pennies", 0.01)
    ]

    change = round(paid-cost,2)
    print(f'Change due: {change}')

# disperse_change(23.38, 25)
def ways(cents):
    coins = [1,5]
    combos = []
    for coin in coins:
        combos.append(coin)
        if sum(combos) == cents:
            break
    print(combos)
# ways(55)

from itertools import combinations
def group_cities(seq):
    for s in seq:
        matches = []
        s = set(s.lower())
        for a,b in combinations(seq,2):
            if set(a.lower()) == set(b.lower()):
                matches.append(a)
    return set(matches)

group_cities(['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot'])