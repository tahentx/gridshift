# Problem 1
def euler_one(num):
    factors = []
    count = 0
    while count < 10:
        if count % 3 == 0:
            factors.append(num)
            count += 1
        else:
            count += 1
    print(factors)
euler_one(1)
