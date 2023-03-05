import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Crea una figura y cuatro objetos de ejes (axis) utilizando matplotlib.
# figsize se utiliza para establecer el tamaño de la figura.
sns.set_style('darkgrid') # Agrega el estilo "dark" de Seaborn

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))


# Grafica en el segundo objeto de ejes (axis)
f = lambda x: x**3+2*x**2-4
g_1 = lambda x: x**3 + 2*x**2 + x -4
g_2 = lambda x: (4 - x**3)/(2*x)
g_3 = lambda x: np.sqrt((4 - x**3)/(2))
p_0 = 1
p = 1.1304
tolerancia = 1e-3
max_ite = 5
x_i, x_f = 0.5, 1.5
x = np.linspace(x_i, x_f, 1000)

axs[0,0].plot(x, f(x), label='f(x)')
axs[0,0].set_title('Original', fontsize=16)
axs[0,0].scatter(p, f(p), color='black', label='raíz encontrada', zorder=3)


axs[0,1].plot(x, g_1(x), label='f(x)')
axs[0,1].plot(x, x, label='f(x)')
axs[0,1].scatter(p, 0, color='red', alpha=1, marker='x', zorder=2)
axs[0,1].plot([p, p], [0, g_1(p)], '--', color='red' )
axs[0,1].text(p, 0, f"p", fontsize=14, ha='center', va='top')
axs[0,1].scatter(p, g_1(p), color='black', label='raíz encontrada', zorder=3)
axs[0,1].set_title('Transformación 1', fontsize=16)


axs[1,0].plot(x, g_2(x), label='f(x)')
axs[1,0].plot(x, x, label='f(x)')
axs[1,0].scatter(p, 0, color='red', alpha=1, marker='x', zorder=2)
axs[1,0].plot([p, p], [0, g_2(p)], '--', color='red' )
axs[1,0].text(p, 0, f"p", fontsize=14, ha='center', va='top')
axs[1,0].scatter(p, g_2(p), color='black', label='raíz encontrada', zorder=3)
axs[1,0].set_title('Transformación 2', fontsize=16)

axs[1,1].plot(x, g_3(x), label='f(x)')
axs[1,1].plot(x, x, label='f(x)')
axs[1,1].scatter(p, 0, color='red', alpha=1, marker='x', zorder=2)
axs[1,1].plot([p, p], [0, g_3(p)], '--', color='red' )
axs[1,1].text(p, 0, f"p", fontsize=14, ha='center', va='top')
axs[1,1].scatter(p, g_3(p), color='black', label='raíz encontrada', zorder=3)
axs[1,1].set_title('Transformación 3', fontsize=16)


for ax in axs.flat:
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.tick_params(labelsize=12, axis='x')
    ax.tick_params(labelsize=12, axis='y')
    ax.annotate("", xy=(xmax, 0), xytext=(xmin, 0),
                 arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10), zorder=2)
    ax.annotate("", xy=(0, ymax), xytext=(0, ymin),
                 arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10), zorder=2)

# Ajusta automáticamente los espacios entre los subplots
fig.tight_layout()
plt.savefig('/imagenes/punto_fijo.png', dpi=400, bbox_inches='tight')

# Muestra la figura
plt.show()
