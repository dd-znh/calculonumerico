import f

def fake_position(P, x0, x1, max_inter, tol=1e-6):
    cont = 0
    x2 = x0

    while cont < max_inter:
        f0 = f.f(P, x0)
        f1 = f.f(P, x1)
        
        x2 = x0 - f0 * ((x1 - x0) / (f1 - f0))
        
        if abs(f.f(P, x2)) < tol:
            return x2
        
        if f.f(P, x0) * f.f(P, x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        cont += 1

    return x2