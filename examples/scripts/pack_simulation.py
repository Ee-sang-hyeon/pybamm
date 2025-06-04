"""
Example showing how to simulate a battery pack by modifying the number of
cells in series and electrodes in parallel.
"""

import pybamm

pybamm.set_logging_level("INFO")

# Load the SPMe model
model = pybamm.lithium_ion.SPMe()

# Load default parameter values and update pack configuration
param = model.default_parameter_values
param.update(
    {
        "Number of cells connected in series to make a battery": 4,
        "Number of electrodes connected in parallel to make a cell": 3,
    }
)

# Create and solve the simulation
sim = pybamm.Simulation(model, parameter_values=param)
solution = sim.solve([0, 3600])

# Plot the pack voltage
sim.plot(["Battery voltage [V]"])

