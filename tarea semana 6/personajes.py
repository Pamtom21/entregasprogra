class personaje:
    def __init__(self,Nombre,Vida, p_ataque, clase):
        self.nombre=Nombre
        self.vida=Vida
        self.p_ataque=p_ataque
        self.clase=clase
    def __str__(self):
        return f"{self.nombre}"
    def ataque(self):
        print(f"has hecho {self.p_ataque} puntos de daño")
    def recibir_dano(self):
        print("te han atacado")
        self.vida-=10
        print(f"tu nueva vida es {self.vida}")
class soldado(personaje):
    def __init__(self, Nombre, Vida, p_ataque, clase):
        super().__init__(Nombre, Vida, p_ataque, clase)
    def ataque(self):
        print("atacas de modo fisico")
        super().ataque()
class mago(personaje):
    def __init__(self, Nombre, Vida, p_ataque, clase):
        super().__init__(Nombre, Vida, p_ataque, clase)
    def ataque(self):
        print("atacas a larga de distancia por medio de magia negra")
        super().ataque()
class arquero(personaje):
    def __init__(self, Nombre, Vida, p_ataque, clase):
        super().__init__(Nombre, Vida, p_ataque, clase)
    def ataque(self):
        print("tu ataque es por medio de flechas")
        super().ataque()
class sistema:
    def __init__(self):
        self.personajes=[]
    def agregar_personajes(self, personaje):
        self.personajes.append(personaje)
    def mostrar_personajes(self):
        print("los personajes disponibles son:")
        for k in range(len(self.personajes)):
            print(f"{self.personajes[k]}")
    def eliminar_personaje(self):
        for k in range(len(self.personajes)):
            if self.personajes[k].vida <= 0:
                print(f"{self.personajes[k]} ha muerto")
                self.personajes.remove(self.personajes[k])
def interfaz():
    system=sistema()
    while True:
        print("Hola gamers")
        print("1. Desea crear un personaje?\n2.Desea ver los personajes disponibles?\n3. Desea atacar?\n4. Desea recibir daño?\n5. Desea salir?")
        opcion=input("Ingrese su eleccion aqui")
        if opcion=="5":
            break
        elif opcion=="1":
            print("elija la clase del personaje\n1. Soldado\n2. Mago\n3. Arquero")
            subopcion=input("ingrese su opcion aqui: ")
            if subopcion=="1":
                nombre=input("Ingrese el nombre: ")
                perso=soldado(nombre,100,10, "Soldado")
            if subopcion=="2":
                nombre=input("Ingrese el nombre: ")
                perso=mago(nombre,50,15, "Mago")
            if subopcion=="3":
                nombre=input("Ingrese el nombre: ")
                perso=arquero(nombre,80,5, "Arquero")
            system.agregar_personajes(perso)
interfaz()
        
