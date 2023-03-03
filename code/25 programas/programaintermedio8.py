# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:10:33 2023
generar e imprimir 200 numeros aleatorios entre 1 y 12 determinar la frecuencia en que aparece cada numero
@author: Flygo
"""

import random

# Inicializar un diccionario para contar las ocurrencias de cada número
frequencies = {n: 0 for n in range(1, 13)}

# Generar 200 números aleatorios e incrementar la frecuencia de cada número
for i in range(200):
    num = random.randint(1, 12)
    frequencies[num] += 1

# Imprimir la frecuencia de cada número
for num, frequency in frequencies.items():
    print(num, "apareció", frequency, "veces")
