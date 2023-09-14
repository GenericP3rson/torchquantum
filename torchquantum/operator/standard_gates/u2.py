from ..op_types import Observable, Operation
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class U2(Operation, metaclass=ABCMeta):
    """Class for U2 gate."""

    name = "u2"
    num_params = 2
    num_wires = 1
    func = staticmethod(tqf.u2)

    @classmethod
    def _matrix(cls, params):
        return tqf.u2_matrix(params)


class CU2(Operation, metaclass=ABCMeta):
    """Class for controlled U2 gate."""

    name = "cu2"
    num_params = 2
    num_wires = 2
    func = staticmethod(tqf.cu2)

    @classmethod
    def _matrix(cls, params):
        return tqf.cu2_matrix(params)
