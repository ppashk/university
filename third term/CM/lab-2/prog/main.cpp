#include<iostream>

using namespace std;

int main()
{
    int i, n, k, n1 = 5;
    double t, z, q, d;
    double** A;
    double* B;
    double* eps;
    double* X;
    double* et;
    int N;
    cout << "Vvedit Rozmir  masuviv:";
    cin >> N;

    B = new double[N];
    eps = new double[N];
    X = new double[N];
    et = new double[N];
    A = new double*[N];
    for (int i = 0; i<N; i++)
        A[i] = new double[N];
    cout << "Vvedit  " << N << " ryadkiv po " << N << " 4isel:\n";
    for (i = 0; i<N; i++)
        for (k = 0; k<N; k++)
            cin >> A[i][k];
    n1 = N;
    cout << "Matrix A:" << endl;
    for (i = 0; i<N; i++)
    {
        for (k = 0; k<N; k++)
            cout << A[k][i] << "\t ";
        cout << endl;
    }

    cout << "Vvedit "<< N <<" 4isel:" << endl;
    for (i = 0; i <N; i++)
        cin >> B[i];

    cout << "Matrix B:" << endl;
    for (i = 0; i<N; i++)
        cout << B[i] << endl;

    n = n1 - 1;
    eps[0] = -A[0][1] / A[0][0];
    et[0] = B[0] / A[0][0];

    for (i = 1; i<n; i++)
    {
        z = A[i][i] + A[i][i - 1] * eps[i - 1];
        eps[i] = -A[i][i + 1] / z;
        et[i] = (B[i] - A[i][i - 1] * et[i - 1]) / z;
    }

    X[n] = (B[n] - A[n][n - 1] * et[n - 1]) / (A[n][n] + A[n][n - 1] * eps[n - 1]);

    for (i = n - 1; i >= 0; i--)
        X[i] = eps[i] * X[i + 1] + et[i];

    cout << "Matrix X:" << endl;
    for (i = 0; i<n1; i++)
        cout << X[i] << endl;

    delete[] B;
    delete[] eps;
    delete[] et;
    delete[] X;
    for (int i = 0; i<N; i++)
        delete[] A[i];
    delete[] A;


    system("pause");
    return 0;
}