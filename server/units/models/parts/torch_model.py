import torch

from torch.nn import Module
from torch.utils.data import DataLoader

from ..base_nn import BaseModelNN


class BaseTorchModel(BaseModelNN):
    def __init__(self, model_path: str, model_class):
        super().__init__()
        self.model: Module = model_class()
        self.model.load_state_dict(torch.load(model_path))

    def predict(self, data: DataLoader):
        self.model.eval()
        predictions = [self.model(X_batch) for X_batch, _ in data]
        return predictions
