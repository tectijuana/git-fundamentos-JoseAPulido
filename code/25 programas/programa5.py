# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:10:59 2023
#JOSE ANGEL VIRGEN PULIDO
introducir n enteros calcular e imprimir el producto de los numeros pares en python
@author: Flygo
"""

# Pedir al usuario que ingrese una lista de números
n = int(input("¿Cuántos números deseas ingresar? "))
numeros = []
for i in range(n):
    numero = int(input("Ingresa el número {}: ".format(i+1)))
    numeros.append(numero)

# Calcular el producto de los números pares
producto = 1
for numero in numeros:
    if numero % 2 == 0:
        producto *= numero

# Imprimir el resultado
print("El producto de los números pares es: {}".format(producto))
