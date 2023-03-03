# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:11:17 2023
convertir un angulo, minutos y segundos a grados en fraccion decimal 
@author: Flygo
"""
# Pedir al usuario que ingrese los grados, minutos y segundos del ángulo
grados = float(input("Ingrese los grados: "))
minutos = float(input("Ingrese los minutos: "))
segundos = float(input("Ingrese los segundos: "))

# Convertir el ángulo a una fracción decimal
angulo_decimal = grados + (minutos / 60) + (segundos / 3600)

# Imprimir el resultado
print("El ángulo es:", angulo_decimal, "grados")

