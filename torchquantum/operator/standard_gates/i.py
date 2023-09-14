from ..op_types import Observable
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class I(Observable, metaclass=ABCMeta):
    """Class for Identity Gate."""

    name = "i"
    num_params = 0
    num_wires = 1
    eigvals = torch.tensor([1, 1], dtype=C_DTYPE)
    matrix = mat_dict["i"]
    func = staticmethod(tqf.i)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix

    @classmethod
    def _eigvals(cls, params):
        return cls.eigvals

    def diagonalizing_gates(self):
        return []
