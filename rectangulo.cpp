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
    int d;
    cout<<"\n quiere cambiar alto 1(si) o 2(no)", cin>> d;
    if (d==1)
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
    int d;
    cout<<"\n quiere cambiar ancho 1(si) o 2(no)", cin>> d;
    if (d==1)
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
        int a;
        recta c1=recta(2, 5);
        cout<<"\n 1 o 2",cin>> a;
        while (a==1){
            c1.CambiarAlto();
            c1.CambiarAncho();
            c1.CalcularArea();
            c1.CalcularPerimetro();
            cout<<"\n 1 o 2",cin>> a;
        }
    };