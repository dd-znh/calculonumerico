import math

a, b =  0.7685398643432143, 0.7855179720146774 # intervalo a0, b0
r = None

def f(x): # funcao
    return math.sin(x) - math.cos(x)

def r(x):
    return f(a) - (((f(b) - f(a)) / (b-a)) * (x-a))

xk = a - ((f(a) * (b-a)) / (f(b) - f(a)))

if f(xk) == 0:
    print(xk)
else:
    if f(xk) * f(a) < 0:
        print([a, xk])
        print(xk - a)
    else:
        if f(xk) * f(b) < 0:
            print([xk, b])
            print(b-xk)

