def fake_position(P, a_b1, a_b2, max_inter):

    cont = 0
    while cont < max_inter:
        cont += 1

        def f(P, x):
            y = 0
            for i in range(len(P)):
                y += P[i] * (x**(len(P)-2))
            return y

        def r(x):
            return f(a_b1) - (((f(a_b2) - f(a_b1)) / (a_b2 - a_b1)) * (x - a_b1))
        
        xk = a_b1 - ((f(a_b1) * (a_b2-a_b1)) / (f(a_b2) - f(a_b1)))

        if f(xk) == 0:
            print(xk)
        else:
            if f(xk) * f(a_b1) < 0:
                a_b2 = xk
            elif f(xk) * f(a_b2) < 0:
                a_b1 = xk
            else: # xk é a raíz
                return xk
