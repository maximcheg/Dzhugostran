import random
import numpy
M = random.randrange(2,10)
N = random.randrange(2,10)
print("M = ",M,"; N = ",N)
a = numpy.zeros((M, N))
c = [random.randrange(1,5) for i in range(N)]
print("Набор из ",N," чисел:")
print(c)
print()
for i in range(M):
    for j in range(N):
        a[i][j] = c[j]
print(a)
print()
Matrix = [c for y in range(M)]
print(Matrix)