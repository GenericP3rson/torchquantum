import torchquantum as tq
import qiskit 
from qiskit import Aer, execute

from torchquantum.util import (
    switch_little_big_endian_matrix,
    find_global_phase,
)

from qiskit.circuit.library import GR, GRX, GRY
import numpy as np

all_pairs = [
    # {"qiskit": GR, "tq": tq.layer.GlobalR},
    {"qiskit": GRX, "tq": tq.layer.GlobalRX},
    {"qiskit": GRY, "tq": tq.layer.GlobalRY},
]

for pair in all_pairs:
    num_wires = 2

    # create the qiskit circuit
    qiskit_circuit = pair["qiskit"](num_wires, np.pi/4) #, np.pi/2)

    # get the unitary from qiskit
    backend = Aer.get_backend('unitary_simulator')
    result = execute(qiskit_circuit, backend).result()
    unitary_qiskit = result.get_unitary(qiskit_circuit)

    # create tq circuit
    qdev = tq.QuantumDevice(num_wires)
    tq_circuit = pair["tq"](num_wires, np.pi/4) #, np.pi/2)
    tq_circuit(qdev)

    # get the unitary from tq
    unitary_tq = tq_circuit.get_unitary(qdev)
    unitary_tq = switch_little_big_endian_matrix(unitary_tq.data.numpy())

    # phase?
    phase = find_global_phase(unitary_tq, unitary_qiskit, 1e-4)

    print(unitary_tq*phase)
    print(unitary_qiskit)
    print(np.allclose(unitary_tq*phase, unitary_qiskit, atol=1e-6))
    assert np.allclose(unitary_tq*phase, unitary_qiskit, atol=1e-6), f"{pair} not equal!"
