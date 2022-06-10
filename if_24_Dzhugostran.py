import math
for i in range(-5,6):
    h = i/2 
    x = math.pi * h
    if x > 0:
        y = 2*math.sin(x)
    else:
        y = 6 - x
    print("h = {0} : x = {1:.4f} : f(x) = {2:.4f}".format(h,x,y))