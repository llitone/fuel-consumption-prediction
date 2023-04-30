import pickle
import numpy as np

from typing import Any


class BaseModel(object):
    def __init__(self, model_path: str) -> None:
        with open(model_path, "rb") as file:
            self.model: Any = pickle.load(file)
        self.convert = lambda x: x if 0 < x > 150 else 0
        self.convert = np.vectorize(self.convert)

    def predict(self, data: np.ndarray) -> np.ndarray:
        return self.model.predict(data)
