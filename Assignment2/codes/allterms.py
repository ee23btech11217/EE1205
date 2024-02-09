import numpy as np
import matplotlib.pyplot as plt

# Load the data from 'values.dat'
data = np.loadtxt('values.dat')
n = data[:, 0].astype(int)  # n values as integers
xn = data[:, 1]  # x(n) values as floats

# Plotting
plt.stem(n, xn, basefmt=" ")
plt.xlabel('n')
plt.ylabel('$x(n)$')
plt.savefig('plot.png', dpi = 300, bbox_inches = 'tight')
