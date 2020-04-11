l = []
for _ in range(int(input())):
    _, a = input(), set(list(map(int, input().split())))
    print(*a)
    _, b = input(), set(list(map(int, input().split())))
    if a.intersection(b) == a:
        l.append("True")
    else:
        l.append("False")
print(*l, sep='\n')
