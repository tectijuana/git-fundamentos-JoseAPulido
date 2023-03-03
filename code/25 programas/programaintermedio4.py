# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:47:37 2023
simula los tiros de 6 monedas 1000 veces e imprime la distribucion
@author: Flygo
"""
import random

# Crear un diccionario para almacenar los resultados
resultados = {'Cara': 0, 'Cruz': 0}

# Realizar 1000 tiros de 6 monedas
for i in range(1000):
    # Tiro de 6 monedas
    caras = 0
    cruces = 0
    for j in range(6):
        if random.randint(0, 1) == 0:
            caras += 1
        else:
            cruces += 1
    # Registrar los resultados
    resultados['Cara'] += caras
    resultados['Cruz'] += cruces

# Imprimir los resultados
for resultado, cantidad in resultados.items():
    print(resultado + ': ' + str(cantidad))

