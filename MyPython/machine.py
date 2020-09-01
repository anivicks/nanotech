import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

x = np.arange(5, 20)
y = np.exp(x/3.0)
f = interpolate.interp1d(x,y)
x1 = np.arange(6, 12)
y1 = f(x1)
plt.plot(x, y, 'o', x1, y1, '--')
plt.show()

# plt.plot([1, 2, 3])
# plt.ylabel('some numbers')
# plt.show()