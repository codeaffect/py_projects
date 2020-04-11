n = int(input())
s = set(list(map(int, input().split()))[:n])
k = int(input())
for _ in range(k):
    x = input().split()
    if x[0] == "intersection_update":
        s.intersection_update(set(list(map(int, input().split()))[:int(x[1])]))
    elif x[0] == "update":
        s.update(set(list(map(int, input().split()))[:int(x[1])]))
    elif x[0] == "symmetric_difference_update":
        s.symmetric_difference_update(
            set(list(map(int, input().split()))[:int(x[1])]))
    elif x[0] == "difference_update":
        s.difference_update(set(list(map(int, input().split()))[:int(x[1])]))
print(sum(s))
