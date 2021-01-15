print("Started program")
num = 2**1000
sum = 0
while num > 0:
    print(num, sum)
    sum += num%10
    num = num//10
print(sum)
