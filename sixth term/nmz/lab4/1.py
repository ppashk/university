import neurolab as nl
import pylab as pl
import numpy as np
import os


def plot_errors(errors):
    pl.plot(errors)
    pl.xlabel('Epoch number')
    pl.ylabel('Train error')
    pl.grid()
    pl.show()

def plot_graph(x, y, axis_bound=None, net=None):
    pl.figure(0)
    for xi,yi in zip(x, y):
        if yi[0] == 1:
            pl.scatter(xi[0], xi[1], c='r')
        else: 
            pl.scatter(xi[0], xi[1], c='b')
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
    

x = [[-0.5, -0.5], [-1, 0], [0, 0.5], [0.5, 1]]
y = [[0], [0], [1], [1]]

plot_graph(x, y)
if os.path.exists('1nn.net'):
    load_net = nl.load('1nn.net')
    plot_graph(x, y, 3, load_net)
    x1  = float(input("Input first coord: "))
    x2  = float(input("Input second coord: "))
    print(f"PREDICTION: {load_net.sim([[x1,x2]]).T}")
        
else:
    net = nl.net.newp([[-2,2], [-2,2]], 1)
    errors = net.train(input=x, target=y, epochs=10, show=True)
    net.save('1nn.net')
    plot_errors(errors)
