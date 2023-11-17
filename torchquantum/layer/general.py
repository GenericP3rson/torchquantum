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
from torchquantum.operator.operators import R

__all__ = [
    "GlobalR",
    "GlobalRX",
    "GlobalRY",
]


class GlobalR(tq.QuantumModule):
    """Layer Template for a Global R General Gate"""

    def __init__(
        self,
        n_wires: int = 0,
        theta: float = 0,
        phi: float = 0,
    ):
        """Create the layer"""
        super().__init__()
        self.ops_all = tq.QuantumModuleList()
        self.n_wires = n_wires
        self.params = torch.tensor([[theta, phi]])
        for k in range(self.n_wires):
            self.ops_all.append(R(has_params=True, trainable=True))

    @tq.static_support
    def forward(self, q_device, x=None):
        for k in range(self.n_wires):
            R()(q_device, wires=k, params=self.params)


class GlobalRX(GlobalR):
    """Layer Template for a Global RX General Gate"""

    def __init__(
        self,
        n_wires: int = 0,
        theta: float = 0,
    ):
        """Create the layer"""
        super().__init__(n_wires, theta, phi=0)


class GlobalRY(GlobalR):
    """Layer Template for a Global RY General Gate"""

    def __init__(
        self,
        n_wires: int = 0,
        theta: float = 0,
    ):
        """Create the layer"""
        super().__init__(n_wires, theta, phi=torch.pi / 2)

if __name__ == "__main__":
    print(Rot(has_params=True, init_params=[3, 3, 0]))
