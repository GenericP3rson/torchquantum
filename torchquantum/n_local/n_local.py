"""
An attempt at nlocal
"""

import torchquantum as tq

class NLocal():
    """
    WIP NLocal circuit

    Inputs: 
    - Operations list of rotation_circuit
    - n_wires_rotation of rotation_circuit
    - Operations list of entanglement_circuit
    - n_wires_entanglement of entanglement_circuit
    - n_wires: total number of wires in the circuit
    - reps: number of repetitions of the circuit
    """
    def __init__(self, rotation_circuit, n_wires_rotation, entanglement_circuit, n_wires_entanglement, n_wires, reps):
        self.rotation_circuit = rotation_circuit
        self.n_wires_rotation = n_wires_rotation
        self.entanglement_circuit = entanglement_circuit
        self.n_wires_entanglement = n_wires_entanglement
        self.n_wires = n_wires
        self.reps = reps
    
    def build_rotation_layer(self):
        """
        Adds the rotation layer
        """
        all_rotation_operations = []

        # create deep copy of rotation circuit
        rotation_circuit = self.rotation_circuit.copy()

        # go by blocks
        for _ in range(0, self.n_wires, self.n_wires_rotation):

            # iterate through the operations and add the offset to all the wires
            for op in rotation_circuit:
                op.wires = op.wires + self.n_wires_rotation 
            
            # add list of operations
            all_rotation_operations = all_rotation_operations + rotation_circuit
        
        # return a quantum module
        return tq.QuantumModule.from_op_history(all_rotation_operations)

    def build_entanglement_layer(self):
        """
        Adds an entanglement layer
        """
        all_entanglement_operations = []

        # create deep copy of entangelement circuit
        entanglement_circuit = self.entanglement_circuit.copy()

        for _ in range(self.n_wires-self.n_wires_entanglement+1):
            
            for op in entanglement_circuit:
                op.wires = op.wires + 1
            
            all_entanglement_operations = all_entanglement_operations + entanglement_circuit

        return tq.QuantumModule.from_op_history(all_entanglement_operations)

    def build_circuit(self, qdev):
        """
        Build out the circuit itself
        """
        rotation_module = self.build_rotation_layer()
        entanglement_module = self.build_entanglement_layer()
        for _ in self.reps:
            rotation_module(qdev)
            entanglement_module(qdev)
        rotation_module(qdev)
        return qdev
        



