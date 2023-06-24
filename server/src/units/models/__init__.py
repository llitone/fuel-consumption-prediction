from enum import Enum
from typing import Any

from .parts import *


class _ModelsPaths(Enum):
    xgb_fuel_130_v1 = "./src/units/models/saves/fuel/xgb_fuelTA130_099889.bf"
    xgb_fuel_130_v2 = "./src/units/models/saves/fuel/xgb_fuelTA130_099.bf"
    catboost_fuel_130_v1 = "./src/units/models/saves/fuel/cat_boost_fuelTA130_09924.bf"
    catboost_fuel_130_v2 = "./src/units/models/saves/fuel/cat_boost_fuelTA130v2.bf"
    torch_model_fuel_130_v1 = "./src/units/models/saves/fuel/FuelTA130NN.pt"
    torch_scaler_fuel_130_v1 = "./src/units/models/saves/fuel/nn_fuelTA130_0868_scaler.bf"


class Models(object):
    def __init__(self):
        self.xgb_fuel_130_v1 = XGBFuelModelV1(_ModelsPaths.xgb_fuel_130_v1.value)
        self.xgb_fuel_130_v2 = XGBFuelModelV2(_ModelsPaths.xgb_fuel_130_v2.value)
        self.catboost_fuel_130_v1 = CatBoostFuelModelV1(_ModelsPaths.catboost_fuel_130_v1.value)
        self.catboost_fuel_130_v2 = CatBoostFuelModelV2(_ModelsPaths.catboost_fuel_130_v2.value)
        self.torch_fuel_130_v1 = TA130FuelNNV1(
            _ModelsPaths.torch_model_fuel_130_v1.value,
            _ModelsPaths.torch_scaler_fuel_130_v1.value
        )
        self.__all_models = {
            "xgb_fuel_130_v1": self.xgb_fuel_130_v1,
            "xgb_fuel_130_v2": self.xgb_fuel_130_v2,
            "catboost_fuel_130_v1": self.catboost_fuel_130_v1,
            "catboost_fuel_130_v2": self.catboost_fuel_130_v2,
            "torch_fuel_130_v1": self.torch_fuel_130_v1
        }

    def __getitem__(self, item: str) -> Any:
        if item == "xgb_fuel_130":
            return self.__all_models["xgb_fuel_130_v2"]
        elif item == "catboost_fuel_130":
            return self.__all_models["catboost_fuel_130_v1"]
        elif item == "torch_fuel_130":
            return self.__all_models["torch_fuel_130_v1"]
        return self.__all_models[item]
