import numpy as np
import matplotlib.pyplot as plt

velocidad = np.linspace(10,100,50)

rho = 1.225
S = 1.5
CL = 0.8

L = 0.5 * rho * velocidad**2 * S * CL

plt.plot(velocidad, L)

plt.xlabel("Velocidad (m/s)")
plt.ylabel("Sustentacion (N)")
plt.title("Sustentacion vs velocidad")

plt.show()