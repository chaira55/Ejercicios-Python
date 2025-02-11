print("CALCULADORA PARA CALCULAR DIAS VACACIONALES")

nombre = input("Nombre: ")
clave_departamento = int(input("Clave (1, 2 o 3): "))
antiguedad = int(input("Digite los años laborados: "))


class DiasVacacionales:

    #Constructor
    def __init__(self, nombre, clave_departamento, antiguedad):
        #Atributos de instancia
        self.nombre = nombre
        self.clave_departamento = clave_departamento
        self.antiguedad = antiguedad


    def vacaciones(self):
        #Departamento de Atenci´on al cliente (Clave 1)

        if self.clave_departamento == 1:
            if self.antiguedad <= 1:
               print(f"{self.nombre} tiene 6 dias de vacaciones")
            elif 2 <= self.antiguedad <= 6:
               print(f"{self.nombre} tiene 14 dias de vacaciones")
            elif self.antiguedad >=7:
               print(f"{self.nombre} tiene 20 dias de vacaciones")

        #Departamento de Log´ıstica (Clave 2)
        elif self.clave_departamento == 2:
            if self.antiguedad  <= 1:
               print(f"{self.nombre} tiene 7 dias de vacaciones")
            elif 2 <= self.antiguedad  <= 6:
               print(f"{self.nombre} tiene 15 dias de vacaciones")
            elif self.antiguedad  >=7:
               print(f"{self.nombre} tiene 21 dias de vacaciones")

        #Departamento de Gerencia (Clave 3)
        elif self.clave_departamento == 3:
            if self.antiguedad  <= 1:
               print(f"{self.nombre} tiene 10 dias de vacaciones")
            elif 2 <= self.antiguedad  <= 6:
               print(f"{self.nombre} tiene 20 dias de vacaciones")
            elif self.antiguedad  >=7:
               print(f"{self.nombre} tiene 30 dias de vacaciones")
        #Default
        else:
            raise ValueError("Error: La clave del departamento digitado no existe. Ingrese 1, 2 o 3.")

try:
   persona1 = DiasVacacionales(nombre, clave_departamento, antiguedad)
   persona1.vacaciones()
except ValueError as e:
   print(e)


