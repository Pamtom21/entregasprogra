class rectangulo:
    def __init__(self,ancho,alto):
        self.ancho= ancho
        self.alto=alto
    def cambiar_ancho(self,_ancho):
        self.ancho=_ancho
    def cambiar_alto(self,_alto):
        self.alto=_alto
    def calcularArea(self):
        x=self.alto*self.ancho
        print("El area es: ", x)
    def calcularPeri(self):
        x=2*self.alto+2*self.ancho
        print("El perimetro es: ", x)
rec1= rectangulo(3,4)
l=1
while l>0:
    v=str(input("Desea cambiar alto y(si) o n(no) "))
    if v=="y":
        rec1.cambiar_alto(int(input("Ingrese alto: ")))
    b=str(input("Desea cambiar ancho y(si) o n(no) "))
    if b=="y":
         rec1.cambiar_ancho(int(input("Ingrese ancho: ")))
    rec1.calcularArea()
    rec1.calcularPeri()
    t=str(input("ingrese y para continuar o n para salir : "))
    if t=="n":
        l=0