import matplotlib.pyplot as plt
from random import uniform, randint
from random import normalvariate

#profits = 1,−1−1,1−1,1 1,−1

#bilief(
alpha = 0.9
ts_length = 200
current_x = 0

x_values = []
for t in range(ts_length):
    x_values.append(current_x)
    a = uniform(0, 1)
    current_x = current_x + (a - current_x)/(t+2)  
plt.plot(x_values, 'b-')

plt.show()