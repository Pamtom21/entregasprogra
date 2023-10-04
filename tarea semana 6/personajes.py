f=0
h=0
class personaje:
    def __init__(self,Nombre,Vida, p_ataque, clase, mov, id,icono):
        self.nombre=Nombre
        self.vida=Vida
        self.p_ataque=p_ataque
        self.clase=clase
        self.mov= mov
        self.id=id
        self.icono=icono
    def __str__(self):
        return f"{self.icono}"
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
    def __init__(self, Nombre, Vida, p_ataque, clase,mov,id,icono="S"):
        super().__init__(Nombre, Vida, p_ataque, clase,mov,id,icono)
    def ataque(self,persona):
        print("atacas de modo fisico")
        super().ataque(persona)

class mago(personaje):
    def __init__(self, Nombre, Vida, p_ataque, clase,mov,id,icono="M"):
        super().__init__(Nombre, Vida, p_ataque, clase,mov,id,icono)
    def ataque(self,persona):
        print("atacas a larga de distancia por medio de magia negra")
        super().ataque(persona)
class arquero(personaje):
    def __init__(self, Nombre, Vida, p_ataque, clase,mov,id,icono="l"):
        super().__init__(Nombre, Vida, p_ataque, clase,mov,id,icono)
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
class campo:
    def __init__(self,columnas, filas):
        self.columnas=columnas
        self.filas=filas
        self.campos=[['_' for x in range(self.columnas)] for y in range(self.filas)]
    def mostrar_campo(self):
        for k in self.campos:
            resultado= "   ".join([str(y) for y in k])
            print(resultado)

    def agregar_perso(self,perso,y,x):
        self.campos[x][y]= perso
        return self.campos
    def eliminar_perso(self):
        for k in range(len(self.campos)):
            for j in range(len(self.campos)):
                if self.campos[k][j] != 'X' and self.campos[k][j].vida <= 0:
                    self.campos[k][j]= 'X'   
                    return self.campos
    def mover_personaje(self,person):
            print("Hacia donde desea moverse\n1. adelante\n2. atras\n3. izquierda\n4. derecha")
            opcion=input("Ingrese su opcion aqui: ")
            if opcion=="1":
                person.mostrar_personajes()
                p=int(input("elija que personaje desea mover: "))
                x=int(input("Ingrese cuantas casillas que desea moverse: "))
                if x>person.personajes[p].mov:
                    x=person.personajes[p].mov
                for k in range(len(self.campos)):
                    for j in range(len(self.campos)):
                        if self.campos[k][j] != '_':
                            if self.campos[k][j].id == person.personajes[p].id :
                                l= k+x
                                if l > len(self.campos)-1:
                                    l=len(self.campos)-1
                                self.campos[l][j] = person.personajes[p]
                                self.campos[k][j]= '_'
                                return self.campos
            elif opcion == "2":
                person.mostrar_personajes()
                p=int(input("elija que personaje desea mover: "))
                x=int(input("Ingrese cuantas casillas que desea moverse: "))
                if x>person.personajes[p].mov:
                    x=person.personajes[p].mov
                for k in range(len(self.campos)):
                    for j in range(len(self.campos)):
                        if self.campos[k][j] != '_':
                            if self.campos[k][j].id == person.personajes[p].id :
                                l= k-x
                                if l < 0:
                                    l=0
                                self.campos[l][j] = person.personajes[p]
                                self.campos[k][j]= '_'
                                return self.campos
            elif opcion == "3":
                person.mostrar_personajes()
                p=int(input("elija que personaje desea mover: "))
                x=int(input("Ingrese cuantas casillas que desea moverse: "))
                if x>person.personajes[p].mov:
                    x=person.personajes[p].mov
                for k in range(len(self.campos)):
                    for j in range(len(self.campos)):
                        if self.campos[k][j] != '_':
                            if self.campos[k][j].id == person.personajes[p].id :
                                l= j-x
                                if l < 0:
                                    l=0
                                self.campos[k][l] = person.personajes[p]
                                self.campos[k][j]= '_'
                                return self.campos
            elif opcion == "4":
                person.mostrar_personajes()
                p=int(input("elija que personaje desea mover: "))
                x=int(input("Ingrese cuantas casillas que desea moverse: "))
                if x>person.personajes[p].mov:
                    x=person.personajes[p].mov
                for k in range(len(self.campos)):
                    for j in range(len(self.campos)):
                        if self.campos[k][j] != '_':
                            if self.campos[k][j].id == person.personajes[p].id :
                                l= j+x
                                if l >= len(self.campos)-1:
                                    l=len(self.campos)-1
                                self.campos[k][l] = person.personajes[p]
                                self.campos[k][j]= '_'
                                return self.campos
    def mover_personaje2(self,person):
            print("Hacia donde desea moverse\n1. adelante\n2. atras\n3. izquierda\n4. derecha")
            opcion=input("Ingrese su opcion aqui: ")
            if opcion=="1":
                person.mostrar_personajes()
                p=int(input("elija que personaje desea mover: "))
                x=int(input("Ingrese cuantas casillas que desea moverse: "))
                if x>person.personajes[p].mov:
                    x=person.personajes[p].mov
                for k in range(len(self.campos)):
                    for j in range(len(self.campos)):
                        if self.campos[k][j] != '_':
                            if self.campos[k][j].id == person.personajes[p].id :
                                l= k-x
                                if l > len(self.campos)-1:
                                    l=len(self.campos)-1
                                self.campos[l][j] = person.personajes[p]
                                self.campos[k][j]= '_'
                                return self.campos
            elif opcion == "2":
                person.mostrar_personajes()
                p=int(input("elija que personaje desea mover: "))
                x=int(input("Ingrese cuantas casillas que desea moverse: "))
                if x>person.personajes[p].mov:
                    x=person.personajes[p].mov
                for k in range(len(self.campos)):
                    for j in range(len(self.campos)):
                        if self.campos[k][j] != '_':
                            if self.campos[k][j].id == person.personajes[p].id :
                                l= k+x
                                if l < 0:
                                    l=0
                                self.campos[l][j] = person.personajes[p]
                                self.campos[k][j]= '_'
                                return self.campos
            elif opcion == "3":
                person.mostrar_personajes()
                p=int(input("elija que personaje desea mover: "))
                x=int(input("Ingrese cuantas casillas que desea moverse: "))
                if x>person.personajes[p].mov:
                    x=person.personajes[p].mov
                for k in range(len(self.campos)):
                    for j in range(len(self.campos)):
                        if self.campos[k][j] != '_':
                            if self.campos[k][j].id == person.personajes[p].id :
                                l= j-x
                                if l < 0:
                                    l=0
                                self.campos[k][l] = person.personajes[p]
                                self.campos[k][j]= '_'
                                return self.campos
            elif opcion == "4":
                person.mostrar_personajes()
                p=int(input("elija que personaje desea mover: "))
                x=int(input("Ingrese cuantas casillas que desea moverse: "))
                if x>person.personajes[p].mov:
                    x=person.personajes[p].mov
                for k in range(len(self.campos)):
                    for j in range(len(self.campos)):
                        if self.campos[k][j] != '_':
                            if self.campos[k][j].id == person.personajes[p].id :
                                l= j+x
                                if l >= len(self.campos)-1:
                                    l=len(self.campos)-1
                                self.campos[k][l] = person.personajes[p]
                                self.campos[k][j]= '_'
                                return self.campos


