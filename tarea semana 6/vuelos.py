class reserva:
    def __init__(self,nom_pasajero, num_vuelo, fecha):
        self.nom_pasajero=nom_pasajero
        self.num_vuelo=num_vuelo
        self.fecha= fecha
    def mostrar_detalle(self):
        print(f"Pasajero:{self.nom_pasajero}")
        print(f"Vuelo:{self.num_vuelo}")
        print(f"Fecha:{self.fecha}")
    def __str__(self):
        return f"Vuelo: {self.num_vuelo}"
class reservaEconomica(reserva):
    def __init__(self, nom_pasajero, num_vuelo, fecha, valor):
        super().__init__(nom_pasajero, num_vuelo, fecha)
        self.valor=valor
    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Valor: {self.valor}")
class reservaBusiness(reserva):
    def __init__(self, nom_pasajero, num_vuelo, fecha,tipo_asiento):
        super().__init__(nom_pasajero, num_vuelo, fecha)
        self.tipo_asiento=tipo_asiento
    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Tipo de asiento: {self.tipo_asiento}")
class reservaPrimeraCLase(reserva):
    def __init__(self, nom_pasajero, num_vuelo, fecha,tipo_comida):
        super().__init__(nom_pasajero, num_vuelo, fecha)
        self.tipo_comida=tipo_comida
    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Comida: {self.tipo_comida}")
class sistema:
    def __init__(self):
        self.vuelos=[]
    def agregar_vuelos(self, vuelo):
        self.vuelos.append(vuelo)
    def mostrar_vuelos(self):
        print("Estas son las reservas ingresadas")
        for j in range(len(self.vuelos)):
            print(f"{j}. {self.vuelos[j]}")
def interfaz():
    system=sistema()
    while True:
        print("Bienvenido a vuelos fantasma\nElija una opcion\n1. Agregar vuelos\n2. Mostrar vuelos\n3. Salir\n")
        opcion=input("Ingrese aqui su opcion: ")
        if opcion == "3":
            break
        elif opcion=="1":
            print("elija entre\n1. Reserva economica\n2. Reserva Business\n3. Reserva Primera Clase\n")
            subopcion=input("Ingrese aqui su opcion: ")
            if subopcion=="1":
                nom=input("Ingrese Nombre del pasajero: ")
                num=input("Ingrese Numero de Vuelo: ")
                fecha=input("Ingrese fecha del vuelo: ")
                valor= input("Ingrese valor del vuelo: ")
                reser=reservaEconomica(nom,num,fecha,valor)
                system.agregar_vuelos(reser)
            elif subopcion=="2":
                nom=input("Ingrese Nombre del pasajero: ")
                num=input("Ingrese Numero de Vuelo: ")
                fecha=input("Ingrese fecha del vuelo: ")
                tipo_asien=input("Ingrese el tipo de asiento: ")
                reser=reservaBusiness(nom,num,fecha,tipo_asien)
                system.agregar_vuelos(reser)
            elif subopcion=="3":
                nom=input("Ingrese Nombre del pasajero: ")
                num=input("Ingrese Numero de Vuelo: ")
                fecha=input("Ingrese fecha del vuelo: ")
                tipo_comida=input("Ingrese el tipo de comida: ")
                reser=reservaPrimeraCLase(nom,num,fecha,tipo_comida)
                system.agregar_vuelos(reser)
            else:
                print("Fatal error")
        elif opcion=="2":
            system.mostrar_vuelos()
            print("Desea ver el detalle de las reservas\n1. Si\n2. No")
            subopcion=input("Ingrese aqui su opcion: ")
            if subopcion=="1":
                print("Elija una reserva ")
                system.mostrar_vuelos()
                x=int(input("Ingrese aqui el numero de reserva "))
                system.vuelos[x].mostrar_detalle()
            elif subopcion=="2":
                print("Gracias por usar sistema de reservas ")
            else:
                print("Fatal error")
        else:
            print("Fatal error")
interfaz()   