from ..op_types import DiagonalOperation, Operation
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class T(DiagonalOperation, metaclass=ABCMeta):
    """Class for T Gate."""

    name = "t"
    num_params = 0
    num_wires = 1
    eigvals = torch.tensor([1, 1j], dtype=C_DTYPE)
    matrix = mat_dict["t"]
    func = staticmethod(tqf.t)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix

    @classmethod
    def _eigvals(cls, params):
        return cls.eigvals


class TDG(Operation, metaclass=ABCMeta):
    """Class for TDG Gate."""

    num_params = 0
    num_wires = 1
    matrix = mat_dict["tdg"]
    func = staticmethod(tqf.tdg)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix
