# -*- coding: utf-8 -*-
"""reto_7_5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KCl_4_RnTJa8w3tdwlAScDeEjF_Vro6t
"""

numero_factorial = int(input("Ingrese un entero: "))
numero_n : int = 1
factorial : int = 1
while numero_n <= numero_factorial and numero_factorial>0:
  factorial = factorial*numero_n
  numero_n += 1
print("El factorial de " +str(numero_factorial)+ " es " +str(factorial))