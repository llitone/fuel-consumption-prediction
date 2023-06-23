from src import *
from src.units.models import *
# if __name__ == "__main__":
#     application.run(port=2342)

models = Models()
print(models.xgb_fuel_130_v2.predict(["123", "123"]))