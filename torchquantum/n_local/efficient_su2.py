"""
An attempt at nlocal
"""

import torchquantum as tq
from .two_local import TwoLocal

class EfficientSU2(TwoLocal):
    """
    WIP TwoLocal circuit
    """
    def __init__(self, rotation_circuit, n_wires_rotation, entanglement_circuit, n_wires_entanglement, n_wires, reps):
        super().__init__([{"name": "ry", "wires": 0, "trainable": True}, {"name": "rz", "wires": 0, "trainable": True}], 1, [{"name": "cx", "wires": [0, 1]}], 2, n_wires, reps)

