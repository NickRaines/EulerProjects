print("program started")
file = open("euler22text.txt")
names = file.readline().split(',')
names.sort()
print(names[0:10])
sum = 0
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, len(names)):
    score1 = i + 1
    score2 = 0
    for letter in names[i]:
        score2 += key.index(letter) + 1
    print(score1 * score2)
    sum += score1*score2

print(sum)