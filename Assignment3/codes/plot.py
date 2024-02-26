import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 40
L = 5
C = 80e-6

# Define a range of frequencies
frequencies = np.linspace(0, 10, 1000)  # You can adjust the range and number of points as needed

# Calculate the modulus of Z for each frequency
modulus_Z = np.sqrt(R**2 + (1 - (2 * np.pi * frequencies)**2 * L * C)**2)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(frequencies, modulus_Z, label='|Z|')
plt.title('Impedance vs Frequency')
plt.xlabel('Frequency (f)')
plt.ylabel('|Z|')
plt.grid(True)
plt.yscale('log')
plt.legend()
plt.savefig("../figs/impedance.png")
plt.show()
