from itertools import groupby
c = [(len(list(g)), int(k)) for k, g in groupby(list(input()))]
print(*c)
