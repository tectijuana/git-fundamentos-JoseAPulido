# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:18:01 2023
encontrar la distancia que recorre la luz en x años
@author: Flygo
"""
# Pedir al usuario que ingrese el número de años
anios = int(input("Ingrese el número de años: "))

# Calcular el número de segundos en 'anios'
segundos = anios * 365 * 24 * 60 * 60

# Calcular la distancia que recorre la luz en 'segundos'
velocidad_luz = 299792458 # metros por segundo
distancia = velocidad_luz * segundos

# Imprimir el resultado
print("La luz recorre una distancia de", distancia, "metros en", anios, "años")

