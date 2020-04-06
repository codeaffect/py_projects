from itertools import combinations
s, k = input().split()
sorted_s = sorted(s)
for j in range(int(k)+1):
    if j == 0:
        continue
    combo_s = [''.join(i) for i in combinations(sorted_s, j)]
    print(*combo_s, sep='\n')
#print(*[''.join(i) for i in combinations(sorted(s), int(k))], sep='\n')
