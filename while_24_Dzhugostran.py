import random
N = random.randrange(1,100000)
N = 4181
print("N = ",N)
F1 = F2 = 1
print(F1,end="; ")
print(F2,end="; ")
while F2 < N:
    F1, F2 = F2, F1+F2
    print(F2,end="; ")
print()
if F2 == N:
    print("TRUE")
else:
    print("FALSE")