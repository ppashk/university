import numpy as np


def training(X,T,Weights,LR):
    sigma = np.zeros(len(T[0]))
    Y = np.zeros(len(T[0]))
    Beta = np.zeros(len(T[0]))
    fl = 1
    epoch = 0
    while(fl):
        epoch+=1
        for k, xk in enumerate(X):
            for i, wi in enumerate(Weights):
                d = 0
                for j in range(len(wi)):
                    d+= wi[j]*xk[j]
                sigma[i]= d
                if sigma[i] >=0:
                    Y[i]=1
                else:
                    Y[i]=0
                Beta[i] = T[k][i]-Y[i]
            fl1 = 1
            for i in range(len(Y)):
                if T[k][i] != Y[i]:
                    fl1 = 0
            if(fl1):
                fl+=1
            else:
                for i,wi in enumerate(Weights):
                    for j in range(len(Weights[i])):
                        Weights[i][j] += LR*xk[j]*Beta[i]
        if fl == 9 :
            fl= 0
        else:
            fl=1
    print("epoch:",epoch)

    
def test(X,T,Weights):
    sigma = np.zeros(len(T[0]))
    Y = np.zeros(len(T[0]))
    for k, xk in enumerate(X):
        for i, wi in enumerate(Weights):
            d = 0
            for j in range(len(wi)):
                d += wi[j] * xk[j]
            sigma[i] = d
            if sigma[i] >= 0:
                Y[i] = 1
            else:
                Y[i] = 0
        print("number ", k+1, "\t", Y, "\t", T[k])

def inputx(Weights):
    print("\ninput x:")
    xtest=input()
    xi=xtest.split()
    xi=list(xi)
    sigma = np.zeros(len(T[0]))
    Y = np.zeros(len(T[0]))
    for i, wi in enumerate(Weights):
        d = 0
        for j in range(len(wi)):
            d += wi[j] * int(xi[j])
        sigma[i] = d
        if sigma[i] >= 0:
            Y[i] = 1
        else:
            Y[i] = 0
    print(Y)
    

X = np.genfromtxt('X.txt',delimiter=' ',dtype=np.float)
T = np.genfromtxt('T.txt', delimiter=' ', dtype=np.float)
Weights = np.random.uniform(-0.1, 0.1, (4,9))
LR = 0.01
training(X,T,Weights,LR)
test(X,T,Weights)

while(1):
    inputx(Weights)
