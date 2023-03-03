# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:02:27 2023
de dos numeros cualesquiera, encontrar la suma e indicar si es positiva, negativa o cero
@author: Flygo
"""

# Solicitar al usuario que ingrese dos números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Calcular la suma
suma = numero1 + numero2

# Determinar si la suma es positiva, negativa o cero
if suma > 0:
    print("La suma es positiva.")
elif suma < 0:
    print("La suma es negativa.")
else:
    print("La suma es cero.")
