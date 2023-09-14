from ..op_types import Operation
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class RY(Operation, metaclass=ABCMeta):
    """Class for RY Gate."""

    name = "ry"
    num_params = 1
    num_wires = 1
    func = staticmethod(tqf.ry)

    @classmethod
    def _matrix(cls, params):
        return tqf.ry_matrix(params)


class RYY(Operation, metaclass=ABCMeta):
    """Class for RYY Gate."""

    name = "ryy"
    num_params = 1
    num_wires = 2
    func = staticmethod(tqf.ryy)

    @classmethod
    def _matrix(cls, params):
        return tqf.ryy_matrix(params)


class CRY(Operation, metaclass=ABCMeta):
    """Class for Controlled Rotation Y gate."""

    name = "cry"
    num_params = 1
    num_wires = 2
    func = staticmethod(tqf.cry)

    @classmethod
    def _matrix(cls, params):
        return tqf.cry_matrix(params)
