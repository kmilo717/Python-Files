colors = ['yellow', 'blue', 'red', 'black', 'white', 'orange', 'purple', 'green']
otherColors = ['grey', 'brown']
print('Original list')
print(colors)

#1. Lists

#Methods
#Agrega un elemento al final de la lista
colors.append('pink')
print('-----------------------------------------------------------------------------')
print('.append')
print(colors)

#Extiende una lista agregándole los elementos de un iterable (list, set, dictionary, tuple)
colors.extend(otherColors)
print('-----------------------------------------------------------------------------')
print('.extend')
print(colors)

#Agrega un elemento indicando la posición donde se desea colocar. El primer argumento es el indicador de la posición teniendo en cuenta que el primer elemento tiene el índice [0]. El segundo argumento es el elemento a agregar
colors.insert(2, 'aquamarine')
print('-----------------------------------------------------------------------------')
print('.insert')
print(colors)

#Elimina un elemento indicandolo. Si hay más de un índice con el mismo valor (elemento) se eliminará el primer elemento
colors.remove('brown')
print('-----------------------------------------------------------------------------')
print('.remove')
print(colors)

#Elimina un elemento indicando su índice, además lo retorna. Cuando no se determina el índice del elemento a eliminar, se eliminará el último elemento
deletedItem = colors.pop(2)
print('-----------------------------------------------------------------------------')
print('.pop')
print(deletedItem)
print(colors)

#Retorna el índice del elemento que se indique. Hay dos argumentos adicionales pero opcionales donde se determinan índices con los cuáles se puede indicar un rango de búsqueda para el elemento indicando. Si hay más de un índice con el mismo elemento, se retornará el índice del primero que se encuentre. Para poder visualizar el índice, se debe crear una variable que sea igual a la sintaxis de este método
ind = colors.index('black')
print('-----------------------------------------------------------------------------')
print('.index')
print('Element "black" in position', ind)

#Cuenta y retorna las veces que un elemento aparezca en la lista. Para poder visualizar esta cuenta se debe crear una variable que sea igual a la sintaxis de este método
cont = colors.count('violet')
print('-----------------------------------------------------------------------------')
print('.count')
print('Element "violet" appears', cont, 'times')

#Ordena los elementos de la lista en orden inverso al determinado
colors.reverse()
print('-----------------------------------------------------------------------------')
print('.reverse')
print(colors)

#Ordena los elementos de la lista en orden alfabético, también usando "reverse=False" se le da orden alfabético descendente. Así mismo, se le puede dar distintos parámetros y argumentos para dar el orden que el usuario desee
colors.sort()
print('-----------------------------------------------------------------------------')
print('.sort')
print(colors)

#Realiza una copia de una lista
colorsCopy = colors.copy()
print('-----------------------------------------------------------------------------')
print('.copy')
print('Copied list:', colorsCopy)

#Elimina todos los elementos guardados en la lista
colorsCopy.clear()
print('-----------------------------------------------------------------------------')
print('.clear')
print('List without elements', colorsCopy)

#Lista como una pila
#El último elemento que sea agregado será el primero en retirarse, utilizando append para agregar y pop (sin un índice) para eliminar el último elemento agregado.
print('-----------------------------------------------------------------------------')
print('Lista como una pila')
colors.append("cian")
print('Agregando un elemento')
print(colors)
colors.pop()
print('Eliminando el último elemento agregado.')
print(colors)

#Lista como una cola
#El primer elemento agregado será el primero en retirarse. Para esto se importa la librería "deque" que servirá para agregar o eliminar elementos rápida y eficazmente de la lista.
from collections import deque
colorsCopy=deque(colors)
print('-----------------------------------------------------------------------------')
print('Lista como una cola')
colorsCopy.append("cian")
print('Agregando un elemento')
print(colorsCopy)
colorsCopy.popleft()
print('Eliminando el primer elemento agregado.')
print(colorsCopy)

#2 Delete (del)
#Con esta instrucción se puede eliminar uno o varios elementos de una lista indicando un rango de elementos a eliminar, cabe aclarar que en los rangos, el valor final es excluyente, por lo que no se eliminará el elemento del índice final. Si se indica solo el índice de inicial, se eliminarán los elementos desde el del índice estipulado hasta el final; si se indica solo el índice final, se eliminarán los elementos desde el inicial hasta el anterior al índice estipulado teniendo en cuenta que es excluyente. Tambien es posible vaciar la lista totalmente como lo hace el método clear, u otra posibilidad es eliminar la variable que contiene la lista, es decir, eliminar la lista del todo.
colorsCopy = colors.copy()
print('-----------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------')
print('Original list colorsCopy')
print(colorsCopy)

del colorsCopy[3]
print('-----------------------------------------------------------------------------')
print('Delete item by index')
print(colorsCopy)

del colorsCopy[3:5]
print('-----------------------------------------------------------------------------')
print('Delete items by range')
print(colorsCopy)

del colorsCopy[:]
print('-----------------------------------------------------------------------------')
print('Delete complete list')
print('List without elements', colorsCopy)

del colorsCopy
print('-----------------------------------------------------------------------------')
print('Delete variable')


#3 Tuplas y secuencias
#La tupla es un dato de tipo secuencia, esta consta de cierto número de valores separados por comas.
months = 'January', 'February', 'March', 'April'
firstSixMonths = months, ('May', 'June')
print('-----------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------')
print('Tupla months:')
print(months)
print('-----------------------------------------------------------------------------')
print('La tupla se puede anidar')
print(firstSixMonths)


#4 Conjuntos
#Es una colección no ordenada y que no contiene un mismo elemento más de una vez, es decir, no repite elementos. Como usos principales está el verificar la pertenencia y eliminar entradas duplicadas. Los conjuntos soportan operaciones como la unión, intersección, diferencia y diferencia simétrica.