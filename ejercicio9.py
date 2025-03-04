frase = input("Ingrese una frase:\n")
caracter = input("Ingrese un carácter específico:\n")

vocales = "aeiouAEIOU"
nueva_frase = ""

for letra in frase:
    if letra == caracter:
        break
    if letra not in vocales:
        nueva_frase += letra

print("Frase sin vocales hasta encontrar el carácter específico:")
print(nueva_frase)