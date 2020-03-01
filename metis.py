from statistics import stdev
b = [-5,3,12,190,-10]
from statistics import mean
b_mean = mean(b)
b_sorted = sorted(b)
# print(b_sorted)
from statistics import pstdev
sd = pstdev(b)
# print(sd)
from statistics import pvariance
foo = pvariance(b)
# print(foo)

from collections import Counter
def find_all(array,n):
    count = Counter(array)
    for key,value in count.items():
        if key == n:
            print(value)
            break
        else:
            print("Value not present")
# find_all([32,542,6],32)

# kata: https://www.codewars.com/kata/5572f7c346eb58ae9c000047/train/python
# def pattern(n):
#     from collections import Counter
#     count = Counter()
#     x = [1]
#     while len(x) < 10:
#         for num in x:
#             count[num] += 1
#     print(count)
# pattern(10)

# import itertools
# def counter(n):
#     i = n
#     while i < 6:
#         print(str(i) * i)
#         i += 1

# testing
from functools import reduce
def sum_of_minimums(numbers):
    foo = reduce((lambda x: min(x),numbers))
    print(foo)
# sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ])

    
# kata: https://www.codewars.com/kata/56f4ff45af5b1f8cd100067d
def sort_by_name(arr):
    import inflect
    p = inflect.engine()
    word = p.numbers_to_words(arr)
    print(word)
# sort_by_name(55)

# kata: https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python
def two_oldest_ages(ages):
    max_ages = [min(x) for x in ages]
    print(max_ages)
# two_oldest_ages([14,16,9,4,15])
import itertools
import operator
def max_gap(numbers):
    numbers.sort()
    diff = list(itertools.starmap(operator.sub, zip(numbers[1:], numbers)))
    return max(diff)

# def max_gap(numbers):
#     lst = sorted(numbers)
#     return max(b-a for a,b in zip(lst, lst[1:]))
# max_gap([3,5,9])