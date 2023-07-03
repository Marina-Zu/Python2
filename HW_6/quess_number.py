# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь

from random import randint
import sys

__all__ = ['quess_number']

LOWER_LIMIT = 0
UPPER_LIMIT = 1001
a = 10


def quess_number(low=0, up=1000, a=10):
    count = 0
    num = randint(low, up)
    #print = (input(f'ве{a - count} Введите число > ')
    while count < a:
        dig = int(input(f'Попытка {a - count} Введите число > '))
        count += 1
        if dig < num:
            print('Больше')
        elif dig > num:
            print('Меньше')
        elif dig == num:
            print('Ура! Вы угадали!')
            return True
        if count == a:
            print(f'Увы... Загаданное число {num}')
            return False


if __name__ == "__main__":
    # _, LOWER_LIMIT, UPPER_LIMIT, a = sys.argv
    # my_func(int(LOWER_LIMIT), int(UPPER_LIMIT), int(a))
    _, *params = sys.argv
    print(quess_number(*map(int, params)))
