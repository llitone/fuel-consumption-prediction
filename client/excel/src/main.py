import os

from config import file_ends
from units.worker import ExcelGenerator


if __name__ == "__main__":
    for file in os.listdir():
        if file.endswith(file_ends):
            generator = ExcelGenerator(str(file))
            generator.update_fuel_ta_130()

