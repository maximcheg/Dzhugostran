import random
A,B,C = sorted(random.sample(range(-10, 10), 3))
print("A = {0}, B = {1}, C = {2}".format(A,B,C))
A,C = C,A
A,B = B,A
print("A = {0}, B = {1}, C = {2}".format(A,B,C))