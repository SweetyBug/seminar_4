#Вычислить результат деления двух чисел c заданной точностью d
import math
from decimal import *
def number(d):
    n = 0
    while d <= 1:
        d *= 10
        n += 1
    p = Decimal(math.pi)
    g = str(p)
    s = ""
    for i in range(n+1):
        s += g[i]
    s = float(s)
    print(s)

