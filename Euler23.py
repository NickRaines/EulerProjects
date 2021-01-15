import math 

def isAbundant(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if( n % i == 0):
            factors.append(i)
            factors.append(int(n/i))
    return (sum(factors) - n) > n


print("program starting")

abundants = []
for i in range(0, 28124):
    if isAbundant(i):
        abundants.append(i)

ints = set()
for i in range(0, len(abundants)):
    for j in range(0, len(abundants)):
        if(abundants[i] + abundants[j] < 28124):   
            ints.add(abundants[i] + abundants[j])

print(ints)
print(sum(range(0,28124)) - sum(ints))