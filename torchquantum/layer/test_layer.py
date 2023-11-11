from layers import EntangleLinear, EntanglePairwise, EntangleFull, EntangleCircular

from layers import EntanglementLayer

import torchquantum as tq
import torchquantum.functional as tqf

qdev = tq.QuantumDevice(n_wires=10, bsz=5, device="cpu", record_op=True) # use device='cuda' for GPU

lin = EntangleLinear(tq.CNOT, 10, "linear") # EntangleLinear(tq.CNOT, 2)

lin(qdev)

pair = EntangleLinear(tq.CNOT, 10, "pairwise") #EntanglePairwise(tq.CNOT, 2)

pair(qdev)

full = EntangleLinear(tq.CNOT, 10, "full") #EntangleFull(tq.CNOT, 2)
full(qdev)

circ = EntangleLinear(tq.CNOT, 10, "circular") #EntangleCircular(tq.CNOT, 2)
circ(qdev)

print(qdev)


# lyr = EntangleLinear(tq.CNOT, 2, "linear")
