# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
class EnterNotNumber(ValueError):
    pass


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


user_list = []
while num := input("Enter number or 'stop' to exit: "):
    if num.lower() == "stop":
        print("End of input")
        break
    try:
        if is_int(num):
            user_list.append(int(num))
            print(user_list)
        elif is_float(num):
            user_list.append(float(num))
            print(user_list)
        else:
            raise EnterNotNumber
    except EnterNotNumber:
        print("Not a number entered!")

print(user_list)

