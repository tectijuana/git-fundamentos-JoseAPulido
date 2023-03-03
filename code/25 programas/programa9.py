# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:25:39 2023

@author: Flygo
"""

# Crear una lista de 20 enteros
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Crear una nueva lista con los primeros 10 elementos intercambiados con los últimos 10 elementos
nueva_lista = lista[10:] + lista[:10]

# Imprimir la nueva lista
print(nueva_lista)
