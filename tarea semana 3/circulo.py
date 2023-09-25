class circulo:
    def __init__(self,radio):
        self.radio=radio
    def calcularArea(self):
        pi=3.14
        x=(self.radio**2)*pi
        print("El area es ", x)
    def calcularPeri(self):
        pi=3.14
        x=2*pi*self.radio
        print("el perimetro es: ", x)
    def cambiar_radio(self,_radio):
        newradio=_radio
        self.radio = newradio
l=1
c1= circulo(2)
while l>0:
    v=str(input("Desea cambiar radio y(si) o n(no) "))
    if v=="y":
        c1.cambiar_radio(int(input("Ingrese Radio ")))
    c1.calcularArea()
    c1.calcularPeri()
    t=str(input("ingrese y para continuar o n para salir : "))
    if t=="n":
        l=0