#install matplotlib

import matplotlib.pyplot as plt

left  = [1, 2, 3, 4, 5]
height = [10, 20, 30, 90, 50]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['blue', 'orange'])

plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.title('Bar Chart')

plt.legend()

plt.show()