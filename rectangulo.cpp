#include <iostream>
using namespace std;
class recta{
    public:
        int ancho;
        int alto;
    public:
        recta(int,int);
        void CalcularArea();
        void CalcularPerimetro();
        void CambiarAlto();
        void CambiarAncho();
};
recta::recta(int _ancho, int _alto){
    ancho= _ancho;
    alto= _alto;
}
void recta::CalcularArea(){
    float x= ancho*alto;
    cout<<"\n el Area es "<<x<<""<<endl;
}
void recta::CalcularPerimetro(){
    float x= 2*ancho+2*alto;
    cout<<"\n el perimetro es "<<x<<""<<endl;
}
void recta::CambiarAlto(){
    string d;
    cout<<"\n quiere cambiar alto y(si) o n(no)", cin>> d;
    if (d=="y")
        {
            int newalto;
            cout<<"\n ingrese numero ", cin>> newalto ;
            alto= newalto;
        }
    else{
            cout<<"\n no cambia alto";
        }
}
void recta::CambiarAncho(){
    string d;
    cout<<"\n quiere cambiar ancho y(si) o n(no)", cin>> d;
    if (d=="y")
        {
            int newancho;
            cout<<"\n ingrese numero ", cin>> newancho ;
            ancho= newancho;
        }
    else{
            cout<<"\n no cambia ancho";
        }
}
int main()
    {
        string a;
        recta c1=recta(2, 5);
        cout<<"\n desea continuar y(si) o n(no)",cin>> a;
        while (a=="y"){
            c1.CambiarAlto();
            c1.CambiarAncho();
            c1.CalcularArea();
            c1.CalcularPerimetro();
            cout<<"\n Desea continuar y(si) o n(no)",cin>> a;
        }
    };