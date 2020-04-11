n = int(input())
a = set(list(map(int, input().split()))[:n])
n = int(input())
print(len(a.union(set(list(map(int, input().split()))[:n]))))
