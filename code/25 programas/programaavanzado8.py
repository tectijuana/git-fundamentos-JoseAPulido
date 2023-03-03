# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:40:43 2023
chuck a luck
@author: Flygo
"""

import random

# Definir la lista de posibles resultados de un lanzamiento
resultados = [1, 2, 3, 4, 5, 6]

# Solicitar al usuario que ingrese su apuesta y la cantidad de dinero a apostar
apuesta = int(input("Ingrese su apuesta (un número del 1 al 6): "))
dinero_apostado = int(input("Ingrese la cantidad de dinero a apostar: "))

# Lanzar los tres dados
dado1 = random.choice(resultados)
dado2 = random.choice(resultados)
dado3 = random.choice(resultados)

# Imprimir los resultados del lanzamiento
print("El primer dado muestra:", dado1)
print("El segundo dado muestra:", dado2)
print("El tercer dado muestra:", dado3)

# Calcular el resultado de la apuesta
if apuesta == dado1 or apuesta == dado2 or apuesta == dado3:
    resultado = dinero_apostado * 1
    print("Felicidades, ganaste", resultado, "dólares!")
else:
    resultado = dinero_apostado * -1
    print("Lo siento, perdiste", abs(resultado), "dólares.")
