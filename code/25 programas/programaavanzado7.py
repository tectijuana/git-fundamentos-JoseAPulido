# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:32:15 2023
calcule el interes total ganado, si se da el total invertido, la tasa de interes, el numero de años de la inversion y el numero de veces por año que se paga de interes
@author: Flygo
"""
# Solicitar al usuario que ingrese los datos de entrada
total_invertido = float(input("Ingrese el monto invertido: "))
tasa_interes = float(input("Ingrese la tasa de interés anual como decimal: "))
años_inversion = int(input("Ingrese la cantidad de años de inversión: "))
veces_por_año = int(input("Ingrese la cantidad de veces que se paga el interés por año: "))

# Calcular el interés total ganado
interes_total = total_invertido * ((1 + tasa_interes / veces_por_año) ** (años_inversion * veces_por_año) - 1)

# Imprimir el resultado
print("El interés total ganado es:", round(interes_total, 2))

