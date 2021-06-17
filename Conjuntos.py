"""
Conjuntos: Es una coleccion que no tiene un orden 

Cardinalidad: Es el numero de elementos que contiene un conjunto 
|A| = 5

Conjunto vacio: Es aquel conjunto que carece de elementos

V = {}

Operaciones: UNION, INTERSECCION DIFERENCIA, COMPLEMENTO

"""
import os

#CREANDO UN CONJUNTO o SET EN PYTHON
vocales = {
    'a',
    'e',
    'i',
    'o',
    'u',
    'a',
    'e',
}

#IMPRIMIENDO EL CONJUNTO 
print (vocales)
print('Tipo de dato: ',type(vocales))

#Los imprime en diferente orden, a pesar de que tenga mas datos iguales
print('Cardinalidad de Vocales: ',len(vocales)) 
vocales.remove('i')
print (vocales)
vocales.add('i')
print (vocales)

#No podemos accceder a los elementos del conjunto mediante indexacion porque no es un diccionario o indice
paises = {
    'Mexico','Chile','Peru','Paraguay','Argentina',
}
print('Mis paises: ',end='')

#Recorriendo el set en un loop
for pais in paises:
    print(pais,end=" ")
print()

#Añadir un elemento al conjunto o set
paises.add('Colombia')
for pais in paises:
    print(pais,end=" ")
print()

#Eliminando  un elemento del conjunto o set
paises.remove('Argentina')
print(paises)

#Vaciar un conjunto o eliminar todos los elementos 
#Metodo clear
paises.clear()
print(paises)

#Para eliminar toda la estructura 
del paises

#Definiendo el conjunto vacio
vacio = set()
print(vacio)

#******* Operaciones con Conjuntos *******

A = {1,2,3}
B = {4,5,6}

#Union | Conmutativa
AUB = A | B
print(AUB)

#Intereseccion & Conmutativa
C = {1,2,3,4,5}
D = {4,5,6,7,8}
I = C&D
print(I)

#Diferencia - No Conmutativa
E = {1,2,3,4}
F = {2,3}

dif_e_y_f = E - F 
print(dif_e_y_f)

#Conjuntos iguales
os.system('cls')

G = {'a','b','c'}
H = {'c','b','a'}
print(G,H)
if G==H:
    print('Iguales')
else:
    print('Diferentes')

#Subconjuntos issubSet
M= {1,2,3,4}
N = {2,3,100}

print(f"{N} es subconjunto de {M}") if N.issubset(M) else print(f"{N} NO es subconjunto de {M}")

