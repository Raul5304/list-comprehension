#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

nums = {1,2,2,3,4,5}
print(type(nums))
print(nums)

print()

ListaNums = list(nums)
print(type(ListaNums))
print(ListaNums)

print()

cosas = {11,22,23,"22",3.14,4}
print(type(cosas))
print(cosas)
print("Intento meter un valor repetido: 22")
cosas.add(22) # NO EXCEPTION: IGNORED
print(cosas)
print("Ni caso")

print()

ListaCosas = list(cosas)
print(type(ListaCosas))
print(ListaCosas)

print()
print(ListaCosas)
ListaCosas.append("22")
print("Añado el 22 a la lista")
print(ListaCosas)

print()

# LISTA -> SET
l = [x for x in "patata"]
print(l)
print(list(set(l)))

print()

comandos = {"new", "delete", "run", "delete"}
print(comandos)

print()

nums = { 21, 11, 42, 29, 22, 71, 18 }
print(nums)
lista = list(nums)
print(lista)
print("Ahora ordeno la lista")
lista.sort
print(lista)
print("Ahora convierto la lista en un set de nuevo, dejará de estar ordenado")
nums = set(lista)
print(nums)

print()

setA = {11,22,33,44}
setB = {33,44,55,66}

# union
print("Union:")
print(setA.union(setB))
print(setB.union(setA))
print(setA | setB)
print() # El orden no afecta a la unión

# intersección
print("Intersección:")
print(setA.intersection(setB))
print(setB.intersection(setA))
print(setA & setB)
print(setB & setA)
print() # El orden no afecta a la intersección

# diferencia A-B: 11,22
print("Diferencia")
print(setA.difference(setB))
print(setA- setB)
# diferencia B-A: 55,66
print(setB.difference(setA))
print(setB- setA)
print() # El orden si afecta a la diferencia

# diferencia simétrica A^B ~ B^A
print("Diferencia simétrica:")
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
print(setA ^ setB)
print(setB ^ setA)
print() # El orden no afecta en la diferencia simétrica

# subsets y supersets
set1 = { 'a', 'b', 'c', 'd', 'e' }
set2 = { 'a', 'b', 'c' }
set3 = {'x', 'y', 'z' }

print(set1)
print(set2)
print(set3)

if (set2.issubset(set1)):
    print("set2 es subset de set1")

if (set1.issuperset(set2)):
    print("set1 es superset de set2")

if (set2.isdisjoint(set3)):
    print("set2 y set3 no tienen elementos en común")

print()

# frozenset
colores = {"R","G","B"}
print(colores, type(colores))
colores.add("Y")
print(colores)

colores = frozenset(colores)
print(colores, type(colores))
# colores.add("Pistacho")
print(colores)
