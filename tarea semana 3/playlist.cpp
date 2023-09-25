#include <iostream>
using namespace std;
class playlist{
    public:
        string nombre;
        string estado;
        string indice;
        string canciones[100]={};
    public:
        playlist(string, string);
        void agrega_cancion();
        void elimina_cancion();
        void mostrar_canciones();
        void reproducir();
        void seleccionar_cancion();
        void pausar();
        void detener();
        void siguiente_cancion();
        void cancion_anterior();
        void aleatorio();
        void estado_playlist();
        void mostrar_canrep();

};
class cancion{
    public:
        int indice;
        string nombre;
    public:
        cancion(int,string);
};


playlist::playlist(string _nombre, string _estado){
    nombre = _nombre;
    estado= _estado;
}

int main(){
    int b;
    string v;
    cout<<"ingrese un id ", cin>>b;
    cout<<"ingrese un nombre ", cin>>v;
    cancion c1= cancion(b,v);

}