def j1(pj1,pj2,camp):
        global f
        print("Menu jugador 1\n")
        print("1. Crear un personaje\n2. Ver los personajes disponibles?\n3. Atacar\n4. Desplegar tropas\n5. Mover tropas ")
        opcion=input("Ingrese su eleccion aqui: ")
        print("\n")
        if opcion=="1":
            print("elija la clase del personaje\n1. Soldado\n2. Mago\n3. Arquero")
            subopcion=input("ingrese su opcion aqui: ")
            if subopcion=="1":
                nombre=input("Ingrese el nombre: ")
                perso=soldado(nombre,100,10, "Soldado",3,str(f))
                f+=1
            if subopcion=="2":
                nombre=input("Ingrese el nombre: ")
                perso=mago(nombre,50,15, "Mago",2,str(f))
                f+=1
            if subopcion=="3":
                nombre=input("Ingrese el nombre: ")
                perso=arquero(nombre,80,5, "Arquero",3,str(f))
                f+=1
            pj1.agregar_personajes(perso)
            print("El personaje a sido creado con exito\n")
            return f
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
                camp.eliminar_perso()
            else:
                print("No hay personajes vivos\n")
        elif opcion=="4":
            pj1.mostrar_personajes()
            p=int(input("Elija un personaje: "))
            per=pj1.personajes[p]
            y=int(input("Elija una posicion "))
            if y>9:
                y=9
                camp.agregar_perso(per,y,0)
            camp.agregar_perso(per,y,0)
        elif opcion=="5":
                camp.mover_personaje(pj1)
                
def j2(pj1,pj2,camp):
        global h
        print("Menu jugador 2\n")
        print("1. Crear un personaje?\n2. Ver los personajes disponibles\n3. Atacar\n4. Desplegar tropas\n5. Mover ")
        opcion=input("Ingrese su eleccion aqui: ")
        print("\n")
        if opcion=="1":
            print("elija la clase del personaje\n1. Soldado\n2. Mago\n3. Arquero")
            subopcion=input("ingrese su opcion aqui: ")
            if subopcion=="1":
                nombre=input("Ingrese el nombre: ")
                perso=soldado(nombre,100,50, "Soldado",3,str(h))
                h+=1
            if subopcion=="2":
                nombre=input("Ingrese el nombre: ")
                perso=mago(nombre,50,15, "Mago",2,str(h))
                h+=1
            if subopcion=="3":
                nombre=input("Ingrese el nombre: ")
                perso=arquero(nombre,80,5, "Arquero",3,str(h))
                h+=1
            pj2.agregar_personajes(perso)
            print("El personaje a sido creado con exito\n")
            return h
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
                camp.eliminar_perso()
            else:
                print("No hay personajes vivos\n")
        elif opcion=="4":
            pj2.mostrar_personajes()
            p=int(input("Elija un personaje: "))
            per=pj2.personajes[p]
            y=int(input("Elija una posicion "))
            if y>9:
                y=9
                camp.agregar_perso(per,y,9)

            camp.agregar_perso(per,y,9)
        elif opcion == "5":
            camp.mover_personaje2(pj2)



def interfaz():
    camp=campo(10,10)
    pj1=jugador1()
    pj2=jugador2()
    while True:
        camp.mostrar_campo()
        print("Hola gamers")
        print("Elija un jugador:\n1. Jugador 1\n2. Jugador 2\n3. Salir")
        opcion=input("Ingrese aqui su opcion: ")
        if opcion=="3":
            break
        elif opcion=="1":
            j1(pj1,pj2,camp)
        elif opcion=="2":
            j2(pj1,pj2,camp)
interfaz()
# camp=campo(10,10)
# camp.mostrar_campo()
# per=soldado("Juan",50,40,"Soldado",3,1)
# camp.agregar_perso(per,3,9)
# print("\n")
# camp.mostrar_campo()