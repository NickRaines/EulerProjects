print("starting program")

file = open('euler67text.txt')
lines = file.readlines()

lists = []
for l in lines:
    lists.append(l.split(' '))

for l in range(0, len(lists)):
    for s in range(0, len(lists[l] )):
        lists[l][s] = int(lists[l][s][0:2])

for i in range(len(lists) - 1, 0, -1):
    for j in range(len(lists[i]) - 1):
        print("entered the for loop")
        if lists[i][j] < lists[i][j+1]:
            lists[i][j] = lists[i][j+1]
        lists[i-1][j] += lists[i][j]

print(lists[0][0])
for i in lists:
    print(i)