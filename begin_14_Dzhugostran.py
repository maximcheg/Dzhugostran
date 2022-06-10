import random
import math
print("Пи:", math.pi)
L = random.randrange(1,100)
print("Длина окружности: ", L)
R = L / 2 / math.pi
S = math.pi * R**2
print("Радиус окружности: ", R)
print("Площадь круга: ", S)