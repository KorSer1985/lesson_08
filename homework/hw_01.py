# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
# виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, dates: str):
        self.date = dates

    @classmethod
    def str_to_num(cls, dates):
        day, month, year = dates.split("-")
        return int(day), int(month), int(year)

    @staticmethod
    def valid(day, month, year):
        if 0 < day < 32:
            if 0 < month < 12:
                if 0 < year < 2022:
                    return f"All right"
                else:
                    return f"wrong year"
            else:
                return f"wrong month"
        else:
            return f"wrong day"


date = Date(input("Enter the date in the format dd-mm-yyyy: "))
print(date)
print(Date.valid(11, 11, 2029))
print(date.valid(22, 15, 2021))
print(date.valid(33, 15, 2021))
print(Date.str_to_num('11 - 11 - 2011'))
print(date.str_to_num('11 - 11 - 2020'))
print(Date.valid(18, 12, 1985))
