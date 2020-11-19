# bring in necessary modules
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram


# number of quantum bits 
n_qbits = 8

# number of classical bits
n_bits = 8 

# create the quantum circuit
circuit = QuantumCircuit(n_qbits, n_bits)

# loop through and measure each qbit into the classical bits
for i in range(8): 
    # NOTE: measure(qbit, outbit) measures result of qbit into outbit, can use ints since these are indexable in our circuit
    circuit.measure(i, i)

print(circuit.draw())


# execute circuit and save the observed results
# NOTE: qasm_simulator stands for quantum assembly language
# NOTE: get_backend is the environment you'd like to execute in 
observations = execute(circuit, Aer.get_backend('qasm_simulator')).result().get_counts()


print(plot_histogram(observations))



