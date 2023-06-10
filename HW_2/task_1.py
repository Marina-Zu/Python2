# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

NUMBER = 25005
SYSTEM_16 = 16


def convert(number: int, system: int) -> str:
    temp = list()
    while number > 0:
        D = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        a = int(number % system)
        if 10 <= a <= 15:
            temp.append(str(D[a]))
        else:
            temp.append(str(a))
        number = number // system
    temp.reverse()
    return ''.join(temp)


print(f'Число {NUMBER} в шестандцатиричной системе {convert(NUMBER, SYSTEM_16)}')
print(f'Проверка {hex(NUMBER)}')