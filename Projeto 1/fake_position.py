import f

def fake_position(P, x0, x1, max_inter):

    cont = 0
    x2 = None

    while cont < max_inter:
        cont += 1

        if (x2 != None and abs(f.f(P, x2)) < 0.000001):
            return x2

        def r(x):
            return f.f(P, x0) - (((f.f(P, x1) - f.f(P, x0)) / (x1 - x0)) * (x - x0))
        
        x2 = x0 - ((f.f(P, x0) * (x1-x0)) / (f.f(P, x1) - f.f(P, x0)))

        if f.f(P, x2) * f.f(P, x0) < 0:
            x1 = x2
        elif f.f(P, x2) * f.f(P, x1) < 0:
            x0 = x2

    return x2
