from itertools import combinations

n = 4  # int(input())
s = ['a', 'a', 'b', 'c']  # [*list(c for c in input())]
k = 2  # int(input())

c = list(combinations(s, k))
print(*c)
ca = [ci for ci in c if 'a' in ci]
print(*ca)


# v = [*list(i+1 for i in range(n))]
# c = combinations(v, k)
# top, bottom = 0.0, 0.0
# cl = []
# for cb in c:
#     bottom += 1
#     if s[cb[0]-1] == 'a' or s[cb[1]-1] == 'a':
#         cl.append(cb)
#         top += 1

# print('{:.4f}'.format(top/bottom))

# print(*cl)

# c = combinations(v, k)
# print('all combos:', *c)
# c_a = list(ci for ci in c if s[ci[0]-1] == 'a' or s[ci[1]-1] == 'a')
# print('combos with "a":', *c_a)
