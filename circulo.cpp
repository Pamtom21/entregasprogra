#include <iostream>
using namespace std;
class circulo{
    public:
        int radio;
    public:
        circulo(int);
        void CalcularArea();
        void CalcularPerimetro();
        void CambiarRadio();
};
circulo::circulo(int  _radio){
    radio = _radio;
}
void circulo::CalcularArea(){
    float pi= 3.14;
    float x= (radio*radio)*pi;
    cout<<"el Area es ";
    cout<<x<<endl;
}
void circulo::CalcularPerimetro(){
    float pi= 3.14;
    float x= 2*pi*radio;
    cout<<"el Perimetro es ";
    cout<<x<<endl;
}
void circulo::CambiarRadio(){
    string f;
    cout<<"Desea cambiar el radio y(si) o n(no) ",cin>>f;
    int newradio;
    if(f=="y"){
        cout<<"Ingrese valor del Radio ", cin>> newradio ;
        radio = newradio;
    }
}
int main()
    {
        circulo c1= circulo(3);
        string d;
        cout<<"Desea continuar y(si) o n(no) ", cin>> d;
        while (d=="y")
        {
            c1.CambiarRadio();
            c1.CalcularArea();
            c1.CalcularPerimetro();
            cout<<"Desea continuar y(si) o n(no)", cin>>d;
        }
    }