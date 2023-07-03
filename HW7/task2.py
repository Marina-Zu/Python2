# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

__all__ = ['write_names']

import random as rnd
import os


def write_names(count_names, file_name, dir_name):
    literals = 'qwertyuiopasdfghjklzxcvbnm'
    vowels = 'eyuioa'
    min_ = 4
    max_ = 7
    file_path = os.path.join(dir_name, file_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    if not os.path.exists(file_path):
        with open(file_name, 'w', encoding='utf-8') as file:
            for _ in range(count_names):
                name = rnd.sample(literals, rnd.randint(min_, max_))
                if not set(name) & set(vowels):
                    half = len(name) // 2
                    name = name[:half] + rnd.sample(vowels, half)
                    rnd.shuffle(name)
                name = ''.join(name).capitalize()
                file.write(f'{name}\n')


if __name__ == '__main__':
    write_names(7, 'names.txt', 'lesson7')
