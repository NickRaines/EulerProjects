print("Started working")
f = open("C:\\Users\\ni4ch\\Documents\\Python Scripts\\euler13text.txt")
data = f.readlines()

for s in range(0, len(data)):
    data[s] = data[s][0 : len(data[s]) - 3]
    
print(data)

# if you only want the first 10 digits of the sum, you only have to add the first digits of each number * 10^10 + second digits * 10^9 etc. for the first ~15 numbers

sum = 0
for i in range(0, 15):
    for s in range(0, len(data)):
        sum += int(data[s][i]) * 10**(15 - i)

print("sum is: " + str(sum))
