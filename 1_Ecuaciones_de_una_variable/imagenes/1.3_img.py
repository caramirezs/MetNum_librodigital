import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Crea una figura y cuatro objetos de ejes (axis) utilizando matplotlib.
# figsize se utiliza para establecer el tamaño de la figura.
sns.set_style('darkgrid') # Agrega el estilo "dark" de Seaborn
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 4.5))


# Grafica en el primer objeto de ejes (axis)
f = lambda x: np.cbrt(x - np.sqrt(2))
df = lambda x: 1/(3*np.cbrt(x - np.sqrt(2))**2)
p_0 = 1.5
tolerancia = 1e-3
max_ite = 5
x_i, x_f = -2, 3
x = np.linspace(x_i, x_f, 1000)
axs[0].plot(x, f(x), label='f(x)')
axs[0].scatter(p_0, f(p_0), color='blue', alpha=0.8, marker='*', zorder=3)
axs[0].scatter(p_0, 0, color='red', alpha=1, marker='x', zorder=2)
axs[0].plot([p_0, p_0], [0, f(p_0)], '--', color='orange', alpha=0.5, zorder=2)
axs[0].text(p_0, 0, f"p0", fontsize=14, ha='center', va='top')

# Iterar hasta que la tolerancia sea alcanzada o se supere el número máximo de iteraciones
ite= 1
while ite <= max_ite:
    if df(p_0) == 0 or f(p_0) == 0:
        break
    p_i = p_0 - f(p_0)/df(p_0)  # Newton-Rapshon (recta tangente)

    # Graficar la línea vertical en p_i y el punto en la grafica
    axs[0].scatter(p_i, f(p_i), color='blue', alpha=0.8, marker='*', zorder=3)
    axs[0].scatter(p_i, 0, color='red', alpha=0.8, marker='x', zorder=2)
    if ite <= 10:
        axs[0].text(p_i, 0, f"p{ite}", fontsize=14, ha='center', va='top')
        axs[0].plot([p_0, p_i, p_i], [f(p_0), 0, f(p_i)], '--', color='orange', alpha=0.5, zorder=2)

    if abs(p_i-p_0) < tolerancia:
        break
    p_0 = p_i
    ite += 1

axs[0].scatter(p_i, 0, color='red', alpha=0.8, marker='x', label='raíz aproximada')
axs[0].plot([p_0, p_i], [f(p_0), 0], '--', color='orange', alpha=0.5, label='recta tangente', zorder=2)
axs[0].set_title('Gráfica 1', fontsize=16)

xmin, xmax = axs[0].get_xlim()
ymin, ymax = axs[0].get_ylim()
axs[0].tick_params(labelsize=12, axis='x')
axs[0].tick_params(labelsize=12, axis='y')
axs[0].annotate("", xy=(xmax, 0), xytext=(xmin, 0), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10), zorder=2)
axs[0].annotate("", xy=(0, ymax), xytext=(0, ymin), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10), zorder=2)


# Grafica en el segundo objeto de ejes (axis)
f = lambda x: (x - np.sqrt(2))**2 + 0.5
df = lambda x: 2*(x - np.sqrt(2))
p_0 = 1.64
tolerancia = 1e-3
max_ite = 5
x_i, x_f = 0, 2.5
x = np.linspace(x_i, x_f, 1000)

axs[1].plot(x, f(x), label='f(x)')
axs[1].scatter(p_0, f(p_0), color='blue', alpha=0.8, marker='*', zorder=3)
axs[1].scatter(p_0, 0, color='red', alpha=1, marker='x', zorder=2)
axs[1].plot([p_0, p_0], [0, f(p_0)], '--', color='orange', alpha=0.5, zorder=2)
axs[1].text(p_0, 0, f"p0", fontsize=14, ha='center', va='top')

ite= 1
while ite <= max_ite:
    if df(p_0) == 0 or f(p_0) == 0:
        break
    p_i = p_0 - f(p_0)/df(p_0)  # Newton-Rapshon (recta tangente)

    # Graficar la línea vertical en p_i y el punto en la grafica
    axs[1].scatter(p_i, f(p_i), color='blue', alpha=0.8, marker='*', zorder=3)
    axs[1].scatter(p_i, 0, color='red', alpha=0.8, marker='x', zorder=2)
    # texto
    if ite <= 10:
        axs[1].text(p_i, 0, f"p{ite}", fontsize=14, ha='center', va='top')
        axs[1].plot([p_0, p_i, p_i], [f(p_0), 0, f(p_i)], '--', color='orange', alpha=0.5, zorder=2)

    if abs(p_i-p_0) < tolerancia:
        break
    p_0 = p_i
    ite += 1

axs[1].scatter(p_i, 0, color='red', alpha=0.8, marker='x', label='raíz aproximada')
axs[1].plot([p_0, p_i], [f(p_0), 0], '--', color='orange', alpha=0.5, label='recta tangente', zorder=2)
axs[1].set_title('Gráfica 2', fontsize=16)

xmin, xmax = axs[1].get_xlim()
ymin, ymax = axs[1].get_ylim()
axs[1].tick_params(labelsize=12, axis='x')
axs[1].tick_params(labelsize=12, axis='y')
axs[1].annotate("", xy=(xmax, 0), xytext=(xmin, 0), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10), zorder=2)
axs[1].annotate("", xy=(0, ymax), xytext=(0, ymin), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10), zorder=2)

# Configura las etiquetas de los ejes
for ax in axs.flat:
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)

# Ajusta automáticamente los espacios entre los subplots
fig.tight_layout()
plt.savefig('nosol_met_NR.png', dpi=400, bbox_inches='tight')

# Muestra la figura
plt.show()
