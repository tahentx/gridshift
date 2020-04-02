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
euler_one(1)
