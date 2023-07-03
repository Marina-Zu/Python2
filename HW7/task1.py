# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.



# Дорабатываем функции из предыдущих задач.
# * Генерируйте файлы в указанную директорию — отдельный параметр функции.
#
# * Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
#
# * Существующие файлы не должны удаляться/изменяться в случае совпадения имён.



import os.path
from random import randint, uniform

MIN = -1000
MAX = 1000
NUM_ROW = 5

def task_1(count_row, filename, dir_name):
    file_path = os.path.join(dir_name, filename)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    if not os.path.exists(file_path):
        with open(filename, 'a', encoding='utf-8') as f:
            for _ in range(count_row):
                f.write(f'{randint(MIN, MAX)}|{round(uniform(MIN, MAX), 2)}\n')

if __name__ == '__main__':
    task_1(NUM_ROW, "file_1.txt", 'lesson7')

