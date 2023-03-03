# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 17:54:51 2023
Escribir un programa que acepte 25 enteros positivos como datos y describir cada uno como impar o par 
@author: Flygo
"""

# Inicializar una lista vacía para almacenar los enteros
enteros = []

# Aceptar 25 enteros positivos del usuario
for i in range(25):
    entero = int(input("Introduce un entero positivo: "))
    enteros.append(entero)

# Iterar sobre los enteros y describir cada uno como par o impar
for entero in enteros:
    if entero % 2 == 0:
        print("{} es par".format(entero))
    else:
        print("{} es impar".format(entero))
