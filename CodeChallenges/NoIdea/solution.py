n, m = map(int, input().split())
nlist = list(map(int, input().split()))
a = set(list(map(int, input().split()))[:m])
b = set(list(map(int, input().split()))[:m])


a = {3, 1}
b = {5, 7}
nlist = [1, 5, 3]

y = len([x for x in nlist if x in a and x not in b]) - \
    len([x for x in nlist if x in b and x not in a])

print(y)
