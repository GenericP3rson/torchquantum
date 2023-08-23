"""
An attempt at nlocal
"""

import torchquantum as tq
from .two_local import TwoLocal

class ExcitationPreserving(TwoLocal):
    """
    WIP ExcitationPreserving circuit
    """
    def __init__(self, rotation_circuit, n_wires_rotation, entanglement_circuit, n_wires_entanglement, n_wires, reps):
        super().__init__([{"name": "rz", "wires": 0, "trainable": True}], 1, [{"name": "rxx", "wires": [0, 1], "trainable": True}], 2, n_wires, reps)

