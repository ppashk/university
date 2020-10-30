#include<iostream>
#include<cmath>
#include<iomanip>
#define e 0.000001
using namespace std;
double f(double x) {
    return x*x*x - 3 * x*x - 14*x-8;
}
double f1(double x) {
    return 3*x * x + 6*x-14;
}
double f2(double x) {
    return 6*x+6 ;
}
void dyhotomy() {
    cout << "Dyhotomy Metod : \n";
    double a = -2, b = 5.7;

    for (int i = 0;i<20&&abs(b-a)>e;i++) {
        double c = (a + b) / 2; cout << "C " << c << endl;
        cout << "iteration : " << i+1 << " value : "<<fixed <<setprecision(10)<< c << endl;
        cout << "   f(a)    " << f(a); cout << " f(b)    " << f(b); cout << " f(c)    " << f(c) << endl;;
        if (f(a)*f(c) < 0)b = c;
        if (f(b)*f(c) < 0)a = c;
    }

}
void iteration() {
    cout << "Simple iterations Metod : \n";
    double a = 1, b = 1.5;

    double j = 1 / f1(b);

    double x0 = (a + b) / 2;
    double xi = x0 - j * f(x0);


    for (int i = 0; i < 20&&abs(x0-xi)>e; i++) {
        x0 = xi;
        cout << " iteration : " << i + 1 << " value : " << fixed << setprecision(10) << xi << endl;
        xi = x0 - j * f(x0);
    }



}
void nyton() {
    cout << "Nyton Metod : \n";
    double a = 1, b = 1.5;

    double x0 = 0;
    if (f(a)*f2(a) > 0)x0 = a;
    if (f(b)*f2(b) > 0)x0 = b;

    double xi = x0 - (f(x0) / f1(x0));

    for (int i = 0; i<20 && abs(xi - x0)>e; i++) {
        cout << "   x0=      " << x0 << endl;;
        cout << "   f(x0)    " << f(x0); cout << " f(b)    " << f(b); cout << " f1(c)    " << f1(x0) << endl; cout << "   f2(c)    " << f2(b) << endl;
        x0 = xi;
        cout << "iteration : " << i + 1 << " value : " << fixed << setprecision(10) << xi << endl;
        xi = x0 - (f(x0) / f1(x0));
    }


}
void hord() {
    cout << "Hord Metod : \n";
    double a = 1, b = 1.5;
    double x0 = a - (f(a)*(b - a) / (f(b) - f(a)));

    for (int i = 0; i<20 && abs(a-b)>e; i++) {
        cout << " iteration : " << i + 1 << " value : " << fixed << setprecision(10) << x0 << endl;

        if (f(x0) == 0)break;

        if (f(a)*f(x0) < 0)b = x0;
        if (f(x0)*f(b) < 0)a = x0;

        x0 = a - (f(a)*(b - a) / (f(b) - f(a)));

    }
}
int main() {
    dyhotomy();
    iteration();
    nyton();
    hord();
    system("pause");
    return 0;
}