# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class DivisionByZero(Exception):
    pass


while True:
    try:
        dividend = float(input("Enter the dividend: "))
        divider = float(input("Enter the divider: "))
        if divider == 0:
            raise DivisionByZero
        break
    except DivisionByZero:
        print("You can't divide by zero!")
    except ValueError:
        print("Not a numbed entered!")
        continue


print(f"{dividend} / {divider} = {round(dividend / divider, 2)}")
