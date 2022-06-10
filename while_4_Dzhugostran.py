import random
#N = random.randrange(1,1000)
N = 81
print('N = ', N)
while N >= 3:
    N /= 3
print("Является степенью 3: ", (N==1))