import xlwings
from .api_request import APIRequest


class ExcelGenerator(object):
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.__columns = [
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "T", "U", "V", "W", "X", "Y",
            "Z", "AA", "AB", "AC", "AD"
        ]
        self.workbook: xlwings.Book = xlwings.Book(self.filename)
        self.sheet = self.workbook.sheets["Данные"]

    def update_fuel_ta_130(self):
        request = APIRequest()
        skip = []
        for column in self.__columns:
            if str(self.sheet.range(column + "12").value) not in ["", "0"] and \
                    str(self.sheet.range(column + "184").value) not in ["", "0"]:
                request.append(
                    self._convert_date(self.sheet.range(column + "1").value),
                    self.sheet.range(column + "12").value,
                    self.sheet.range(column + "184").value
                )
            else:
                skip.append(column)
        request = iter(request())
        for column in self.__columns:
            if column in skip:
                self.sheet.range(column + "3").value = "0"
            else:
                self.sheet.range(column + "3").value = next(request)
        self.workbook.save(self.filename)

    @staticmethod
    def _convert_date(date):
        return "-".join(date.split(".")[-3:]).strip()
