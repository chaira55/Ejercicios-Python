mensaje = "Bienvenido a la clase python"
mensaje_prueba1 = "Bienvenidos a la clase python"
mensaje_prueba2 = "Bienvenido a la clase python"

buscar = mensaje.find("python")
extraer = mensaje[11:22]

buscar = str(buscar)
extraer = str(extraer)

print("Buscar posicion Ernesto: " + buscar)
print("Extraer palabra: " + extraer)
print(mensaje_prueba1 == mensaje_prueba2)
print(mensaje == mensaje_prueba2)



nombre = (input("Introduce tu nombre : "))
edad = int(input("Introduce tu edad: "))

print("Tu nombre es " + nombre + " y tienes", edad, "años de edad")   
print("Tu nombre es " + nombre + " y tienes " +  str(edad) +  " años de edad")
print(f"Tu nombre es {nombre} y tienes {edad} años de edad")  #f-strings: Literales de cadena formateados