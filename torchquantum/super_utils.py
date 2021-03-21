import numpy as np
import torch.nn as nn


class ConfigSampler(object):
    def __init__(self, model: nn.Module):
        self.model = model
        self.config_space = model.config_space

    def get_uniform_sample_config(self):
        sample_config = []
        for layer_config_space in self.config_space:
            layer_config = np.random.choice(layer_config_space)
            sample_config.append(layer_config)

        return sample_config

    def get_named_sample_config(self, name):
        sample_config = []
        if name == 'smallest':
            for layer_config_space in self.config_space:
                layer_config = layer_config_space[0]
                sample_config.append(layer_config)
        elif name == 'largest':
            for layer_config_space in self.config_space:
                layer_config = layer_config_space[-1]
                sample_config.append(layer_config)
        elif name == 'middle':
            for layer_config_space in self.config_space:
                layer_config = layer_config_space[len(layer_config_space) // 2]
                sample_config.append(layer_config)
        else:
            raise NotImplementedError(name)
        return sample_config
