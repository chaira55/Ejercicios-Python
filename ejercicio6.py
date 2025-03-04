cadena = input("Introduzca la cadena de caracteres: ")

print("Su cadena de caracteres es: [ " + cadena + " ]" )

palabraEliminar = input("¿Que palabra desea eliminar?: ")

print("Palabra a eliminar es: [ " + palabraEliminar + " ]")

nuevaCadena = cadena.replace(palabraEliminar, "")

print("Nueva cadenad de caracteres: [ " + nuevaCadena + " ]")
