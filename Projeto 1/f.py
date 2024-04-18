def f(P, x):
    y = 0
    n = len(P) - 1  # Determina o grau do polinômio (n)
    for i in range(len(P)-1):
        # Calcula a contribuição de cada termo do polinômio
        y += P[i] * (x ** (n - i))
    y += P[len(P)-1]
    return y
