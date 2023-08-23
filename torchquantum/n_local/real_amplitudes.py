from .two_local import TwoLocal

class RealAmplitudes(TwoLocal):
    def __init__(self, n_wires, reps):
        super().__init__([{"name": "ry", wires: 0, trainable: True}], 1, [{"name": "cx", wires: [0, 1]}], 2, n_wires, reps)

