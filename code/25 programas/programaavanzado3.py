# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:20:13 2023
celsius a fahrenheit 
@author: Flygo
"""

# Pedir al usuario que ingrese la temperatura en Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir la temperatura a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Imprimir el resultado
print(celsius, "grados Celsius equivalen a", fahrenheit, "grados Fahrenheit")
