# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:45:39 2023
simular la caida de una moneda
@author: Flygo
"""
import random

# Generar un número aleatorio entre 0 y 1
num = random.randint(0, 1)

# Imprimir el resultado
if num == 0:
    print("Cara")
else:
    print("Cruz")

