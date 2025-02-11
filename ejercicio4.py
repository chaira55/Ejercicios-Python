#La calculadora debera ser capaz de calcular las operaciones de suma,
#resta, multiplicacion, division, division entera, exponente y modulo o
#resto.

import math

while True:
    print("CALCULADORA")
    print("Elija la operacion que desea realizar: ")
    menu = int(input("1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n5. Division entera \n6. Exponente \n7. Modulo \n0.Salir\n"))

    if menu == 0:
        print("Saliendo de la calculadora...")
        break

    num1 = float(input("Introduzca el primer numero: "))
    num2 = float(input("Introduzca el segundo numero: "))


    def suma():
        return num1 + num2

    def resta():
        return num1 - num2

    def multiplicacion():
        return num1 * num2

    def division():
        return num1 / num2 if num2 != 0 else "Error: División por cero"

    def divisionEntera():
        return num1 // num2 if num2 != 0 else "Error!! División por cero"

    def exponente():
        return pow(num1, num2) 

    def modulo():
        return num1 % num2 if num2 != 0 else "Error: División por cero"



    dict = {
        1 : suma,
        2 : resta,
        3 : multiplicacion,
        4 : division,
        5 : divisionEntera,
        6 : exponente,
        7 : modulo
    }        
    resultado = dict.get(menu, lambda: "Opcion incorrecta")()
    print(f"Resultado: {resultado}")


