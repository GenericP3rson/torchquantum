from ..op_types import *
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class PauliX(Observable, metaclass=ABCMeta):
    """Class for Pauli X Gate."""

    name = "paulix"
    num_params = 0
    num_wires = 1
    eigvals = torch.tensor([1, -1], dtype=C_DTYPE)
    matrix = mat_dict["paulix"]
    func = staticmethod(tqf.paulix)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix

    @classmethod
    def _eigvals(cls, params):
        return cls.eigvals

    def diagonalizing_gates(self):
        return [tq.Hadamard()]


class CNOT(Operation, metaclass=ABCMeta):
    """Class for CNOT Gate."""

    name = "cnot"
    num_params = 0
    num_wires = 2
    matrix = mat_dict["cnot"]
    func = staticmethod(tqf.cnot)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix


class C4X(Operation, metaclass=ABCMeta):
    """Class for C4X Gate."""

    name = "c4x"
    num_params = 0
    num_wires = 5
    matrix = mat_dict["c4x"]
    func = staticmethod(tqf.c4x)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix


class C3X(Operation, metaclass=ABCMeta):
    """Class for C3X gate."""

    name = "c3x"
    num_params = 0
    num_wires = 4
    matrix = mat_dict["c3x"]
    func = staticmethod(tqf.c3x)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix


class DCX(Operation, metaclass=ABCMeta):
    """Class for DCX Gate."""

    name = "dcx"
    num_params = 0
    num_wires = 2
    matrix = mat_dict["dcx"]
    func = staticmethod(tqf.dcx)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix


class MultiCNOT(Operation, metaclass=ABCMeta):
    """Class for Multi qubit CNOT gate."""

    name = "multicnot"
    num_params = 0
    num_wires = AnyWires
    func = staticmethod(tqf.multicnot)

    @classmethod
    def _matrix(cls, params, n_wires):
        return tqf.multicnot_matrix(n_wires)

    @property
    def matrix(self):
        op_matrix = self._matrix(self.params, self.n_wires)
        return op_matrix


class MultiXCNOT(Operation, metaclass=ABCMeta):
    """Class for Multi qubit XCNOT gate."""

    name = "multixcnot"
    num_params = 0
    num_wires = AnyWires
    func = staticmethod(tqf.multixcnot)

    @classmethod
    def _matrix(cls, params, n_wires):
        return tqf.multixcnot_matrix(n_wires)

    @property
    def matrix(self):
        op_matrix = self._matrix(self.params, self.n_wires)
        return op_matrix
