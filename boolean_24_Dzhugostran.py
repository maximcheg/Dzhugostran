import numpy as np
import random
A = random.randint(1,10)
B,C = list(np.random.choice(range(1, 11), 2))
print("A = {0}, B = {1}, C = {2}".format(A,B,C))
D = B*B - 4*A*C
x = (D >= 0)
print("Дискриминант:",D)
print("Квадр. уравн. {0}x^2 + {1}x + {2} = 0 имеет вещественные корни: ".format(A,B,C), x)