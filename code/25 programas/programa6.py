# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:13:28 2023
JOSE ANGEL VIRGEN PULIDO
convertir dolares en forma decimal al equivalente a pesos
@author: Flygo
"""

# Pedir al usuario que ingrese la cantidad de dólares
dolares = float(input("Ingresa la cantidad de dólares: "))

# Definir el tipo de cambio entre el dólar y el peso
tipo_de_cambio = 20.0  # Ejemplo: 1 dólar = 20 pesos

# Calcular la cantidad de pesos equivalente
pesos = dolares * tipo_de_cambio

# Imprimir el resultado
print("{} dólares equivalen a {} pesos".format(dolares, pesos))
