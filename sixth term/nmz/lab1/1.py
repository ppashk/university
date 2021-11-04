import matplotlib.pyplot as plt
import numpy as np
x = np.array([[2, 1], [3, -2], [-4, 5], [-4, -1], [-1, -2], [3, 4], [-4, 1], [-3, -3], [1, 3], [-2, 2]])
for x1, x2 in x:
    z = (1 / (1 + np.exp(x2)))
    if z > 0.5:
        print("1 and 2 = (", x1, ";", x2, ")")
        plt.scatter(x1, x2, c='r')
    elif z < 0.5:
        print("3 and 4 = (", x1, ";", x2, ")")
        plt.scatter(x1, x2, c='b')

 
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
