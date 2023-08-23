"""
MIT License

Copyright (c) 2020-present TorchQuantum Authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import torch
import torchquantum as tq
from torchquantum.layer.layers import (
    LayerTemplate0,
    Op1QAllLayer,
    Op2QAllLayer,
    RandomOp1All,
)

class GRLayer(LayerTemplate0):
    def __init__(self, n_wires: int, theta: float, phi: float):
        super().__init__()
        self.n_wires = n_wires
        # self.gate_all = nn.ModuleList()
        gates = []
        for k in range(self.n_wires):
            gates.append({'name': 'r', 'wires': k, 'params': [theta, phi]})
        self.layers_all = tq.QuantumModule.from_op_history(gates)

    def build_layers(self):
        return self.layers_all

class GRXLayer(GRLayer):
    def __init__(self, n_wires: int, theta: float):
        super().__init__(n_wires, theta, phi=0)

class GRYLayer(GRLayer):
    def __init__(self, n_wires: int, theta: float):
        super().__init__(n_wires, theta, phi=torch.pi / 2)

class GRZLayer(LayerTemplate0):
    def __init__(self, n_wires: int, theta: float):
        super().__init__()
        self.n_wires = n_wires
        # self.gate_all = nn.ModuleList()
        gates = []
        for k in range(self.n_wires):
            gates.append({'name': 'rz', 'wires': k, 'params': theta})
        self.layers_all = tq.QuantumModule.from_op_history(gates)

    def build_layers(self):
        return self.layers_all

