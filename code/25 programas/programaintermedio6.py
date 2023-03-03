# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:57:51 2023
convertir numeros de base 10 a octal en python 
@author: Flygo
"""
num_decimal = int(input("Ingrese un número decimal: "))
num_octal = "%o" % num_decimal
print("El número", num_decimal, "en octal es", num_octal)
