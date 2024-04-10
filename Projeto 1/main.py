import mod_min_max, cauchy, kojima, fake_position, secantes

def compute_best_quota(P):
    return min(mod_min_max(P), cauchy(P), kojima(P))

def compute_root(P, a_b1, a_b2):
    max_inter = 5000
    x0 = (a_b1 + a_b2) / 2
    x1 = x0 + 0.01
    if P(a_b1) * P(a_b2) <= 0:
        return fake_position(P, a_b1, a_b2, max_inter, x0, x1)
    return secantes(P, a_b1, a_b2, max_inter, x0, x1)

def read_poly(n):
    l = []
    for _ in range(n):
        l.append(input)

n = input()  # Grau do polinômio

P = read_poly(n) # Coeficientes dos polinômios

a_b = compute_best_quota(P)

print("Best quotas = [%.2f, %.2f]\n", a_b(1), a_b(2));
x = compute_root(P, a_b(1), a_b(2));
print("%6f\n", x);
