from ..op_types import DiagonalOperation
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class PhaseShift(DiagonalOperation, metaclass=ABCMeta):
    """Class for PhaseShift Gate."""

    name = "phaseshift"
    num_params = 1
    num_wires = 1
    func = staticmethod(tqf.phaseshift)

    @classmethod
    def _matrix(cls, params):
        return tqf.phaseshift_matrix(params)
