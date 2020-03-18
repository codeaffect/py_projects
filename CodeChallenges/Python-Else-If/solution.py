import sys

n = int(input().strip())
if n % 2 == 0:
    if n >= 2 and n <= 5:
        print("not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("not Weird")
else:
    print("Weird")
