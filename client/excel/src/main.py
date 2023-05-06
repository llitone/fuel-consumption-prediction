from units.worker import ExcelGenerator


if __name__ == "__main__":
    generator = ExcelGenerator("123.xlsm")
    generator.update_fuel_ta_130()

