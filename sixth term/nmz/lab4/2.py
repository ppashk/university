import neurolab as nl
import numpy as np
import os
import pylab as pl


def plot_errors(errors):
    pl.plot(errors)
    pl.xlabel('Epoch number')
    pl.ylabel('Train error')
    pl.grid()
    pl.show()

def plot_graph(x,y,axis_bound=None,net=None):
    pl.figure(0)
    for xi,yi in zip(x,y):
        if yi[0] == 1:
            pl.scatter(xi[0],xi[1],c='r')
        else: 
            pl.scatter(xi[0],xi[1],c='b')
    pl.xlabel('X-axis')
    pl.ylabel('Y-axis')
    pl.axvline(x=0)
    pl.axhline(y=0)
    
    if net is not None:
        x_axis = np.arange(-axis_bound, axis_bound, 0.1)
        w1 = net.layers[0].np['w'][0][0]
        w2 = net.layers[0].np['w'][0][1]
        print(w1)
        print(w2)
        print(net.layers[0].np['b'][0])
        print('------')
        m = -w1/w2
        c = - net.layers[0].np['b'][0] / w2
        pl.plot(x_axis, m*x_axis + c, label="decision boundary")
    pl.show()


def display_variable_info(X,Y,P,T):
    print("*--------------------------*")
    print(f"X: {X}\tshape: {X.shape}")
    print(f"Y: {Y}\tshape: {Y.shape}")
    print(f"Input: {P}\tshape: {P.shape}")
    print(f"Target: {T}\tshape:{T.shape}")


if os.path.exists('2nn.net'):
    load_net = nl.load('2nn.net')
    x1 = float(input("Input first coord: "))
    x2 = float(input("Input second coord: "))
    print(f"PREDICTION: {load_net.sim([[x1,x2]]).T}")
else:
    n1 = 3
    n2 = 3
    x0 = 10
    alpha = 15
    y0 = 50
    beta = 20
    X = np.random.normal(x0,alpha,(n1,2))
    Y = np.random.normal(y0,beta,(n2,2))
    P = np.concatenate((X,Y))
    T = np.zeros((1, len(P)))

    T[0][:n1] = np.ones(n1)
    T = T.transpose()
    display_variable_info(X,Y,P,T)

    min_value = np.min(P)
    max_value = np.max(P)

    net = nl.net.newp([[min_value, max_value],[min_value, max_value]],1)

    errors = net.train(input=P, target=T, epochs=100, show=True)
    print(net.sim(P))
    plot_errors(errors)
    plot_graph(P,T)
    plot_graph(P,T,100,net)
    net.save('2nn.net')
