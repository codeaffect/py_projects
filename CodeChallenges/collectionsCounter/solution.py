n = int(input())
shoe_sizes = list(map(int, input().split()))
# print(*shoe_sizes)
k = int(input())
sum = 0
for _ in range(k):
    buyers = list(map(int, input().split()))
    if buyers[0] in shoe_sizes:
        shoe_sizes.remove(buyers[0])
        # print(*shoe_sizes)
        sum += buyers[1]
        # print(sum)
print(sum)
