from ..op_types import *
import torch
import torch.nn as nn
import torchquantum as tq
import torchquantum.functional.functionals as tqf
import numpy as np
from abc import ABCMeta
from torchquantum.macro import C_DTYPE, F_DTYPE
from torchquantum.functional import mat_dict


class Hadamard(Observable, metaclass=ABCMeta):
    """Class for Hadamard Gate."""

    name = "hadamard"
    num_params = 0
    num_wires = 1
    eigvals = torch.tensor([1, -1], dtype=C_DTYPE)
    matrix = mat_dict["hadamard"]
    func = staticmethod(tqf.hadamard)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix

    @classmethod
    def _eigvals(cls, params):
        return cls.eigvals

    def diagonalizing_gates(self):
        return [tq.RY(has_params=True, trainable=False, init_params=-np.pi / 4)]


class SHadamard(Operation, metaclass=ABCMeta):
    """Class for SHadamard Gate."""

    name = "shadamard"
    num_params = 0
    num_wires = 1
    matrix = mat_dict["shadamard"]
    func = staticmethod(tqf.shadamard)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix


class CHadamard(Operation, metaclass=ABCMeta):
    """Class for CHadamard Gate."""

    name = "chadmard"
    num_params = 0
    num_wires = 2
    matrix = mat_dict["chadamard"]
    func = staticmethod(tqf.chadamard)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix


H = Hadamard
SH = SHadamard
CH = CHadamard
