#-*- encoding=UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

x = np.linspace(1, 10, 100)

print x

plt.interactive(False)

plt.plot(x, np.sin(x), 'r--')
plt.show()