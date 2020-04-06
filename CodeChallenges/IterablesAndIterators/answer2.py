from itertools import combinations

_, s, n = input(), input().split(), int(input())
c = list(combinations(s, n))
ca = [c1 for c1 in c if 'a' in c1]
print(len(ca)/len(c))
