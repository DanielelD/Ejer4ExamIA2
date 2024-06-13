# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:56:11 2024

@author: ddiaz
"""

import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    return x**2 + 10 * np.sin(x)

def recocido_simulado(funcion, x0, temp_i, tasa_en, i):
    x_actual = x0
    mejor_x = x0
    mejor_v = funcion(x0)
    
    hist = [(x_actual, mejor_v)]
    
    temp = temp_i

    for i in range(i):
        x_nuevo = x_actual + np.random.uniform(-1, 1)
        nuevo_valor = funcion(x_nuevo)
        
        delta_e = nuevo_valor - funcion(x_actual)
        
        if delta_e < 0 or np.random.rand() < np.exp(-delta_e / temp):
            x_actual = x_nuevo
            if nuevo_valor < mejor_v:
                mejor_x = x_nuevo
                mejor_valor = nuevo_valor
        
        temp *= tasa_en
        
        hist.append((mejor_x, mejor_valor))

    return mejor_x, mejor_valor, historial

x0 = 0  
temp_i = 10
tasa_en = 0.99
i = 100

mejor_x, mejor_valor, historial = recocido_simulado(fun, x0, temp_i, tasa_en, i)

print(f"Mejor solución encontrada: x = {mejor_x}, f(x) = {mejor_valor}")

x = np.linspace(-10, 10, 400)
y = fun(x)
plt.plot(x, y, label="Función objetivo")
hist_x, hist_y = zip(*historial)
plt.scatter(hist_x, hist_y, c='r', marker='x', label="Historial de búsqueda")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
