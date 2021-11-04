import numpy as np


def train(learning_rate, Weights, epochs=2000):
    W = Weights.copy()
    for epoch in range(epochs):
        for i,xi in enumerate(X):
            a = 0
            Y = 0
            for x,w in zip(xi,W):
                a += x * w
            if a > 0:
                 Y = 1
            else:
                 Y = 0
            if T[i] == Y:
                continue
            else:
                d = T[i] - Y
                delta = np.zeros(3)
                for index in range(len(delta)):
                    delta[index] = learning_rate * d * xi[index]

                for w_index in range(len(W)):
                    W[w_index] += delta[w_index]

                print('%.2f' % W[0], '\t', '%.2f' % W[1], '\t', '%.2f' % W[2], '\t', str(xi[0]),
                  '\t', str(xi[1]), '\t', str(xi[2]), '\t', '%.2f' % a, '\t', str(Y), '\t', str(T[i]), '\t', '%.2f' % (learning_rate*d),
                  '\t', '%.2f' % (W[0]*d), '\t', '%.2f' % (W[1]*d), '\t', '%.2f' % (W[2]*d))

    return W


def test(X, trained_W, T):
    print("\ntest:")
    for i,xi in enumerate(X):
        a = 0
        Y = 0
        for x,w in zip(xi,trained_W):
            a += x * w
        if a > 0:
            Y = 1
        else:
            Y = 0
        print(f"Values: {xi} Y: {Y} Target Value: {T[i]}")


def inputx(trained_W):
    print("\ninput x:")
    xtest=input()
    xi=xtest.split()
    xi=list(xi)
    a = 0
    Y = 0
    for x,w in zip(xi,trained_W):
        a += int(x) * w
    if a > 0:
        Y = 1
    else:
        Y = 0
    print(f"Y: {Y}")


X = np.array([[0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]])
T = [0,0,0,1,1,1,1,1]

print('w1\tw2\tw3\tx1\tx2\tx3\ta\tY\tT\tLR\tdw1\tdw2\tdw3')

learning_rates = [0.2,0.4,0.6]
Weights = np.random.randn(3)
for learning_rate in learning_rates:
    trained_W = train(learning_rate,Weights)

test(X, trained_W, T)

while(1):
    inputx(trained_W)

