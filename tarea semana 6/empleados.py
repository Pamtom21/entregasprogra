class empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre= nombre
        self.edad= edad
        self.salario= salario
    def __str__(self):
        return f"{self.nombre}"
class gerente(empleado):
    def __init__(self, nombre, edad, salario, rol):
        super().__init__(nombre, edad, salario)
        self.rol= rol
    def describir_rol(self):
        print(f"hola me llamo {self.nombre}, soy gerente mi funcion es administrar a los trabajadores y sus distintas tareas asignadas")
    def trabajo(self, emple):
        print(f"{emple.nombre} ven a una reunion para evaluar tu desempeño")
class ingeniero(empleado):
    def __init__(self, nombre, edad, salario, rol):
        super().__init__(nombre, edad, salario)
        self.rol= rol
    def describir_rol(self):
        print(f"hola me llamo {self.nombre}, soy ingeniero mi funcion es desarrollar ideas y materializarlas en proyectos")
    def mantencion(self):
        print("Estoy haciendo matencion a las maquinas")
class asistente(empleado):
    def __init__(self, nombre, edad, salario, rol):
        super().__init__(nombre, edad, salario)
        self.rol=rol
    def describir_rol(self):
        print(f"hola me llamo {self.nombre}, soy asistente mi funcion es ayudar con lo que me designe el ingeniero o el gerente")
    def mandato():
        print("voy enseguida(duerme un rato en el baño)")
class sistema:
    def __init__(self):
        self.empleados= []
    def agregar_empleados(self, Empleado):
        self.empleados.append(Empleado)
    def mostrar_empleados(self):
        print("Estos son los empleados contratados")
        for j in range(len(self.empleados)):
            print(f"{j}. {self.empleados[j]}")
def interfaz():
    system=sistema()
    while True:
        print("Bienvenido a Empresa fantasma\n")
        print("1. Desea agregar empleados? ")
        print("2. Desea ver los empleados contratados?")
        print("3 Desea salir de este menu?\n")
        opcion= input("ingrese aqui su eleccion: ")
        if opcion=="3":
            break
        if opcion=="1":
            print("1. Gerente\n2. Ingeniero\n3. Asistente")
            subopcion= input("Ingrese su eleccion aqui: ")
            if subopcion== "1":
                nombre=input("Ingrese el nombre del empleado: ")
                edad= input("Ingrese la edad del empleado: ")
                salario=input("Ingrese el Salario del Empleado: ")
                employ= gerente(nombre, edad, salario, "Gerente")
                system.agregar_empleados(employ)
            if subopcion== "2":
                nombre=input("Ingrese el nombre del empleado: ")
                edad= input("Ingrese la edad del empleado: ")
                salario=input("Ingrese el Salario del Empleado: ")
                employ= ingeniero(nombre, edad, salario, "Ingeniero")
                system.agregar_empleados(employ)
            if subopcion== "3":
                nombre=input("Ingrese el nombre del empleado: ")
                edad= input("Ingrese la edad del empleado: ")
                salario=input("Ingrese el Salario del Empleado: ")
                employ= asistente(nombre, edad, salario, "Asistente")
                system.agregar_empleados(employ)
        if opcion=="2":
            system.mostrar_empleados()
            print("desea ver la descripcion del rol del empleado?\n")
            print("Si(1) o No(2)")
            subopcion=input("ingrese su eleccion aqui: ") 
            if subopcion=="1":
                print("Elija un empleado\n")
                system.mostrar_empleados()
                print("\n")
                x=int(input("ingrese el numero del empleado: " ))
                system.empleados[x].describir_rol()
            elif subopcion=="2":
                print("Muchas gracias por usar este sistema de empleados ")
            else:
                print("fatal error")
interfaz()
            