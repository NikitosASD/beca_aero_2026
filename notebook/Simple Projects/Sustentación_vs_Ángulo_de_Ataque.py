import numpy as np
import matplotlib.pyplot as plt

# Constantes:
rho = 1.225         # Densidad del aire (kg/m^3)
v = 50              # Velocidad del flujo (m/s)
S = 15              # Superficie alar (m^2)
a = 0.11            # Pendiente de sustentación
alpha_0 = -2        # Ángulo de sustentación nula

# Rango de ángulos
# "vector" que va desde -5 hasta 15 grados con 100 puntos intermedios.
alpha = np.linspace(-5, 15, 100)

# Cálculo de CL
CL = a * (alpha - alpha_0)

# Cálculo de sustentación
L = 0.5 * rho * (v**2) * S * CL

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(alpha, L, label = "Sustentación (L)", color = "blue", linewidth = 2)
plt.title("Sustentación vs Ángulo de Ataque (Alpha)")
plt.xlabel("Ángulo de Ataque (°)")
plt.ylabel("Fuerza de Sustentación (N)")
plt.grid(True)
plt.legend()
plt.show()