import matplotlib.pyplot as plt
import re
import math
import numpy as np


def find_numbers(Str):
    list_numb = re.findall(r'\d+', Str)
    c = int(list_numb[0])
    d = int(list_numb[1])
    return c, d


def b_function(x):

    if x == 5:
        b = 2.8
    elif x == 15:
        b = 6.48
    elif x == 25:
        b = 6.75
    elif x == 50:
        b = 24
    elif x < 10:
        b = x * 0.46
    elif x % 10 == 0:
        b = (0.357 - 0.00163) * x
    elif x % 5 == 0:
        b = (0.213 - 0.00067 * x) * x
    else:
        b = 0.5 * (b_function(x//10*10 + 5) + b_function(x % 10))
    return b


def find_b(T):
    if T >= 100:
        Tt = list(str(T))
        rq = 0
        q = 0
        qt = 0
        for qt, rqt in reversed(list(enumerate(Tt))):
            if rqt != '0':
                q = len(Tt) - qt
                rq = int(rqt)
                break
        rq1 = int(Tt[qt - 1])
        d = q % 3
        if d == 0:
            x = rq * 10
            b = b_function(x) * pow(10, q - 2)
        elif d == 1:
            if rq1 == 0:
                x = rq
                b = b_function(x) * pow(10, q - 1)
            else:
                x = rq1 * 10 + rq
                b = b_function(x) * pow(10, q - 1)
        else:
            if rq1 == 0:
                x = rq * 10
                b = b_function(x) * pow(10, q - 2)
            else:
                x = rq1 * 10 + rq
                b = b_function(x) * pow(10, q - 1)
    else:
        b = b_function(T)
    return b


def find_on(X, Y):
    xt = 0
    for i in range(len(Y)):
        if Y[i] >= 0.01:
            xt = X[i]
            break
    xt1 = 0
    for i in reversed(range(len(Y))):
        if Y[i] > 0.01:
            xt1 = X[i]
            break
    return xt, xt1


def find_on_one(X,Y):
    xt = 0
    for i in range(len(Y)):
        if Y[i] > 0:
            xt = X[i-1]
            break
    xt1 = 0
    for i in reversed(range(len(Y))):
        if Y[i] > 0:
            xt1 = X[i+1]
            break
    return xt, xt1


def build_gauss(c, d, ax, fig):
    ac = -4 * math.log(0.5, math.e) / pow(find_b(c), 2)
    ad = -4 * math.log(0.5, math.e) / pow(find_b(d), 2)
    X = np.arange(0, d+d/2, 0.1)
    Y = []
    for x in X:
        if x < c:
            Y.append(pow(math.e,-1*ac*(x-c)*(x-c)))
        elif c <= x <= d:
            Y.append(1)
        else:
            Y.append(pow(math.e, -1*ad*(x-d)*(x-d)))

    ax[0, 0].plot(X, Y, c-find_b(c)/2, 0.5, 'or', d+find_b(d)/2, 0.5, 'or')
    ax[0, 0].set_title('Гаусс:\n')
    ''' 
    +'                             | exp('+str("%.2f"%(-1*ac))+'x - ' + str(c) +')'+ r'$x^{2}$'+ ',x < '+str(c)+')\n'
                      +r'$\mu$'+ '(x) = < 1,' + str(c) + " <= x <=" + str(d) + '\n'
                      +'                             | exp('+str("%.2f"%(-1*ad))+'x - ' + str(d) +')'+ r'$x^{2}$'+ ',x < '+str(d)+')\n')
                      '''
    xt, xt1 = find_on(X, Y)
    ax[0, 0].set(ylabel='\u03BC(x)', xlabel='x')
    ax[0, 0].annotate(str("%.2f" % (c - find_b(c) / 2)) + ', ' + str(0.5), xy=(c - find_b(c) / 2, 0.5), xytext=(c - find_b(c) / 2+d/10, 0.5))
    ax[0, 0].annotate(str("%.2f" % (d + find_b(d) / 2)) + ', ' + str(0.5), xy=(d + find_b(d) / 2, 0.5), xytext=(d + find_b(d) / 2+d/10, 0.5))
    ax[0, 0].grid()
    ax[1, 0].plot([c - xt, c, d, d +xt1], [0, 1, 1, 0])
    ax[1, 0].set_title(str('A'+u'\u0342')+' = ('+str(c)+', '+str(d)+', '+str("%.2f" % (c-xt))+', '+str("%.2f" % (xt1-d))+')')
    ax[1, 0].set(ylabel='\u03BC(x)', xlabel='x')
    ax[1, 0].grid()


def find_ab(c, d):
    x1 = c - find_b(c) / 2
    y1 = 0.5
    x2 = c
    y2 = 1
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k*x2
    xcO = -b/k
    x2 = d + find_b(d)/2
    y2 = 0.5
    x1 = d
    y1 = 1
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    xdO = -b/k
    return xcO, xdO


def build_trapeze(c, d, ax, fig):
    a, b = find_ab(c, d)
    X = np.arange(0, d + d/2, 0.1)
    Y = []
    for x in X:
        if x < a:
            Y.append(0)
        elif a <= x <= c:
            Y.append((x-a)/(c-a))
        elif c <= x <= d:
            Y.append(1)
        elif d <= x <= b:
            Y.append((b-x)/(b-d))
        else:
            Y.append(0)
    ax[0, 1].plot(X, Y, c-find_b(c)/2, 0.5, 'or', d + find_b(d)/2, 0.5, 'or')
    ax[0, 1].set_title('Трапеція:\n')
    ''' +'| 0 '+',x < '+str("%.2f" % a)+')\n'
                      '                                  | (x - ' + str("%.2f" % a) + ')/('+str("%.2f" % (c-a))+'), ' + str("%.2f" % a) + '<= x <=' + str(c) + '\n'
                       + r'$\mu$' + '(x) =       <'+' 1 ,' + str("%.2f" % c) +'<= x <= '+str("%.2f" % d)+')\n'
                       +'                                            | (' + str("%.2f" % b) + '- x)/('+str("%.2f" % (b-d)) + '), '+ str("%.2f" % d) +'<= x <=' + str("%.2f" % b) + '\n' +
                      '  | 0 ' + ',x > ' + str("%.2f" % b) + ')')'''
    xt, xt1 = find_on_one(X, Y)
    ax[0, 1].set(ylabel='\u03BC(x)', xlabel='x')
    ax[0, 1].grid()
    ax[0, 1].annotate(str("%.2f" % (c - find_b(c) / 2)) + ', ' + str(0.5), xy=(c - find_b(c) / 2, 0.5), xytext=(c - find_b(c) / 2+d/10, 0.5))
    ax[0, 1].annotate(str("%.2f" % (d + find_b(d) / 2)) + ', ' + str(0.5), xy=(d + find_b(d) / 2, 0.5), xytext=(d + find_b(d) / 2+d/10, 0.5))
    ax[1, 1].plot([c - xt, c, d, d + xt1], [0, 1, 1, 0])
    ax[1, 1].set_title(str('A'+u'\u0342')+' = (' + str(c) + ', ' + str(d) + ', ' + str("%.2f" % (c-xt)) + ',' + str("%.2f" % (xt1-d)) + ')')
    ax[1, 1].set(ylabel='\u03BC(x)', xlabel='x')
    ax[1, 1].grid()


def input_numbers():
    return input('Input c and d: ')


Str = input_numbers()
c, d = find_numbers(Str)
fig, ax = plt.subplots(2, 2, figsize=(14, 7))
fig.suptitle(Str, fontsize=14)
fig.patch.set_facecolor('lightgray')
build_trapeze(c, d, ax, fig)
build_gauss(c, d, ax, fig)
fig.tight_layout(pad=5.0)
plt.show()