def recursiveSolve(lists, row, column):
    if row == len(lists) - 1:
        return (lists[row][column])
    else:
        left = recursiveSolve(lists, row+1, column)
        right = recursiveSolve(lists, row+1, column+1)
        return lists[row][column] + (left if left>right else right)

print("starting program")

file = open('euler18text.txt')
lines = file.readlines()

lists = []
for l in lines:
    lists.append(l.split(' '))

# the indices for the possible next steps of each node are n and n+1

# this can be done since everything is 2 digits
for l in range(0, len(lists)):
    for s in range(0, len(lists[l] )):
        lists[l][s] = int(lists[l][s][0:2])
        
print(recursiveSolve(lists, 0, 0))

