from ..op_types import Operator, AnyWires
from abc import ABCMeta
from torchquantum.macro import C_DTYPE
import torchquantum as tq
import torch
from torchquantum.functional import mat_dict
import torchquantum.functional.functionals as tqf


class Reset(Operator, metaclass=ABCMeta):
    """Class for Reset gate."""

    name = "reset"
    num_params = 0
    num_wires = AnyWires
    func = staticmethod(tqf.reset)

    @classmethod
    def _matrix(cls, params):
        return None
