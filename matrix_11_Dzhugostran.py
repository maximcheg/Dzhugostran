import random
import numpy
M = random.randrange(2,10)
N = random.randrange(2,10)
print("M = ",M,"; N = ",N)
a = numpy.zeros((M, N))
k = 0
for i in range(M):
    for j in range(N):
        k += 1
        a[i][j] = k
print(a)
for i in range(M):
    if i%2 == 0:
        print(a[i])
    else:
        print(a[i][::-1])
b = []
for i in range(M):
    b.append([])
    for j in range(N):
        b[i].append(a[i][j])
print(b)
for i in range(M):
    if i%2 == 0:
        print(b[i])
    else:
        print(b[i][::-1])