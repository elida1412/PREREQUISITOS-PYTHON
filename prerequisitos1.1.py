
## Bienvenidos a prerequisitos con Python - Parte1

import numpy as np
import matplotlib.pyplot as plt
#ALgebra lineal
#ejemplo con vectores

a = np.array([1, 2])
b = np.array([-4, 4])
c = a + b

# graficamos
# creamos referencia de eje
ax = plt.axes()
# graficamos un punto (o) en (0,0) como verde (g)
ax.plot(0,0, 'og')
# graficamos el vector a como azul empezando en (0,0)
ax.arrow(0,0, *a, color='b', linewidth=0.2, head_width=0.4, head_length=0.5)
# graficamos el otro vector b como cyan
ax.arrow(a[0],a[1], *b, color='c', linestyle='dotted', linewidth=0.2, head_width=0.4, head_length=0.5)
# graficamos la resultante
ax.arrow(0,0, *c, color='k', linewidth=0.2, head_width=0.4, head_length=0.5)
# limites para el eje x
plt.xlim(-4,2)
# limites para el eje y
plt.ylim(-1,7)
# ticks para el eje y
yticks = np.arange(-1,7)
ax.set_yticks(yticks)
# crea un enrejado
plt.grid(b=True, which='major')
#display the plot
plt.show()
