def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        print("lista: ",arr,"\n", "parte izquierda: ",less,"mitad: ",pivot, "parte derecha: ",greater)
        return quick_sort(less) + [pivot] + quick_sort(greater)
def binary_search(arr, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            print("El numero esta en la posicion: ", mid)
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        print("El numero no se encuentra disponible en la lista")
        return -1
class sistema:
    def __init__(self):
        self.lista= []
    def agregar(self):
        d='1'
        while d == '1': 
            x=int(input("Ingrese numero: "))
            self.lista.append(x)
            print(self.lista)
            op=input('y para salir o enter para continuar')
            if op=='y':
                d= '2'
    def ordenar(self):
        if len(self.lista) > 1:
            self.lista = quick_sort(self.lista)
            print("Lista ordenada: ", self.lista)
            return self.lista
        else: 
            print("Se necesitan al menos 2 numeros para usar esta funcion")

    def buscar(self):
        if len(self.lista) >= 1:
            x=int(input("Ingrese el numero a buscar: "))
            binary_search(self.lista,0, len(self.lista)-1,x)
        else:
            print("Se necesita al menos un numero para usar esta funcion")
siste=sistema()
while True:
    print("Bienvenido al sistema mas ordenado")
    print("1. Agregar numeros\n2. Ordenar lista\n3.Buscar numero en la lista\n4.Salir")
    opcion=input("Ingrese su opcion aqui: ")
    if opcion=="4":
        print( "Gracias vuelva pronto")
        break
    elif opcion=="1":
        siste.agregar()
    elif opcion=="2":
        siste.ordenar()
    elif opcion=="3":
        siste.buscar()
    else:
        print("error")
        