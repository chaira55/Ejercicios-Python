a = int(input("Ingrese el tamaño de las filas = "))
b = int(input("Ingrese el tamaño de las columnas = "))

matriz = []

for i in range(a):
    matriz.append([])
    for j in range(b):
        elemento = int(input("Ingrese un numero = "))
        matriz[i].append(elemento)

for row in matriz:
    for elemento in row:
        print(elemento, end=" ")
    print()