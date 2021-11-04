import numpy as np
import neurolab as nl


alpha = 15
beta = 20
x1 = 45
y1 = 50

x1 = np.random.normal(x1,beta,1)
y1 = np.random.normal(y1,beta,1)

p = np.concatenate((x1,y1))
p = p.reshape(1,2)
print(p)
net = nl.load('2nn.net')
print(net.sim(p))
print(net.layers[0].np['w'])
