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
find_all([32,542,6],32)
