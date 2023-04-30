from enum import Enum

from .parts import *


class _ModelsPaths(Enum):
    xgb_fuel_130 = "./units/models/saves/fuel/xgb_fuelTA130_0998.bf"


class Models(object):
    def __init__(self):
        self.xgb_fuel_130 = XGBModel(_ModelsPaths.xgb_fuel_130.value)
        self.__all_models = {
            "xgb_fuel_130": self.xgb_fuel_130
        }

    def __getitem__(self, item):
        return self.__all_models[item]
