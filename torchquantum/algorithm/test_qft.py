from torchquantum.algorithm import QFT

print(QFT(n_wires=10).construct_qft_circuit())
print(QFT(n_wires=10).construct_inverse_qft_circuit())
