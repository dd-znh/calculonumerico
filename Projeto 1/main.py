import mod_min_max, cauchy, kojima, fake_position, secantes, f

def compute_best_quota(P) -> tuple:
    vet = mod_min_max.mod_min_max(P)
    a = min(vet[0], cauchy.cauchy(P), kojima.kojima(P))
    b = min(vet[1], cauchy.cauchy(P), kojima.kojima(P))
    return [a, b]

def compute_root(P, a_b) -> float:
    max_inter = 5000
    if (f.f(P, a_b[0])) * (f.f(P, a_b[1])) <= 0:
        return fake_position.fake_position(P, a_b[0], a_b[1], max_inter)
    else:
        x0 = (a_b[0] + a_b[1]) / 2
        x1 = x0 + 0.01
        return secantes.secantes(P, x0, x1, max_inter)

def read_poly(n) -> list:
    l = []
    for _ in range(n+1):
        aux = int(input())
        l.append(aux)
    return l

def main():
    n = int(input())  # Grau do polinômio
    P = read_poly(n) # Coeficientes dos polinômios

    a_b = compute_best_quota(P)
    print(f"Best quotas = [{a_b[0]:.2f}, {a_b[1]:.2f}]")
    x = compute_root(P, a_b)
    print(f"{x:.6f}")
main()
