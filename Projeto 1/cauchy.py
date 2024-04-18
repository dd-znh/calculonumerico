def cauchy(P):
    # eq são os coeficientes da nova equação
    eq = []
    for i in range(1, len(P)):
        eq.append(abs(P[i] / P[0]))

    # eq vai ser elevada por esse valor no final
    e = len(P) - 1

    x = 1
    x1 = 0
    tolerance = 0.0001
    while True:
        x = x1
        x1 = 0
        for i in range(len(eq)):
            x1 += eq[i] * (x ** (e - i - 1))
        x1 = round(x1 ** (1 / e), 4)

        if abs(x1 - x) < tolerance:
            break

    return float(x1)
