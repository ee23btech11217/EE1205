import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
frequency = 50  # Frequency in Hz
omega = 2 * np.pi * frequency  # Angular frequency
t = np.linspace(0, 0.1, 1000)  # Time vector from 0 to 0.1 seconds

# Define the voltage function
V = 230 * np.sqrt(2) * np.exp(1j * omega * t)

# Plot the real and imaginary parts
plt.figure(figsize=(10, 6))
plt.plot(t, V.real, label='Input voltage')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Input Voltage vs Time (50 Hz)')
plt.legend()
plt.grid(True)
plt.show()

