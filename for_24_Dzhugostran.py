import math
X = math.pi/4
N = 10
print('X = ', X)
print('N = ', N)
p = X
S = X
k = 0
for i in range(1,N+1):
    k += 2
    p *= (-1) * X * X / (k * (k + 1))
    S += p
    print(i," : ", k," : ", k+1," : ", p," : ", S)
print("Result:")
print(S)
print("sin:")
print(math.sin(X))