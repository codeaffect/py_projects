n = int(input())
a = set(list(map(int, input().split()))[:n])
n = int(input())
print(len(a.intersection(set(list(map(int, input().split()))[:n]))))
