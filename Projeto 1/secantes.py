import f

def secantes(P, x0, x1, max_inter):
    cont = 0
    x2 = None

    while (x2 == None or abs(f.f(P, x2)) >= 0.000001) and cont < max_inter:
        cont += 1
        x2 = (x0 - (f.f(P, x0)/((f.f(P, x1) - f.f(P, x0)) / (x1 - x0))))
        x0 = x1
        x1 = x2

    return float(x2)
