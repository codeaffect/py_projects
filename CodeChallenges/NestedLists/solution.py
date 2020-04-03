n = int(input())

marks = [0]*n
names = [None]*n
maxscore = 0.0
maxScoreIndex = 0

for i in range(n):
    # print('>> Iteration %d' % i)
    names[i] = input()
    marks[i] = float(input())
    if marks[i] >= maxscore:
        maxscore = marks[i]
        maxScoreIndex = i
#print('---current Set:')
print([[names[i], marks[i]] for i in range(n)])
# print('maxScore:', maxscore)

del marks[maxScoreIndex]
del names[maxScoreIndex]

# print('len after: %d -- %d' % (len(marks), len(names)))

maxscore = 0.0
for i in range(n-1):
    if marks[i] >= maxscore:
        maxscore = marks[i]
        maxScoreIndex = i

# print('second max: %s -- %f' % (names[maxScoreIndex], marks[maxScoreIndex]))

# result = [[names[i], marks[i]]
result = [[names[i], marks[i]]
          for i in range(n-1) if marks[i] == maxscore]

# print('-- Results is ---')
print(sorted(result))
