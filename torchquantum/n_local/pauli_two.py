import torch
from .two_local import TwoLocal

class PauliTwo(TwoLocal):
    def __init__(self, rotation_circuit, n_wires_rotation, entanglement_circuit, n_wires_entanglement, n_wires, reps, seed=0):
        torch.manual_seed(seed)
        super().__init__(rotation_circuit, n_wires_rotation, entanglement_circuit, n_wires_entanglement, n_wires, reps)

    def build_rotation_layer(self):
        """
        Adds the rotation layer
        """
        all_rotation_operations = []

        # go by blocks
        for i in range(self.n_wires):
            # randomly add a rx, ry, rz
            all_rotation_operations.append({"name": ["rx", "ry", "rz"][torch.randint(0, 3)], "wires": i, "trainable": True})

        # return a quantum module
        return tq.QuantumModule.from_op_history(all_rotation_operations)

    def build_circuit(self, qdev):
        """
        Build out the circuit itself
        """
        # start by adding rx
        for wire in self.n_wires:
            qdev.ry(torch.pi / 4, wires=wire)

        # create the entanglement module
        entanglement_module = self.build_entanglement_layer()

        # add a rotation and entanglement for each rep
        for _ in self.reps:
            self.build_rotation_layer()(qdev)
            entanglement_module(qdev)

        # add one extra rotation layer
        self.build_rotation_layer()(qdev)

        # return the device
        return qdev
