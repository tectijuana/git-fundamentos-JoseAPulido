# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:44:12 2023
encontrar las raices cuadradas de los numeros del 9 al 25 imprimir el entero y la raiz cuadrada
@author: Flygo
"""
import math

# Iterar sobre los números del 9 al 25
for num in range(9, 26):
    # Calcular la raíz cuadrada del número
    raiz = math.sqrt(num)
    # Imprimir el número y su raíz cuadrada redondeada a 2 decimales
    print(num, round(raiz, 2))

