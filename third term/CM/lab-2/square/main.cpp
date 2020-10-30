#include<iostream>
#include<iomanip>
#include <cmath>

using namespace std;
int main()
{
    setlocale(LC_CTYPE, "ukr");
    int n, k;
    int i, j;
    float temp;
    cout << "Input length" << endl;
    cin >> n;
    float **A = new float *[n];
    for (i = 0; i<n; i++)
        A[i] = new float[n];

    float **S = new float *[n];
    for (i = 0; i<n; i++)
        S[i] = new float[n];
    float *b = new float[n];
    float *x = new float[n];
    float *y = new float[n];
    b[0] =5.14 ; b[1] =3.21 ; b[2] =3.23 ; b[3] =6.25 ; b[4] =3.90 ;
    A[0][0] =4.43 ; A[0][1] =1.12 ; A[0][2] =0.95 ; A[0][3] =1.32 ; A[0][4] =0.83 ;
    A[1][0] =1.12 ; A[1][1] =3.53 ; A[1][2] = 2.12; A[1][3] =0.57 ; A[1][4] = 0.91;
    A[2][0] = 0.95; A[2][1] =2.12 ; A[2][2] = 5.38; A[2][3] = 1.29; A[2][4] = 1.57;
    A[3][0] = 1.32; A[3][1] =0.57 ; A[3][2] = 1.29; A[3][3] = 3.82; A[3][4] = 1.25;
    A[4][0] = 0.83; A[4][1] = 0.91; A[4][2] = 1.57; A[4][3] = 1.25; A[4][4] =4.46 ;
    cout << "Input elements " << n << "x" << n << endl;
    for (i = 0; i < n; i++) {
     for (j = 0; j < n; j++)
     {
      cin >> A[i][j];
     }
    }
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
        {
            S[i][j] = 0;
        }
    }

    cout << "input elements of b" << n << "x" << n << endl;
    for (i = 0; i < n; i++)
    {
     cin >> b[i];
    }

    for (i = 0; i < n; i++)
    {
        temp = 0;
        for (k = 0; k < i; k++)
            temp = temp + S[k][i] * S[k][i];
        S[i][i] = sqrt(A[i][i] - temp);
        for (j = i; j < n; j++)
        {
            temp = 0;
            for (k = 0; k < i; k++)
                temp = temp + S[k][i] * S[k][j];
            S[i][j] = (A[i][j] - temp) / S[i][i];
        }
    }
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            cout <<fixed<<setprecision(12)<< S[i][j] << " ";
        }
        cout << endl;
    }
    for (i = 0; i < n; i++)
    {
        temp = 0;
        for (k = 0; k < i; k++)
            temp = temp + S[k][i] * y[k];
        y[i] = (b[i] - temp) / S[i][i];
    }
    for (i = n - 1; i >= 0; i--)
    {
        temp = 0;
        for (k = i + 1; k < n; k++)
            temp = temp + S[i][k] * x[k];
        x[i] = (y[i] - temp) / S[i][i];
    }
    for (i = 0; i < n; i++)
        cout << "x" << i << "= " << x[i] << endl;
    system("pause");
}