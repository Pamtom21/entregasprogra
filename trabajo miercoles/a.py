def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        print("lista: ",arr,"\n", "parte izquierda: ",less,"comparativo: ",pivot, "parte derecha: ",greater)
        return quick_sort(less) + [pivot] + quick_sort(greater)
def binary_search(arr, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            print("El numero esta en la posicion: ", mid)
            return mid

        elif arr[mid] > x:
            print("el numero se encuentra en la parte izquierda: ", arr[:mid])
            return binary_search(arr, low, mid - 1, x)
 
        else:
            print("el numero se encuentra en la parte derecha: ",arr[mid:])
            return binary_search(arr, mid + 1, high, x)
    else:
        print("El numero no se encuentra disponible en la lista")
class sistema:
    def __init__(self):
        self.lista= []
    def agregar(self):
        d='1'
        while d == '1': 
            try:
                x=int(input("Ingrese un numero: "))
                self.lista.append(x)
                print(self.lista)
                op=input('ingrese y para salir o enter para continuar: ')
                if op=='y':
                    d= '2'
            except ValueError:
                print("Error")
    def ordenar(self):
        if len(self.lista) > 1:
            self.lista = quick_sort(self.lista)
            print("Lista ordenada: ", self.lista)
            return self.lista
        else: 
            print("Se necesitan al menos 2 numeros en la lista para usar esta funcion")

    def buscar(self):
        if len(self.lista) >= 1:
            k=0
            while k < len(self.lista)-1:
                if self.lista[k] < self.lista[k+1]:
                    f='1'
                    k+=1
                else:
                    f='2'
                    break
            if f == '1':
                try:
                    x=int(input("Ingrese el numero a buscar: "))
                    binary_search(self.lista,0, len(self.lista)-1,x)
                except ValueError:
                    print("Error")
            elif f == '2':
                print("La lista no esta ordenada")
        else:
            print("Se necesita al menos un numero en la lista para usar esta funcion")
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
        