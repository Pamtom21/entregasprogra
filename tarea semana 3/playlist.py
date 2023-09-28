class musica:
    def __init__(self,nom, artista, genero):
        self.nom=nom
        self.artista=artista
        self.genero=genero
        self.estado= False
class playlist:
    def __init__(self):
        self.canciones=[]
    def agregar(self, can):
        self.cancione.append(can)
    def eliminar(self,can):
        self.canciones.remove(can)
    def mostrar_canciones(self):
        for k in range(len(self.canciones)):
            print(f"{k}. {self.canciones[k]}")
    def reproducir(self,x):
        self.canciones[x].estado=True
        if self.canciones[x] == True:
            print("Se esta reproduciendo")
    def pausar(self,x):
        if self.canciones[x].estado== True:
            self.canciones.estado= False
        else:
            print("la cancion ya esta pausada")
    def siguiente(self, ):
        self.canciones