import numpy as np
import matplotlib.pyplot as plt

# tracé d'une boule (pour le workspace)

# paramètres
R = 10
Nx, Ny, Nz = 10, 10, 10 # maillage Nx * Ny * Nz

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(-R,R,Nx)
Y = np.linspace(-R,R,Ny)
Z = np.linspace(-R,R,Nz)

for x in X:
    for y in Y:
        for z in Z:
            if x**2 + y**2 + z**2 <= R**2:
                ax.scatter(x,y,z, color="C1")

ax.set_title(f"\"Boule\" : maillage {Nx} x {Ny} x {Nz}, volume d'étude {R}$^3$")

ax.set_xlim(-R,R)
ax.set_ylim(-R,R)
ax.set_zlim(-R,R)

plt.show()