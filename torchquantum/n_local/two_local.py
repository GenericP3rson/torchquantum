"""
An attempt at nlocal
"""

import torchquantum as tq
from .n_local import NLocal

class TwoLocal(NLocal):
    """
    WIP TwoLocal circuit
    """
    def __init__(self, rotation_circuit, n_wires_rotation, entanglement_circuit, n_wires_entanglement, n_wires, reps):
        super().__init__(rotation_circuit, n_wires_rotation, entanglement_circuit, n_wires_entanglement, n_wires, reps)

