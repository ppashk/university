#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

void solve(const vector<float>& matrix,
           const vector<float>& freeElem,
           vector<float>& x,
           const float allowed_error)
{
    const unsigned n = x.size();
    vector<float> tmp_x(n);

    float error;

    do
    {
        error = 0;

        tmp_x = freeElem;
        for (unsigned i = 0; i < n; ++i)
        {
            for (unsigned j = 0; j < n; ++j)
            {
                if (i != j)
                {
                    tmp_x[i] -= matrix[i * n + j] * x[j];
                }
            }
            const float x_updated = tmp_x[i] / matrix[i * (n + 1)];
            const float e = fabs(x[i] - x_updated);
            x[i] = x_updated;
            if (e > error) { error = e; }
        }
    } while (error > allowed_error);
}


int main()
{
    unsigned n;
    setlocale(LC_ALL, "Ukr");
    cout << "\nInput length\nn = ";
    cin >> n;

    vector<float> x(n);
    vector<float> a(n * n);
    vector<float> b(n);

    cout << "\ninput vector of free elements\n";
    for (auto& b_elem : b)
    {
        cin >> b_elem;
    }

    cout << "\ninput coef\n";
    for (auto& a_elem : a)
    {
        cin >> a_elem;
    }

    float allowed_error;
    cout << "\ninput allowed error\n";
    cin >> allowed_error;

    solve(a, b, x, allowed_error);

    cout << "\nresult\n";
    for (unsigned i = 0; i < n; ++i)
    {
        cout << "\nx[" << i << "]=  " << x[i];
    }
    system("pause");
    return 0;
}