"""The Random Pauli circuit class, adapted from Qiskit."""

from __future__ import annotations
import numpy as np

from torchquantum.devices import QuantumDevice

from .two_local import TwoLocal

class PauliTwoDesign(TwoLocal):
    r"""The Pauli Two-Design ansatz.

    This class implements a particular form of a 2-design circuit [1], which is frequently studied
    in quantum machine learning literature, such as e.g. the investigating of Barren plateaus in
    variational algorithms [2].

    The circuit consists of alternating rotation and entanglement layers with
    an initial layer of :math:`\sqrt{H} = RY(\pi/4)` gates.
    The rotation layers contain single qubit Pauli rotations, where the axis is chosen uniformly
    at random to be X, Y or Z. The entanglement layers is compromised of pairwise CZ gates
    with a total depth of 2.

    For instance, the circuit could look like this (but note that choosing a different seed
    yields different Pauli rotations).

    .. parsed-literal::

             ┌─────────┐┌──────────┐       ░ ┌──────────┐       ░  ┌──────────┐
        q_0: ┤ RY(π/4) ├┤ RZ(θ[0]) ├─■─────░─┤ RY(θ[4]) ├─■─────░──┤ RZ(θ[8]) ├
             ├─────────┤├──────────┤ │     ░ ├──────────┤ │     ░  ├──────────┤
        q_1: ┤ RY(π/4) ├┤ RZ(θ[1]) ├─■──■──░─┤ RY(θ[5]) ├─■──■──░──┤ RX(θ[9]) ├
             ├─────────┤├──────────┤    │  ░ ├──────────┤    │  ░ ┌┴──────────┤
        q_2: ┤ RY(π/4) ├┤ RX(θ[2]) ├─■──■──░─┤ RY(θ[6]) ├─■──■──░─┤ RX(θ[10]) ├
             ├─────────┤├──────────┤ │     ░ ├──────────┤ │     ░ ├───────────┤
        q_3: ┤ RY(π/4) ├┤ RZ(θ[3]) ├─■─────░─┤ RX(θ[7]) ├─■─────░─┤ RY(θ[11]) ├
             └─────────┘└──────────┘       ░ └──────────┘       ░ └───────────┘

    References:

        [1]: Nakata et al., Unitary 2-designs from random X- and Z-diagonal unitaries.
            `arXiv:1502.07514 <https://arxiv.org/pdf/1502.07514.pdf>`_

        [2]: McClean et al., Barren plateaus in quantum neural network training landscapes.
             `arXiv:1803.11173 <https://arxiv.org/pdf/1803.11173.pdf>`_
    """

    def __init__(
        self,
        num_qubits: int | None = None,
        reps: int = 3,
        seed: int | None = None,
        insert_barriers: bool = False,
        name: str = "PauliTwoDesign",
    ):
        from torchquantum.operators import RY # pylint: disable=cyclic-import

        # store a random number generator
        self._seed = seed
        self._rng = np.random.default_rng(seed)

        # store a dict to keep track of the random gates
        self._gates: dict[int, list[str]] = {}

        super().__init__(
            num_qubits,
            reps=reps,
            entanglement_blocks="cz",
            entanglement="pairwise",
            insert_barriers=insert_barriers,
            name=name,
        )

        # set the initial layer
        self._prepended_blocks = [RY(np.pi / 4)]
        self._prepended_entanglement = ["linear"]

    def _invalidate(self):
        """Invalidate the circuit and reset the random number."""
        self._rng = np.random.default_rng(self._seed)  # reset number generator
        super()._invalidate()

    def _build_rotation_layer(self, circuit, param_iter, i):
        """Build a rotation layer."""

        # TODO: how to import previous circuit to here
        layer = QuantumDevice(self.num_qubits) # QuantumCircuit(*self.qregs)
        qubits = range(self.num_qubits)

        # if no gates for this layer were generated, generate them
        if i not in self._gates.keys():
            self._gates[i] = list(self._rng.choice(["rx", "ry", "rz"], self.num_qubits))
        # if not enough gates exist, add more
        elif len(self._gates[i]) < self.num_qubits:
            num_missing = self.num_qubits - len(self._gates[i])
            self._gates[i] += list(self._rng.choice(["rx", "ry", "rz"], num_missing))

        for j in qubits:
            getattr(layer, self._gates[i][j])(next(param_iter), j)

        # add the layer to the circuit
        circuit.compose(layer, inplace=True)

    @property
    def num_parameters_settable(self) -> int:
        """Return the number of settable parameters.

        Returns:
            The number of possibly distinct parameters.
        """
        return (self.reps + 1) * self.num_qubits
