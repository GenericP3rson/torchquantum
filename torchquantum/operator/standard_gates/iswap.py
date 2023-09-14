from ..op_types import Operation
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class ISWAP(Operation, metaclass=ABCMeta):
    """Class for ISWAP Gate."""

    name = "iswap"
    num_params = 0
    num_wires = 2
    matrix = mat_dict["iswap"]
    func = staticmethod(tqf.iswap)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix
