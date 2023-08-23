# import torchquantum as tq
# import torchquantum.layers as layers
#
# class NLocal(layers.LayerTemplate0):
#     """Layer Template for a NLocal Class
#
#     Args:
#         rotation_ops (list): gates for the rotation layer as a list of torchquantum operations
#         entanglement_ops (list): gates for the entanglement layer as a list of torchquantum operations
#         arch (dict): circuit architecture in a dictionary format
#         rotation_layer (torchquantum.QuantumModule): type of rotation layer in a torchquantum.QuantumModule format
#         entanglement_layer (torchquantum.QuantumModule): type of entanglement layer in a torchquantum.QuantumModule format
#         rotation_layer_params (dict): additional parameters for the rotation layer in a dictionary format
#         entanglement_layer_params (dict): additional parameters for the entanglement layer in a dictionary format
#         initial_circuit (torchquantum.QuantumModule): initial gates or layer in a QuantumModule format
#         skip_final_rotation_layer (bool): whether or not to add the final rotation layer as a boolean
#     """
#     def __init__(self, rotation_ops: list, entanglement_ops: list, arch: dict = None, rotation_layer: tq.QuantumModule=tq.layers.Op1QAllLayer, entanglement_layer: tq.QuantumModule=tq.layers.Op2QAllLayer, rotation_layer_params: dict={}, entanglement_layer_params: dict={}, initial_circuit: tq.QuantumModule=None, skip_final_rotation_layer: bool=False):
#         # rotation block options
#         self.rotation_ops = rotation_ops
#         self.rotation_layer = rotation_layer
#         self.rotation_layer_params = rotation_layer_params
#
#         # entanglement block options
#         self.entanglement_ops = entanglement_ops
#         self.entanglement_layer = entanglement_layer
#         self.entanglement_layer_params = entanglement_layer_params
#
#         # extra parameters
#         self.initial_circuit = initial_circuit
#         self.skip_final_rotation_layer = skip_final_rotation_layer
#
#         # initialize the LayerTemplate0
#         super().__init__(arch)
#
#     def bulid_rotation_block(self):
#         rotation_layers = []
#         for rot in self.rotation_ops:
#             rotation_layers.append(self.rotation_layer(op=rot, n_wires=self.n_wires, **self.rotation_layer_params))
#         return rotation_layers
#
#     def bulid_entanglement_block(self):
#         entanglement_layers = []
#         for entanglement in self.entanglement_ops:
#             entanglement_layers.append(self.entanglement_layer(op=entanglement, n_wires=self.n_wires, **self.entanglement_layer_params))
#         return entanglement_layers
#
#     def build_layers(self):
#         layers_all = tq.QuantumModuleList()
#
#         # add the initial circui
#         if self.initial_circuit is not None:
#             layers_all.append(self.initial_circuit)
#
#         # repeat for each rep
#         for _ in range(self.n_blocks):
#
#             # add rotation blocks to the qubits
#             layers_all.extend(self.bulid_rotation_block())
#
#             # add entanglement blocks to the qubits
#             layers_all.extend(self.bulid_entanglement_block())
#
#         # add final rotation layer
#         if not self.skip_final_rotation_layer:
#             layers_all.extend(self.build_rotation_block())
#
#         # return QuantumModuleList
#         return layers_all
#


import torchquantum as tq
# import nlocal as layers
import torchquantum.layer as layers

print(layers.QFTLayer(n_wires=10, inverse=True))
