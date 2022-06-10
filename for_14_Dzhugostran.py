import random
N = random.randrange(1,15)
print('N = ', N)
S = 0.0
for i in range(1,N+1):
    x = 2 * i - 1
    S += x
    print(i," : ",x," : ",S)
print("Sum = ",S)