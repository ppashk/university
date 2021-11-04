import neurolab as nl
import numpy as np
import os
import pylab as pl


def getTrainName(net_trainf):
    net_name = str(net.trainf.__dict__['_train_class']).split('.')[-1]
    net_name = net_name.replace("'>","")
    net_name = net_name.split('Train')[-1]

    return net_name


methods_dict = {1:"GD",2:"GDM", 3:"GDA", 4:"GDX", 5:"RPROP", 6:"BFGS", 7:"NCG", 8:"CG"}

x = np.linspace(0, 20, 40)
y = np.sin(0.5 * x) - (0.72 * np.sin(4 * x)) + (0.25 * np.sin(35 * x))
max_value = np.max(x)
min_value = np.min(x)
size = len(x)
x_train = x.reshape(size, 1)
y_train = y.reshape(size, 1)

if  os.path.exists('../lab5/saved_weights'):
    print("1 - GD")
    print("2 - GDM")
    print("3 - GDA")
    print("4 - GDX")
    print("5 - RPROP")
    print("6 - BFGS")
    print("7 - NCG")
    print("8 - CG")
    
    number = int(input("Input one of netword: "))
    name_method = methods_dict[number]
    net = nl.load(f'saved_weights/{name_method}.net')
    out = net.sim(x_train)
    print(f"Out: {out}")
    print(f"Target: {y_train}")
   
    pl.plot(out, '-', y_train, '--o')
    pl.legend(['train target', 'net output'])
    pl.show()
else:
    trainings = ['nl.train.train_gd','nl.train.train_gdm','nl.train.train_gda',
    'nl.train.train_gdx','nl.train.train_rprop','nl.train.train_bfgs','nl.train.train_ncg','nl.train.train_cg']
    outputs = []
    outputs_dict = {}
    os.mkdir('../lab5/saved_weights')
    
    for train in trainings:
        net = nl.net.newff([[min_value,max_value]],[10,1])
        exec(f"net.trainf = {train}")
        
        net_name = getTrainName(net.trainf)

        print(net_name)
        print("-----------------")



        error = net.train(x_train, y_train, epochs=1000, show=15,goal= 0.00001)

        net.save(f'saved_weights/{net_name}.net')

        out = net.sim(x_train)
        outputs.append(out)
        outputs_dict[f'{net_name}'] = out
        print(f"Errors: {error}")
        print(y_train)
        print(out)

        pl.subplot(211)
        pl.plot(error)
        pl.xlabel('Epoch number')
        pl.ylabel('Error')
        pl.subplot(313) 
        pl.plot(y_train, '-', out, '--')
        pl.xlabel('x')
        pl.ylabel('y')
        pl.title(f"{net_name}")
        pl.legend(['train target', 'net output'])
        pl.show()

    for out in outputs_dict.values():
        pl.plot(out)
    pl.plot(y_train,'--')

    outputs = list(outputs_dict.keys())
    outputs.append('target')
    print(outputs)
    pl.legend(outputs)
    pl.show()
