import numpy
n = int(input().strip())
arr1 = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr2 = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.dot(arr1, arr2))
