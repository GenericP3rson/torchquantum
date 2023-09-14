from ..op_types import Operation
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class SWAP(Operation, metaclass=ABCMeta):
    """Class for SWAP Gate."""

    name = "swap"
    num_params = 0
    num_wires = 2
    matrix = mat_dict["swap"]
    func = staticmethod(tqf.swap)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix


class SSWAP(Operation, metaclass=ABCMeta):
    """Class for SSWAP Gate."""

    name = "sswap"
    num_params = 0
    num_wires = 2
    matrix = mat_dict["sswap"]
    func = staticmethod(tqf.sswap)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix


class CSWAP(Operation, metaclass=ABCMeta):
    """Class for CSWAP Gate."""

    name = "cswap"
    num_params = 0
    num_wires = 3
    matrix = mat_dict["cswap"]
    func = staticmethod(tqf.cswap)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix
