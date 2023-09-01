import os

from src.config import *
from src.units.worker import ExcelGenerator


if __name__ == "__main__":
    os.chdir("./")
    if files == ".":
        for file in os.listdir():
            if file.endswith(file_ends):
                generator = ExcelGenerator(str(file))
                generator.update_fuel_ta_130()
    else:
        generator = ExcelGenerator(files)
        generator.update_fuel_ta_130()
