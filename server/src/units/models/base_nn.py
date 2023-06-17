import numpy as np


class BaseModelNN(object):
    def __init__(self):
        self.convert = lambda x: x if 0 < x > 150 else 0
        self.convert = np.vectorize(self.convert)

    @staticmethod
    def _convert(data):
        return np.array(data)
