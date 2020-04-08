from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)

for i in range(n):
    x = input()
    d[x].append(i+1)

mlist = list([input() for _ in range(m)])

for x in mlist:
    print(' '.join(map(str, d[x])) or -1)
