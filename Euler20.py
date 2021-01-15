def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("started program")
sum = 0
x = factorial(100)
while x > 0:
    sum += x%10
    x = x//10

print(sum)