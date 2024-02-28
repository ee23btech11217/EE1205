import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 40
L = 5
C = 80e-6

# Define a range of frequencies
omega = np.linspace(0, 100, 100)  # You can adjust the range and number of points as needed

# Calculate the modulus of Z for each frequency
modulus_Z = np.sqrt(R**2 + (1 - (omega)**2 * L * C)**2)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(omega, modulus_Z, label='|Z|')
plt.scatter(50, 40)
plt.text(50, 40, '(50, 40)', verticalalignment='bottom', horizontalalignment='right')  # Add text at (50, 40)
plt.title('Impedance vs Frequency')
plt.xlabel('Frequency ($\omega$)')
plt.ylabel('|Z|')
plt.grid(True)
plt.yscale('log')
plt.legend()
plt.savefig("../figs/impedance.png")
plt.show()
