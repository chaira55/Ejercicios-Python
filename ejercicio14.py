def pedir_matrices(n, filas, columnas):
    matrices = []
    for m in range(n):
        print(f"\nIngrese los elementos de la matriz {m + 1}:")
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = int(input(f"Elemento ({i+1},{j+1}): "))
                fila.append(valor)
            matriz.append(fila)
        matrices.append(matriz)
    return matrices


def sumar_matrices(matrices, filas, columnas):
    matriz_resultante = [[0] * columnas for _ in range(filas)]
    for matriz in matrices:
        for i in range(filas):
            for j in range(columnas):
                matriz_resultante[i][j] += matriz[i][j]
    return matriz_resultante


def imprimir_matrices(matrices, resultado):
    print("\nResultado de la suma de matrices:")
    for i in range(len(matrices[0])):
        fila_str = "   ".join(str(matrices[m][i]) for m in range(len(matrices)))
        if i == len(matrices[0]) // 2:
            print(fila_str + " = " + str(resultado[i]))
        else:
            print(fila_str + "   " + str(resultado[i]))


def main():
    while True:
        n = int(input("Ingrese la cantidad de matrices a sumar (mínimo 2): "))
        if n >= 2:
            break
        print("Debe ingresar al menos dos matrices.")
    
    filas = int(input("Ingrese la cantidad de filas: "))
    columnas = int(input("Ingrese la cantidad de columnas: "))
    
    matrices = pedir_matrices(n, filas, columnas)
    resultado = sumar_matrices(matrices, filas, columnas)
    imprimir_matrices(matrices, resultado)


if __name__ == "__main__":
    main()
