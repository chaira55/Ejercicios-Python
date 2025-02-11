numero = []

for i in range(3):
    num = int(input("Digite un numero: "))
    numero.append(num)


mayor = 0

for num in numero:
    if num > mayor:
        mayor = num

print(f"El numero {mayor} es el mas grande de los tres")
