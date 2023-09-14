from ..op_types import Operation
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class ECR(Operation, metaclass=ABCMeta):
    """Class for Echoed Cross Resonance Gate."""

    name = "ecr"
    num_params = 0
    num_wires = 2
    matrix = mat_dict["ecr"]
    func = staticmethod(tqf.ecr)

    @classmethod
    def _matrix(cls, params):
        return cls.matrix


EchoedCrossResonance = ECR
