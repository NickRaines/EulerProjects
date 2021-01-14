# n + n quantity of moves must be made, n down and n right. The total number of options is the number of permutations of 20 down and 20 right commands
import math
numMoves = 40

ans = math.factorial(40) / math.factorial(20) / math.factorial(20)
print(ans)