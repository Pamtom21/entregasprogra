class producto:
    def __init__(self,nombre,precio,categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria= categoria
    def __str__(self):
        return f"{self.nombre}"
    def mostrar_detalle(self):
        print("\n")
        print("Este es el detalle del producto:\n")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Categoria: {self.categoria}")

class Electronico(producto):
    def __init__(self, nombre, precio, categoria, gama):
        super().__init__(nombre,precio,categoria)
        self.gama = gama
    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Gama: {self.gama}")

class Alimenticio(producto):
    def __init__(self, nombre, precio, categoria, marca):
        super().__init__(nombre, precio, categoria)
        self.marca = marca
    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Marca: {self.marca}")
class Vestimenta(producto):
    def __init__(self, nombre, precio, categoria, Talla):
        super().__init__(nombre, precio, categoria)
        self.talla= Talla
    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Talla: {self.talla}")
class Catalogo_productos():
    def __init__(self):
        self.productos= []
    def agregar(self, producto):
        self.productos.append(producto)
    def mostrar_productos(self):
        for k in range(len(self.productos)):
            print(f"{k}. {self.productos[k]}")
def interfaz():
    catalogo = Catalogo_productos()
    while True:
        print("Elija una opcion\n")
        print("1. Agregar productos")
        print("2. Mostrar Productos")
        print("3. Salir")
        opcion= str(input("Ingrese su opcion aqui: "))
        if opcion == '3':
         break
        if opcion == '1':
            print("1. Electronico\n"
                  "2. Alimenticio\n" 
                  "3. Vestimenta\n")
            subopcion= str(input("ingrese una opcion: "))
            if subopcion == '1': 
                nombre= input("Nombre: ")
                precio=int(input("Precio: "))
                gama=input("Gama(Alta, Media, Baja): ")
                if gama == "Alta" or "Media" or "Baja" or "alta" or "media" or "baja":
                    prod= Electronico(nombre,precio , "Electronico", gama)
                    catalogo.agregar(prod)
                    print("producto agregado con exito")
                else:
                    print("datos incorrectos ")
            if subopcion == '2':
                nombre= input("Nombre: ")
                precio=int(input("Precio: "))
                marca=input("Marca: ")
                prod= Alimenticio(nombre,precio , "Alimenticio", marca)
                catalogo.agregar(prod)
                print("producto agregado con exito")
            if subopcion == '3':
                nombre= input("Nombre: ")
                precio=int(input("Precio: "))
                talla=input("Gama(XL, L, M, S): ")
                if talla == "XL" or "L" or "M" or "S"or "xl" or "l" or "m" or "s":
                    prod= Vestimenta(nombre,precio , "Vestimenta", talla)
                    catalogo.agregar(prod)
                    print("producto agregado con exito")
                else:
                    print("datos incorrectos ")
        if opcion == '2':
            catalogo.mostrar_productos()
            print("desea ver el detalle de algun producto?")
            subopcion= input("si(1) o no(2): \n")
            if subopcion == '1':
                catalogo.mostrar_productos()
                print("elija un producto\n")
                x= int(input("ingrese el numero de producto aqui: \n"))
                catalogo.productos[x].mostrar_detalle()
            else:
                print("gracias vuelva pronto ")
if __name__ == "__main__":
    interfaz()