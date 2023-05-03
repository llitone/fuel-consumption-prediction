import numpy as np

from ..catboost import CatBoostFuelModel


class CatBoostFuelModelV1(CatBoostFuelModel):
    def __init__(self, model_path: str):
        super().__init__(model_path)

    def _convert_data(self, data: np.ndarray) -> np.ndarray:
        data = self._convert(data)
        if len(data.shape) == 1:
            data = np.array([data])
        if len(data[0]) == 3:
            date = np.array([[0, 0, 0]], dtype=int)
            for i in data[:, 0]:
                date = np.vstack([date, np.array(i.split("-"))])
            date = date[1:]
            data = np.concatenate([date, np.float32(data[:, 1:])], axis=1)
            data = np.float32(data)
        return data

    def predict(self, data: np.ndarray) -> np.ndarray:
        return self.convert(self.model.predict(self._convert_data(data))).tolist()
