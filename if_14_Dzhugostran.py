import random
A = random.randrange(-30,30)
B = random.randrange(-30,30)
C = random.randrange(-30,30)
print("Число A:", A)
print("Число B:", B)
print("Число C:", C)
if A < B:
    mn = A
    mx = B
else:
    mn = B
    mx = A
if mx < C:
    mx = C
if mn > C:
    mn = C    
    
print()    
print("Минимум:", mn)
print("Максимум:", mx)