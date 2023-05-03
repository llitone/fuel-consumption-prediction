from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook

from api_request import APIRequest


class ExcelGenerator(object):
    def __init__(self, filename: str) -> None:
        self.__columns = [
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "T", "U", "V", "W", "X", "Y",
            "Z", "AA", "AB", "AC", "AD"
        ]
        self.workbook: Workbook = load_workbook(filename)
        self.sheet = self.workbook["Данные"]

    def update_fuel_ta_130(self):
        request = APIRequest("http://192.168.0.48:1111/api/v1.0/models/fuel/")
        for column in self.__columns:
            request.append(
                self._convert_date(self.sheet[column + "1"].value),
                self.sheet[column + "12"].value,
                self.sheet[column + "184"].value
            )
        print(request())

    @staticmethod
    def _convert_date(date):
        return "-".join(date.split(".")[-3:]).strip()

excel = ExcelGenerator("../123.xlsm")
excel.update_fuel_ta_130()