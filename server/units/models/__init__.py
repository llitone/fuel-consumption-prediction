from enum import Enum

from .parts import *


class _ModelsPaths(Enum):
    xgb_fuel_130 = "./units/models/saves/fuel/xgb_fuelTA130_099889.bf"
    catboost_fuel_130 = "./units/models/saves/fuel/cat_boost_fuelTA130_09924.bf"


class Models(object):
    def __init__(self):
        self.xgb_fuel_130 = XGBFuelModel(_ModelsPaths.xgb_fuel_130.value)
        self.catboost_fuel_130 = CatBoostFuelModel(_ModelsPaths.catboost_fuel_130.value)
        self.__all_models = {
            "xgb_fuel_130": self.xgb_fuel_130,
            "catboost_fuel_130": self.catboost_fuel_130
        }

    def __getitem__(self, item):
        return self.__all_models[item]
