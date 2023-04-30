import numpy as np

from units.models.base import BaseModel


class XGBModel(BaseModel):
    def __init__(self, model_path: str):
        super().__init__(model_path)

    def predict(self, data: np.ndarray) -> np.ndarray:
        date = np.array([[0, 0, 0]], dtype=int)
        for i in data[:, 0]:
            date = np.vstack([date, i.split("-")])
        date = date[1:]
        data = np.concatenate([date, np.int32(data[:, 1:])], axis=1)
        data = np.int32(data)
        return self.convert(self.model.predict(data))


model = XGBModel("")
print()