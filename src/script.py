import numpy as np
import matplotlib.pyplot as plt

print('Hello, World!')
a = np.array([1, 2, 3])
print(a)

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# https://matplotlib.org/3.5.0/gallery/lines_bars_and_markers/simple_plot.html
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

print('displaying simple plot')
fig
