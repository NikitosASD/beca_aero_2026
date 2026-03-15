# postprocess_pressure.py



import pandas as pd
import matplotlib.pyplot as plt



# Ruta al CSV
csv_path = r"A:\CFD\OpenFOAM\pitzDaily\data\velocity_along_channel.csv"

# Leer archivo
data = pd.read_csv(csv_path)

# Verificar columnas
print("Columnas del archivo:")
print(data.columns)

# Posición a lo largo del canal
x = data["Points:0"]

# Velocidad en dirección x
velocity_x = data["U:0"]

# Crear gráfico
plt.figure(figsize=(8,5))
plt.plot(x, velocity_x)

plt.xlabel("Position along channel (m)")
plt.ylabel("Velocity Ux (m/s)")
plt.title("Velocity profile along channel - pitzDaily")
plt.grid(True)

# Guardar imagen
plt.savefig(r"A:\CFD\OpenFOAM\pitzDaily\images\velocity_profile_plot.png", dpi=300)
plt.savefig("images/velocity_profile_plot.png", dpi=300)

plt.show()