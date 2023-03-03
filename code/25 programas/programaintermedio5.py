# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:52:21 2023
una persona se encuentra en una habitacion con 29 personas cual es la probabilidad de que una de ellas tenga la misma fecha de cumpleaños
@author: Flygo
"""

p = 1.0
for i in range(1, 29):
    p = p * (365-i) / 365

probabilidad = 1 - p
print("La probabilidad de que al menos dos personas tengan la misma fecha de cumpleaños en una habitación con 29 personas es:", probabilidad)
