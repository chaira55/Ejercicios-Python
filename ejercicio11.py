lista = [ "A", "B", "b", "c", "E", "E", "f"]

print(lista)

elemento = input("Ingrese el elemento de la lista que desea eliminar\n")
nuevaLista = []
for caracter in lista:
    if elemento.lower() != caracter.lower():
        nuevaLista.append(caracter)

lista = nuevaLista
print(lista)
