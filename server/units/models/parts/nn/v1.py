import pickle
from itertools import chain

import numpy as np
import torch
import torch.nn.functional as f

from torch import nn
from torch.utils.data import DataLoader
from sklearn.preprocessing import StandardScaler

from ..torch_model import BaseTorchModel


class _TA130FuelNN(nn.Module):
    def __init__(self):
        super(_TA130FuelNN, self).__init__()
        self.fc1 = nn.Linear(2, 15)
        self.fc2 = nn.Linear(15, 15)
        self.fc3 = nn.Linear(15, 1)

    def forward(self, x):
        x = f.relu(self.fc1(x))
        x = f.relu(self.fc2(x))
        x = f.relu(self.fc3(x))
        return x


class TA130FuelNNV1(BaseTorchModel):
    def __init__(self, model_path: str, scaler_path: str):
        super().__init__(model_path, _TA130FuelNN)
        with open(scaler_path, "rb") as file:
            self.scaler: StandardScaler = pickle.load(file)

    def predict(self, data: np.array):
        self.model.eval()
        data = np.array(data)[:, 1:]
        data = self.scaler.transform(np.array(data, dtype=float))
        data = torch.tensor(data, dtype=torch.float32)
        data = DataLoader(list(zip(data, torch.tensor([0] * len(data)))))
        predictions = [self.model(X_batch) for X_batch, _ in data]
        predictions = list(map(lambda x: x.detach().numpy(), predictions))
        predictions = list(map(lambda x: x.reshape(-1).tolist(), predictions))
        predictions = np.array(list(chain.from_iterable(predictions)))
        predictions = self.convert(predictions)
        return list(predictions)
