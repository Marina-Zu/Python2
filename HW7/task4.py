# ✔Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры: ✔расширение
# ✔минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔количество файлов, по умолчанию 42 ✔Имя файла и его размер должны быть в рамках
# переданного диапазона.

import random
import string

def create_files_with_extension(extension, min_name_lenght=6, max_name_lenght=30, min_file_size=256,
                                max_file_size=4096, num_files=1):
    for _ in range(num_files):
        name_lenght = random.randint(min_name_lenght, max_name_lenght)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_lenght)) + '.' + extension

        file_size = random.randint(min_name_lenght, max_name_lenght)
        random_bytes = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size)).encode('UTF-8')

        with open(file_name, 'wb') as file:
            file.write(random_bytes)

create_files_with_extension('bin')