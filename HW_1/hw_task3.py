# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1001
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 0
while count < 10:
    dig = int(input(f'Попытка {10 - count} Введите число > '))
    count += 1
    if dig < num:
        print('Больше')
    elif dig > num:
        print('Меньше')
    elif dig == num:
        print('Ура! Вы угадали!')
        break
    if count == 10:
        print(f'Увы... Загаданное число {num}')