#install matplotlib

import matplotlib.pyplot as plt

x1  = [2, 4, 5, 6]
y1 = [2, 3, 6, 7]

plt.plot(x1, y1, label =  'Line 1')

x2 = [2, 5, 7, 9]
y2 = [4, 3, 5, 8]

plt.plot(x2, y2, label =  'Line 1')


plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.title('Calculus of multivariable functions -  Two lines')

plt.legend()

plt.show()