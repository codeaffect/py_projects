n = int(input())
a = set(list(map(int, input().split()))[:n])
n = int(input())
print(len(a.symmetric_difference(set(list(map(int, input().split()))[:n]))))
