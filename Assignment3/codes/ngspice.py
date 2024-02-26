import os
import numpy as np
import matplotlib.pyplot as plt

# Define the NGSpice netlist
ngspice_netlist = """
*Title: case(ii) transient analysis
R1 1 2 100   
L1 2 3 0.5m 
C1 3 0 10u   
V1 1 0 AC 230V 

.AC DEC 10 1Hz 1MegHz 
.END
"""

# Write the netlist to a file
with open("transient_analysis.cir", "w") as file:
    file.write(ngspice_netlist)

# Run NGSpice simulation
command = "ngspice -b transient_analysis.cir"
output = os.popen(command).read()

# Parse the output to extract time and voltage values
time_values = []
voltage_values = []
for line in output.split("\n"):
    if line.strip() and not line.startswith("No"):
        data = line.split()
        if len(data) >= 2:
            try:
                time_values.append(float(data[0]))
                voltage_values.append(float(data[1]))
            except ValueError:
                pass

# Convert time to milliseconds
time_values = np.array(time_values) * 1000  # Convert to milliseconds

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(time_values, voltage_values)
plt.title("Transient Analysis")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.tight_layout()

plt.show()
