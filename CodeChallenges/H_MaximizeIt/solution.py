from itertools import product

k, m = map(int, input().split())
n = (list(map(int, input().split()))[1:] for _ in range(k))

p = list(product(*n))

#results1 = map(lambda x: sum(i**2 for i in x) % m, p)
results = []
for x in p:
    # print(x)
    f = (sum(i*i for i in x)) % m
    results.append(f)

print(max(results))
