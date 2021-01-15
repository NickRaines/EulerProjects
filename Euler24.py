# there are an even number of permutations with each number at the front, so of 10! = 3628800 permutations, 362880 start with each number.
# starting with:
# 0 = 0 - 362880
# 1 = 362881 - 725760
# 2 = 725761 - 1088640

# so the 1,000,000th in lexicographic order will start with a 2

# there are 9 remaining digits which have the numbers starting with 2 split between them, so 40320 of the 362880 will start with each number.
# starting with:
# 20 = 725761 - 766081
# 21 = 766082 - 806401
# 23 = 806402 - 846721
# 24 = 846722 - 887041
# 25 = 887042 - 927361
# 26 = 927362 - 967681
# 27 = 967682 - 1008001

# so the 1,000,000th digit will start with 27. We can automate this process.

import math
print("program starting")
n = math.factorial(10)
digits = list()
digit = 0

start = 0
end = n
for i in range(10, 0, -1):
    
    step = (end-start) / i
    print(start, end, step, digits)
    while start + step < 1000000:
        start+=step
        digit += 1 # finds the appropriate digit in order of the ones left
    while digit in digits:
        digit += 1 # finds the actual digit 
    digits.append(digit)
    digit = 0
    end = start + step

print(digits)