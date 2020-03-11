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

def string_reverse_A(input_str):
    input_str = input_str[::-1]
    a_cont = []
    for letter in input_str:
        a_cont.append(letter)
        a_cont.append("A")
    a_string = ''.join(a_cont)
    return a_string
string_reverse_A("hello")

def tweener(lower,upper):
    values = range(lower,upper + 1)
    output = []
    for x in values:
        if x % 2 == 0:
            output.append(x)
        elif x % 7 == 0:
            output.append(x)
        else:
            pass
    return output
tweener(5,9)

def combine_distinct_and_sort(list1,list2):
    a = [char for char in list1 if char not in list2]
    b = [char for char in list2 if char not in list1]
    joined = a + b
    output = sorted(joined)
    return output
combine_distinct_and_sort([3,3,5],[1,4,5])

def can_spell_with(target_word,letter_word):
    letter_word_list = list(letter_word)
    letter_word_set = list(set(letter_word_list))
    letter_lower = [x.lower() for x in letter_word_set]
    target_lower = [x.lower() for x in target_word]
    output = zip(target_lower,letter_lower)
    print([x for x in output])

def create_divisors_dict(divisors,lower,upper):
    d = dict((x,[]) for x in divisors)
    
    span = range(lower,upper + 1)
    for x in span:
        for key in d.keys():
            if x % key == 0:
                d[key].append(x)
    return d

create_divisors_dict([1,2,5],2,4)


# def complex(a):
#     list1 = range(0,20)
#     list2 = [123, 234, 456]
#     d = {'a': [], 'b': []}
#     for val in list1:
#         if val % 2 == 0:
#             d['a'].append(val)
#     print(a)
#     print(d)
# # complex(56)

# kata: https://www.codewars.com/kata/545f05676b42a0a195000d95/train/python
def ranks(a):
    from itertools import count
    a.sort()
    b = list(set(a))
    print(a)
    base = count(start=1,step=1)
    c = zip(a,base)
    for x in c:
        print(x)
# ranks([5,6,2,2,2])

# kata: https://www.codewars.com/kata/5c55ad8c9d76d41a62b4ede3
def duplicates(arr):
    if not arr:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        foo = [x for x in arr if arr.count(x) > 1]
        d = len(set(foo))
        return d
# duplicates([5,9,8,5,1,9])

# kata: https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python
def solve(s):
    import string
    a = list(string.ascii_lowercase)
    vals = zip(a,range(1,len(a) + 1))
    s = list(s)
# solve("Brother")

# kata: https://www.codewars.com/kata/5bdcd20478d24e664d00002c/train/python

def wheat_from_chaff(values):
    neg_values = list(filter(lambda x: x < 0, values))
    pos_values = list(filter(lambda x: x > 0, values))
    combined = neg_values + pos_values
    return combined
# wheat_from_chaff([-4,-5,2,5,-9])

# kata: https://www.codewars.com/kata/56b861671d36bb0aa8000819/train/python
def reverse_and_combine_text(text):
    import itertools
    text = text.split()
    foo = slice(0,2)
    print(text[foo])
# reverse_and_combine_text("Come mister tally man")

# kata: https://www.codewars.com/kata/57f7f71a7b992e699400013f/train/python
def sort_csv_columns(csv_file_content):
    columns = csv_file_content[0]
    columns = columns.split(";")
    print(columns)
sort_csv_columns()