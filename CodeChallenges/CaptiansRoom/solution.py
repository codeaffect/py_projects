n = int(input())
r = list(map(int, input().split()))
print((sum(set(r))*n - sum(r))//(n-1))
