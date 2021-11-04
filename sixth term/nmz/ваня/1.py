import random as r

def neuron(x, w, w0=0):
    temp = w0
    for i in range(len(w)):
        temp += x[i] * w[i]
    if temp >= 0:
        y = 1
    else:
        y = 0
    return y


# Коефіцієнт швидкості навчання
a = 0.4
# К-сть варіантів виводу і к-сть вхідних образів
M = 8
# К-сть входів одного нейрона
N = 9
# К-сть нейронів
K = 4

# Ваги ядер нейронів
w0 = [r.uniform(-0.1, 0.1) for k in range(K)]
W = [[r.uniform(-0.1, 0.1) for n in range(N)] for k in range(K)]

flag = True
i = 0
while flag:
    i += 1
    errors = 0
    # Подаємо на вхід образи
    for j in range(M):
        # Очікуваний вивід (еталон)
        d = out[j]
        y_array = []
        # Знаходимо вивід кожного нейрона
        for k in range(K):
            y = neuron(X[j], W[k], w0[k])
            y_array.append(y)
            # Якщо вивід не збігається з еталонним
            if y != d[k]:
                errors += 1
                # Знаходимо різницю між еталоном та нашим виводом
                b = d[k] - y
                # Змінюємо поріг поточного нейрона
                w0[k] += a * b
                # Модифікуємо ваги поточного нейрона за дельта правилом
                for v in range(N):
                    W[k][v] += a * X[j][v] * b

        print('Очікуваний результат: ' + str(d))
        print('Нейрон: ' + str(y_array) + '\n')

    print('Кількість ошибок в епосі #%i: %i' % (i, errors),"\n")
    print("************************************","\n")
    if errors == 0 or i > 1000:
        flag = False

y = []
print("Введіть вхідний об'єкт:")
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])

for k in range(K):
    y.append(neuron(A, W[k]))

try:
    out.index(y)
except ValueError:
    print(y)
finally:
    print('Цифра:  '+str(out.index(y)+1))