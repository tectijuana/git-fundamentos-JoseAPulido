# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:20:12 2023
convertir libras y onzas a kilogramos
@author: Flygo
"""
# Pedir al usuario que ingrese la cantidad de libras y onzas
libras = float(input("Ingresa la cantidad de libras: "))
onzas = float(input("Ingresa la cantidad de onzas: "))

# Convertir las libras a kilogramos
kg_libras = libras / 2.2046

# Convertir las onzas a kilogramos
kg_onzas = onzas / 35.274

# Sumar las cantidades en kilogramos
kg_total = kg_libras + kg_onzas

# Imprimir el resultado
print("{:.2f} libras y {:.2f} onzas equivalen a {:.2f} kilogramos".format(libras, onzas, kg_total))

