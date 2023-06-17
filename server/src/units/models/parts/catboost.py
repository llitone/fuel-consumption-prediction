import numpy as np

from ..base import BaseModel


class CatBoostFuelModel(BaseModel):
    def __init__(self, model_path: str):
        super().__init__(model_path)

    def predict(self, data: np.ndarray) -> np.ndarray:
        return self.convert(self.model.predict(data)).tolist()
