import numpy as np

from ..catboost import CatBoostFuelModel


class CatBoostFuelModelV2(CatBoostFuelModel):
    def __init__(self, model_path: str):
        super().__init__(model_path)

    def _convert_data(self, data: np.ndarray) -> np.ndarray:
        data = self._convert(data)
        if len(data.shape) == 1:
            data = np.array([data])
        return data

    def predict(self, data: np.ndarray) -> np.ndarray:
        return self.convert(self.model.predict(self._convert_data(data))).tolist()
