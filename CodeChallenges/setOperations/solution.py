n = int(input())
s = set(map(int, input().split()))
k = int(input())
for _ in range(k):
    x = input().split()
    if x[0] == "pop" and len(s) > 0:
        s.pop()
    elif x[0] == "remove" and int(x[1]) in s:
        s.remove(int(x[1]))
    elif x[0] == "discard":
        s.discard(int(x[1]))

print(sum(s))
