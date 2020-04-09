n = int(input())+1
print('---')
for i in range(1, n):
    print(sum(map(lambda k: 10**k, range(0, i)))**2)  # 11 square
