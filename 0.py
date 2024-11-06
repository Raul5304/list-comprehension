#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from math import pi

# sets from lists

# l = [11,22,33,22]
# print(l, type(l))

# s = set(l)
# print(s, type(s))

# sets from list comprehension:

r0 = range(16+1)        # {x : x in {0 ... 16}}
print(r0, type(r0))

l0 = []
for item in r0:
    l0.append(item)
    
# {x : x in {0 ... 16}}
print(l0, type(l0))

L0 = [x for x in range(17)]
print(L0, type(L0))

# S = {x² : x in {0 ... 16}}
L1 = [x*x for x in range(17)] # Cálculo del cuadro de los números en una lista
print(L1, type(L1))

ListaEntrada = [x for x in range(17)]
ListaPares = [x for x in ListaEntrada if x%2==0] # Cálculo para listas pares
print(ListaPares, type(ListaPares))

ListaImpares = [x for x in ListaEntrada if x%2!=0] # Cálculo para listas impares
print(ListaImpares, type(ListaImpares))

# Cálculo de temperaturas celsius a fahrenheit

# Temperatura en celsius
rangoClimasC = range(19, 30) 
ClimasC = [c for c in range(19, 30)]
print(ClimasC, type(ClimasC))

ClimasF = [c * 9/5 + 32 for c in rangoClimasC]
print(ClimasF, type(ClimasF))

# filtrar aritméticamente valores positivos
a = [-4, 2, 0, -1, 12, -3]

b = [e for e in a if e > 0]
print(b)

# filtrar por tipos de datos
input = ['a', 2, 'patata', 12, 3, 'd', "3.4", 3.14, pi]
notStrT = [x for x in input if type(x) == int]
StrT = [x for x in input if type(x) == str]

print(notStrT, type(notStrT))
print(StrT, type(StrT))

# Filtrar vocales en una frase
def hay_vocales(c):

    vocales = 'aeiouAEIUOU'

    if c in vocales:
        return True
    else:
        return False


frase = 'Hay aguilas en el cielo.'

vocales = [c for c in frase if hay_vocales(c)]
print(vocales, type(vocales))