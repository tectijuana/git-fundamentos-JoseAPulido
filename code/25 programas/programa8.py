# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:24:02 2023
invertir un numero es escribirlo hacia atras
@author: Flygo
"""

# Pedir al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Convertir el número a una cadena de texto e invertirla
numero_invertido = int(str(numero)[::-1])

# Imprimir el resultado
print("El número {} invertido es {}".format(numero, numero_invertido))
