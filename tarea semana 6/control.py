class persona:
    def __init__(self, Nombre, edad):
        self.nombre=Nombre
        self.edad=edad
    def mostrar(self):
        print(f"Soy {self.nombre} y tengo {self.edad}")
class estudiante(persona):
    def __init__(self,Nombre,edad):
        super().__init__(Nombre,edad)
        self.asignaturas=[]
    def agregar_asig(self,asig):
        self.asignaturas.append(asig)
    def mostrar_asigna(self):
        for k in range(len(self.asignaturas)):
            print(k)
class profesor(persona):
    def __init__(self, Nombre, edad,asigna):
        super().__init__(Nombre, edad)
        self.asigna= asigna
class asignatura:
    