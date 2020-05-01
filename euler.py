# Problem 1
def euler_one(num):
    factors = []
    count = 0
    for x in range(1,1000):
        if x % 3 == 0:
            factors.append(x)
        elif x % 5 == 0:
            factors.append(x)
    total = sum(factors)
    return total
# euler_one(1)

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
# print(Fibonacci(9)) 

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
t =  [4, 4, 4, 9, 10, 11, 12]
# moving_average(t)

# nums = list(range(1,101))
# sum_sq = sum(list(map(lambda x: x ** 2, nums)))
# sq_sum = sum(nums) ** 2
# answer = sq_sum - sum_sq
# print(answer)
  
def largest(a, b):
    candidates = []
    while a > 0:
        product = a * b
        candidates.append(product)
        a = a - 1
        b = b - 1
    print(candidates)

# largest(3,3)

import numpy as np

def num_demo(n, v = np.random.rand(5,1)):
    arr = np.arange(n)
    new_arr = np.reshape(arr,(5,5))
    val = np.dot(new_arr,v)
    print(val)
    

# num_demo(25)

