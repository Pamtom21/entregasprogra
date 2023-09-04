#include <iostream>
using namespace std;
class playlist{
    public:
        string nombre;
        string canciones[100]={};
        string estado;
        string indice;
    public:
        playlist(string, string, string);
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
playlist::playlist(string _nombre, string _estado,string _indice){
    nombre = _nombre;
    estado= _estado;
    indice=_indice;
}
void agrega_cancion(){
    
}
