num = int(input("Indique la longitud de la lista = "))
lista = []

#llenar lista
for i in range(num):
    a = int(input(f"Ingrese el {i+1} de la lista = "))
    lista.append(a)

#imprimir lista
print(lista)

#suma del array
print(f"Suma de la lista de enteros = {sum(lista)}")
