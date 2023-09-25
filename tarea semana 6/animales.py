class animal:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    def sonido(self):
        print(f"soy {self.nombre} y hago: ")
    def __str__(self):
        return f"{self.nombre}"
class perro(animal):
    def sonido(self):
        super().sonido()
        print("guau guau")
class gato(animal):
    def sonido(self):
        super().sonido()
        print("miau miau")
class pajaro(animal): 
    def sonido(self):
        super().sonido()
        print ("tiu tiu")
class sistema:
    def __init__(self):
        self.animales=[]
    def agregar_animales(self, animal):
        self.animales.append(animal)
        print("se agrego exitosamente")
    def mostrar_animales(self):
        print("Estos son los animales disponibles ")
        for j in range(len(self.animales)):
            print(f"{j}. {self.animales[j]}")
def interfaz():
    system=sistema()
    while True:
        print("Bienvenido al refugio de animales\n")
        print("1. Desea agregar animales\n2. Desea ver los animales en el refugio\n3. Desea salir")
        print("\n")
        opcion= input("Ingrese su eleccion aqui: ")
        if opcion=="3":
            break
        elif opcion=="1":
            print("elija que tipo de animal es:\n1. Perro\n2. Gato\n3. Pajaro")
            subopcion= input("Ingrese su opcion aqui: ")
            if subopcion=="1":
                nombre=input("Ingrese la raza del perro: ")
                edad=input("Ingrese la edad del perro: ")
                ani=perro(nombre,edad)
                system.agregar_animales(ani)
            elif subopcion=="2":
                nombre=input("Ingrese la raza del gato: ")
                edad=input("Ingrese la edad del gato: ")
                ani=gato(nombre,edad)
                system.agregar_animales(ani)
            elif subopcion=="3":
                nombre=input("Ingrese el nombre del pajaro: ")
                edad=input("Ingrese la edad del pajaro: ")
                ani=pajaro(nombre,edad)
                system.agregar_animales(ani)
            else:
                print("fatal error")
        elif opcion=="2":
            system.mostrar_animales()
            print("Desea saber que sonido hace el animal\n1. Si\n2.No ")
            subopcion=input("Ingrese su eleccion aqui: ")
            if subopcion=="1":
                print("elija el animal que desea saber su sonido: ")
                system.mostrar_animales()
                x=int(input("Ingrese su eleccion aqui: "))
                system.animales[x].sonido()
            elif subopcion=="2":
                print("Gracias por usar sistema de animales")
            else:
                print("fatal error")
        else:
            print("fatal error")
interfaz()
                
                                
        