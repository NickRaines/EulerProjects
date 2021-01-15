import math
def sumOfDivisors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if( n % i == 0):
            factors.append(i)
            factors.append(int(n/i))
    return sum(factors) - n


print("program started")

n = 10000
amicable = []

for i in range(0, n):
    a = sumOfDivisors(i)
    b = sumOfDivisors(a)
    if b == i and i != a:
        amicable.append(a)

print(sum(amicable))