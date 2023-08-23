import torchquantum as tq

from torchquantum.algorithm import Hamiltonian
import numpy as np

from qiskit.circuit.library import RealAmplitudes, PauliTwoDesign, EfficientSU2, ExcitationPreserving
from torchquantum.plugin import tq2qiskit, qiskit2tq

def test_circuits(circuit_data, tq_history):
    assert len(circuit_data) == len(tq_history)

    for op, gate in zip(tq_history, circuit_data):
        assert op["name"] == gate[0].name
        assert op["wires"] == list(map(lambda x: x.index, gate[1]))

# TODO: HOW TO TEST NLOCAL AND TWOLOCAL

def test_paulitwodesign():
    # create TQ circuit
    qdev = tq.QuantumDevice(n_wires=4, record_op=True)
    tq_circuit = tq.nlocal.PauliTwoDesign(arch={'n_wires': 4, 'reps': 2})
    for lyr in tq_circuit.layers_all:
        tq_circuit(qdev)

    # create qiskit circuit
    circuit = PauliTwoDesign(4, reps=2)
    circuit_data = circuit.decompose().data

    # test
    test_circuits(circuit_data, qdev.op_history)

def test_realamplitudes():
    # create TQ circuit
    qdev = tq.QuantumDevice(n_wires=4, record_op=True)
    tq_circuit = tq.nlocal.RealAmplitudes(arch={'n_wires': 4, 'reps': 2})
    for lyr in tq_circuit.layers_all:
        tq_circuit(qdev)

    # create qiskit circuit
    circuit = RealAmplitudes(4, reps=2)
    circuit_data = circuit.decompose().data

    # test
    test_circuits(circuit_data, qdev.op_history)

def test_efficientsu2():
    # create TQ circuit
    qdev = tq.QuantumDevice(n_wires=4, record_op=True)
    tq_circuit = tq.nlocal.EfficientSU2(arch={'n_wires': 4, 'reps': 2})
    for lyr in tq_circuit.layers_all:
        tq_circuit(qdev)

    # create qiskit circuit
    circuit = EfficientSU2(4, reps=2)
    circuit_data = circuit.decompose().data

    # test
    test_circuits(circuit_data, qdev.op_history)

def test_excitationpreserving():
    # create TQ circuit
    qdev = tq.QuantumDevice(n_wires=4, record_op=True)
    tq_circuit = tq.nlocal.ExcitationPreserving(arch={'n_wires': 4, 'reps': 2})
    for lyr in tq_circuit.layers_all:
        tq_circuit(qdev)

    # create qiskit circuit
    circuit = ExcitationPreserving(4, reps=2)
    circuit_data = circuit.decompose().data

    # test
    test_circuits(circuit_data, qdev.op_history)
