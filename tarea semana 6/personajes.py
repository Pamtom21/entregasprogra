class personaje:
    def __init__(self,Nombre,Vida, p_ataque, clase, mov):
        self.nombre=Nombre
        self.vida=Vida
        self.p_ataque=p_ataque
        self.clase=clase
        self.mov= mov
    def __str__(self):
        return f"{self.nombre}"
    def ataque(self, persona):
        print(f"has hecho {self.p_ataque} puntos de daño a {persona}\n")
    def recibir_dano(self,persona):
        print(f"{self.nombre} te han atacado\n")
        self.vida-=persona.p_ataque
        print(f"tu nueva vida es {self.vida}\n")
    def stats(self):
        print(f"Estas son las estadisticas de {self.nombre}\nvida: {self.vida}\nataque: {self.p_ataque}\nclase: {self.clase}\n")
    def mover(self):
        print(f"te has movido {self.mov}")
class soldado(personaje):
    def __init__(self, Nombre, Vida, p_ataque, clase,mov):
        super().__init__(Nombre, Vida, p_ataque, clase,mov)
    def ataque(self,persona):
        print("atacas de modo fisico")
        super().ataque(persona)

class mago(personaje):
    def __init__(self, Nombre, Vida, p_ataque, clase,mov):
        super().__init__(Nombre, Vida, p_ataque, clase,mov)
    def ataque(self,persona):
        print("atacas a larga de distancia por medio de magia negra")
        super().ataque(persona)
class arquero(personaje):
    def __init__(self, Nombre, Vida, p_ataque, clase,mov):
        super().__init__(Nombre, Vida, p_ataque, clase,mov)
    def ataque(self,persona):
        print("tu ataque es por medio de flechas")
        super().ataque(persona)
class jugador1:
    def __init__(self):
        self.personajes=[]
    def agregar_personajes(self, personaje):
        self.personajes.append(personaje)
    def mostrar_personajes(self):
        print("los personajes disponibles son:")
        for k in range(len(self.personajes)):
            print(f"{k}. {self.personajes[k]}")
    def eliminar_personaje(self):
        for k in range(len(self.personajes)):
            if self.personajes[k].vida <= 0:
                print(f"{self.personajes[k]} ha muerto")
                self.personajes.remove(self.personajes[k])
class jugador2:
    def __init__(self):
        self.personajes=[]
    def agregar_personajes(self, personaje):
        self.personajes.append(personaje)
    def mostrar_personajes(self):
        print("los personajes disponibles son: ")
        for k in range(len(self.personajes)):
            print(f"{k}. {self.personajes[k]}")
    def eliminar_personaje(self):
        for k in range(len(self.personajes)):
            if self.personajes[k].vida <= 0:
                print(f"{self.personajes[k]} ha muerto\n")
                self.personajes.remove(self.personajes[k])
def j1(pj1,pj2):
        print("Menu jugador 1\n")
        print("1. Desea crear un personaje?\n2.Desea ver los personajes disponibles?\n3. Desea atacar?")
        opcion=input("Ingrese su eleccion aqui: ")
        print("\n")
        if opcion=="1":
            print("elija la clase del personaje\n1. Soldado\n2. Mago\n3. Arquero")
            subopcion=input("ingrese su opcion aqui: ")
            if subopcion=="1":
                nombre=input("Ingrese el nombre: ")
                perso=soldado(nombre,100,10, "Soldado",5)
            if subopcion=="2":
                nombre=input("Ingrese el nombre: ")
                perso=mago(nombre,50,15, "Mago",2)
            if subopcion=="3":
                nombre=input("Ingrese el nombre: ")
                perso=arquero(nombre,80,5, "Arquero",3)
            pj1.agregar_personajes(perso)
            print("El personaje a sido creado con exito\n")
        elif opcion=="2":
            pj1.mostrar_personajes()
            print("desea ver las estadisticas del personaje\n1. Si\n2. No")
            subopcion=input("Ingrese su opcion aqui: ")
            print("\n")
            if subopcion=="1":
                print("elija un personaje")
                pj1.mostrar_personajes()
                x=int(input("Ingrese el numero de personaje: "))
                print("\n")
                pj1.personajes[x].stats()
            elif subopcion=="2":
                print("gracias por jugar")
                print("\n")
            else: 
                print("fatal error")
                print("\n")
        elif opcion=="3":
            print("elija que personaje desea usar para atacar: ")
            pj1.mostrar_personajes()
            x=int(input("Ingrese el numero del personaje: "))
            print("\n")
            print("Elija el personaje a atacar: ")
            pj2.mostrar_personajes()
            y=int(input("Ingrese aqui el personaje: "))
            person=pj2.personajes[y]
            pj1.personajes[x].ataque(person)
            if len(pj2.personajes)>0:
                pj2.personajes[y].recibir_dano(pj1.personajes[x])
                pj2.eliminar_personaje()
            else:
                print("No hay personajes vivos\n")
def j2(pj1,pj2):
        print("Menu jugador 2\n")
        print("1. Desea crear un personaje?\n2.Desea ver los personajes disponibles?\n3. Desea atacar?")
        opcion=input("Ingrese su eleccion aqui: ")
        print("\n")
        if opcion=="1":
            print("elija la clase del personaje\n1. Soldado\n2. Mago\n3. Arquero")
            subopcion=input("ingrese su opcion aqui: ")
            if subopcion=="1":
                nombre=input("Ingrese el nombre: ")
                perso=soldado(nombre,100,10, "Soldado",5)
            if subopcion=="2":
                nombre=input("Ingrese el nombre: ")
                perso=mago(nombre,50,15, "Mago",2)
            if subopcion=="3":
                nombre=input("Ingrese el nombre: ")
                perso=arquero(nombre,80,5, "Arquero",3)
            pj2.agregar_personajes(perso)
            print("El personaje a sido creado con exito\n")
        elif opcion=="2":
            pj2.mostrar_personajes()
            print("desea ver las estadisticas del personaje\n1. Si\n2. No")
            subopcion=input("Ingrese su opcion aqui: ")
            print("\n")
            if subopcion=="1":
                print("elija un personaje")
                pj2.mostrar_personajes()
                x=int(input("Ingrese el numero de personaje: "))
                print("\n")
                pj2.personajes[x].stats()
            elif subopcion=="2":
                print("gracias por jugar\n")
            else: 
                print("fatal error\n")
        elif opcion=="3":
            print("elija que personaje desea usar para atacar: ")
            pj2.mostrar_personajes()
            print("\n")
            x=int(input("Ingrese el numero del personaje: "))
            print("Elija el personaje a atacar ")
            pj1.mostrar_personajes()
            y=int(input("Ingrese aqui el personaje: "))
            person=pj1.personajes[y]
            pj2.personajes[x].ataque(person)
            if len(pj1.personajes)>0:
                pj1.personajes[y].recibir_dano(pj2.personajes[x])
                pj1.eliminar_personaje()
            else:
                print("No hay personajes vivos\n")
def interfaz():
    pj1=jugador1()
    pj2=jugador2()
    while True:
        print("Hola gamers")
        print("Elija un jugador:\n1. Jugador 1\n2. Jugador 2\n3. Salir")
        opcion=input("Ingrese aqui su opcion: ")
        if opcion=="3":
            break
        elif opcion=="1":
            j1(pj1,pj2)
        elif opcion=="2":
            j2(pj1,pj2)
interfaz()
        
