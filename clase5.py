#Listas -> Colecciones de datos ordenados y mutables, que pueden contener elementos de diferentes tipos.
#Mutables -> Se pueden modificar después de su creación (agregar, eliminar, cambiar elementos).
lista_numeros: list[int] = [1, 2, 3, 4, 5]
print(lista_numeros)  # Salida: [1, 2, 3, 4, 5]
lista_mixta: list = [1, "Hola", 3.14, True]
print(lista_mixta)  # Salida: [1, 'Hola', 3.14, True]
lista_strings: list[str] = ["Python", "Java", "C++"]
print(lista_strings)  # Salida: ['Python', 'Java', 'C++']

#operaciones
lista_numeros.append(6)  # Agrega el número 6 al final de la lista
print(lista_numeros)  # Salida: [1, 2, 3
lista_numeros.remove(2)  # Elimina el número 2 de la lista
print(lista_numeros)  # Salida: [1, 3, 4, 5, 6]
lista_numeros[0] = 10  # Cambia el primer elemento de la lista a 10
print(lista_numeros)  # Salida: [10, 3, 4, 5, 6]
lista_numeros.reverse()  # Invierte el orden de la lista
print(lista_numeros)  # Salida: [6, 5, 4, 3, 10]
lista_numeros.sort()  # Ordena la lista de menor a mayor
print(lista_numeros)  # Salida: [3, 4, 5, 6, 10]
lista_numeros.sort(reverse=True)  # Ordena la lista de mayor a menor
print(lista_numeros)  # Salida: [10, 6, 5, 4, 3]
#insertar al final
#len(objeto) -> Devuelve la cantidad de elementos en la lista
lista_numeros.insert(len(lista_numeros), 7)  # Inserta el número 7 al final de la lista
#pop
lista_numeros.pop()  # Elimina el último elemento de la lista (7)
lista_numeros.pop(0)  # Elimina el primer elemento de la lista (10)

lista_numeros = [6, 5, 4, 3] + [2, 1]  # Concatenación de listas

#Repetición
lista_ejemplo = [1,2] * 3 # Repite la lista [1, 2] tres veces
print(lista_ejemplo)  

for numero in lista_numeros:
    print(numero)  # Imprime cada número en la lista_numeros

#Busqueda, if uno existe en lista_numeros
if 1 in lista_numeros:
    print("El número 1 está en la lista_numeros")
else:    
    print("El número 1 no está en la lista_numeros")

numeros = [x for x in range(100)] #valores del 0 al 99

cuadrados = [x**2 for x in numeros] #cuadrados de los numeros del 0 al 99
print(cuadrados)  # Imprime la lista de cuadrados de los números del 0 al 99

lista_pares = [x for x in numeros if x % 2 == 0] #números pares del 0 al 99
print(lista_pares)  # Imprime la lista de números pares del 0 al 99

lista_impares = [x for x in numeros if x % 2 != 0] #números impares del 0 al 99
print(lista_impares)  # Imprime la lista de números impares del 0 al 99

def llenar_lista():
    iteraciones = int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))
    lista = []
    for i in range(iteraciones):
        elemento = input(f"Ingrese el elemento {i + 1}: ")
        if elemento.isdigit():  # Verifica si el elemento es un número
            elemento = int(elemento)  # Convierte el elemento a entero
            if elemento % 2 == 0:  # Verifica si el número es par
                print(f"El número {elemento} es par.")
                lista.append(elemento)
    return lista

lista = llenar_lista()
print("Lista de números pares ingresados:", lista)