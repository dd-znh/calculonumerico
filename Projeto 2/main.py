import numpy as np
import matplotlib.pyplot as plt

# Definindo constantes
g = 9.81  # aceleração gravitacional em m/s^2
L = 0.1   # comprimento do pêndulo em metros

# Definindo a função que representa o sistema de equações diferenciais
def pendulum_system(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -(g/L) * np.sin(theta)
    return np.array([dtheta_dt, domega_dt])

# Método de Runge-Kutta de quarta ordem
def runge_kutta_4(f, y0, t0, tf, dt):
    t = t0
    y = y0
    while t < tf:
        k1 = f(t, y)
        k2 = f(t + 0.5 * dt, y + 0.5 * dt * k1)
        k3 = f(t + 0.5 * dt, y + 0.5 * dt * k2)
        k4 = f(t + dt, y + dt * k3)
        y = y + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t = t + dt
    return y

# Parâmetros iniciais
theta0 = np.pi / 4  # posição angular inicial
omega0 = 0          # velocidade angular inicial
y0 = np.array([theta0, omega0])
t0 = 0              # tempo inicial
tf = float(input("Digite o valor de T (em segundos): "))  # tempo final fornecido pelo usuário
dt = 0.01           # passo de tempo

# Resolvendo o sistema de EDOs
resultado = runge_kutta_4(pendulum_system, y0, t0, tf, dt)
theta_final = resultado[0]

print(f"A posição angular do pêndulo após {tf} segundos é {theta_final} radianos")