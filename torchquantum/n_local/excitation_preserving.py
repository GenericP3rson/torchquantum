"""The ExcitationPreserving 2-local circuit, adapted from Qiskit."""

from typing import Union, Optional, List, Tuple, Callable, Any
from numpy import pi

from torchquantum.devices import QuantumDevice
from torchquantum import QuantumModule
from torchquantum.operators import RZ
from .two_local import TwoLocal


class ExcitationPreserving(TwoLocal):
    r"""The heuristic excitation-preserving wave function ansatz.

    The ``ExcitationPreserving`` circuit preserves the ratio of :math:`|00\rangle`,
    :math:`|01\rangle + |10\rangle` and :math:`|11\rangle` states. To this end, this circuit
    uses two-qubit interactions of the form

    .. math::

        \newcommand{\th}{\theta/2}

        \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & \cos\left(\th\right) & -i\sin\left(\th\right) & 0 \\
        0 & -i\sin\left(\th\right) & \cos\left(\th\right) & 0 \\
        0 & 0 & 0 & e^{-i\phi}
        \end{pmatrix}

    for the mode ``'fsim'`` or with :math:`e^{-i\phi} = 1` for the mode ``'iswap'``.

    Note that other wave functions, such as UCC-ansatzes, are also excitation preserving.
    However these can become complex quickly, while this heuristically motivated circuit follows
    a simpler pattern.

    This trial wave function consists of layers of :math:`Z` rotations with 2-qubit entanglements.
    The entangling is creating using :math:`XX+YY` rotations and optionally a controlled-phase
    gate for the mode ``'fsim'``.

    """

    def __init__(
        self,
        num_qubits: Optional[int] = None,
        mode: str = "iswap",
        entanglement: Union[str, List[List[int]], Callable[[int], List[int]]] = "full",
        reps: int = 3,
        skip_unentangled_qubits: bool = False,
        skip_final_rotation_layer: bool = False,
        parameter_prefix: str = "θ",
        insert_barriers: bool = False,
        initial_state: Optional[Any] = None,
        name: str = "ExcitationPreserving",
        device: str = "cpu",
    ) -> None:
        """Create a new ExcitationPreserving 2-local circuit.

        Args:
            num_qubits: The number of qubits of the ExcitationPreserving circuit.
            mode: Choose the entangler mode, can be `'iswap'` or `'fsim'`.
            reps: Specifies how often the structure of a rotation layer followed by an entanglement
                layer is repeated.
            entanglement: Specifies the entanglement structure. Can be a string ('full', 'linear'
                or 'sca'), a list of integer-pairs specifying the indices of qubits
                entangled with one another, or a callable returning such a list provided with
                the index of the entanglement layer.
            initial_state: A `QuantumDevice` object to prepend to the circuit.
            skip_unentangled_qubits: If True, the single qubit gates are only applied to qubits
                that are entangled with another qubit. If False, the single qubit gates are applied
                to each qubit in the Ansatz. Defaults to False.
            skip_unentangled_qubits: If True, the single qubit gates are only applied to qubits
                that are entangled with another qubit. If False, the single qubit gates are applied
                to each qubit in the Ansatz. Defaults to False.
            skip_final_rotation_layer: If True, a rotation layer is added at the end of the
                ansatz. If False, no rotation layer is added. Defaults to True.
            parameter_prefix: The parameterized gates require a parameter to be defined.
            insert_barriers: If True, barriers are inserted in between each layer. If False,
                no barriers are inserted.

        Raises:
            ValueError: If the selected mode is not supported.
        """
        supported_modes = ["iswap", "fsim"]
        if mode not in supported_modes:
            raise ValueError(f"Unsupported mode {mode}, choose one of {supported_modes}")
        
        swap = QuantumDevice(n_wires=2, device=device)

        # NOTE: the param should technically be the same
        ops = [
            {'name': 'rxx', 'wires': [0, 1], 'trainable': True},
            {'name': 'ryy', 'wires': [0, 1], 'trainable': True},
        ]

        if mode == "fsim":
            ops.append({'name': 'cp', 'wires': [0, 1], 'trainable': True})

        QuantumModule.from_op_history(ops)(swap)

        super().__init__(
            num_qubits=num_qubits,
            rotation_blocks=RZ,
            entanglement_blocks=swap,
            entanglement=entanglement,
            reps=reps,
            skip_unentangled_qubits=skip_unentangled_qubits,
            skip_final_rotation_layer=skip_final_rotation_layer,
            parameter_prefix=parameter_prefix,
            insert_barriers=insert_barriers,
            initial_state=initial_state,
            name=name,
        )

    @property
    def parameter_bounds(self) -> List[Tuple[float, float]]:
        """Return the parameter bounds.

        Returns:
            The parameter bounds.
        """
        return self.num_parameters * [(-pi, pi)]
