#ARRAYS y sus .py
#0 1 2 3 4..5...

"""
primero se indica el indice entre corchetes y 
luego se le asigna logicamente
"""
print("--lista no modificada--")
numeros=[10,20,30]
print(numeros)

numeros[0]=1
numeros[1]=2
numeros[2]=3

print("---lista modificada---")

print(numeros)

#append: lo pone al final de la lista
numeros.append(99)
print("-APPEND final de la lista:",numeros)

#count: numero de veces que hay un elemento en la lista
print("-COUNT la cantidad de 2 son:",numeros.count(2))


#index: devuelve la pocision que estamos buscando
print("-INDEX la pocision del 3 esta en:",numeros.index(3))

#insert: inserta un numero con una variable

edad=[14]
numeros.insert(4,edad)
print("-INSERT el numero insertado es 14:",numeros)

#pop: devuelve el ultimo elemento

#print("-POP Solo devuelve el ultimo elemento:",numeros.pop())

#remove: por logica borra.

#print(numeros.remove(99))

#reverse: como su nombre lo dice lo hace en la lista

edad.append(18)
edad.reverse()
print("-REVERSE alrevez:",edad)

#sort ordena los numeros de menor a mayor 
lista_nueva=[5,4,8,3,7,7,7]
lista_nueva.sort()
print(lista_nueva)
