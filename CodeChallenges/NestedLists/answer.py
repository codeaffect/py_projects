import sys

n = int(input())
names = [None]*n
marks = [0]*n

for i in range(n):
    names[i] = input()
    marks[i] = float(input())

minMarks = min(marks)
areallSame = [names[i] for i in range(n) if marks[i] == minMarks]

if len(areallSame) == n:
    print(*sorted(names), sept='\n')

minIndex = marks.index(minMarks)
del marks[minIndex]
del names[minIndex]

minMarks = min(marks)
areallSame = [names[i] for i in range(n-1) if marks[i] == minMarks]

if len(areallSame) == n-1:
    print(*sorted(names), sept='\n')

results = [names[i] for i in range(n-1) if marks[i] == minMarks]
# print('-- Results:')
print(*sorted(results), sep='\n')
