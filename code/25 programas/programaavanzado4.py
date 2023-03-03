# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:22:03 2023
calcular ingreso global por semana de una persona dada su tasa por hora, sueldo por hora de tiempo extra, numero de horas normales y extras 
@author: Flygo
"""
# Pedir al usuario que ingrese la tasa por hora, sueldo por hora de tiempo extra,
# número de horas normales y número de horas extras
tasa_por_hora = float(input("Ingrese la tasa por hora: "))
sueldo_por_hora_de_tiempo_extra = float(input("Ingrese el sueldo por hora de tiempo extra: "))
horas_normales = float(input("Ingrese el número de horas normales: "))
horas_extras = float(input("Ingrese el número de horas extras: "))

# Calcular el ingreso global
ingreso_global = (horas_normales * tasa_por_hora) + (horas_extras * sueldo_por_hora_de_tiempo_extra)

# Imprimir el resultado
print("El ingreso global por semana es:", ingreso_global)

