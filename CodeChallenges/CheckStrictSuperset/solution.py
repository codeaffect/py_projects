a = set(list(map(int, input().split())))
v = True
for _ in range(int(input())):
    b = set(list(map(int, input().split())))
    if len(b.intersection(a)) != len(b) or len(b.difference(a)) != 0:
        v = False
print(v)
