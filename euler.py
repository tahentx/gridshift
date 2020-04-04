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
print(Fibonacci(9)) 
  
