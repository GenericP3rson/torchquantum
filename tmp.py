from qiskit.circuit.library import GR
from qiskit import Aer, execute
import numpy as np

## TODO: SOMEWHAT REVERSE-ENGINEER THE GATE!!

circuit = GR(num_qubits=3, theta=np.pi, phi=0)

backend = Aer.get_backend('unitary_simulator')
result = execute(circuit, backend).result()
unitary_qiskit = result.get_unitary(circuit)

# print(unitary_qiskit)

for row in unitary_qiskit:
    print(row)

