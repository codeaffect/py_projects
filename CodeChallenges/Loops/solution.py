import math

print('Enter Number:')
n = int(input().strip())
for x in range(n):
    y = int(math.pow(x, 2))
    print(y)
