# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

__all__ = ['riddle_box', 'show_result']

def riddle(text="Сорок одёжок и все без застёжек", solution=['капуста', 'капустка'], attempt=5):
    count = 1
    print(f"Отгадайте загадку: {text}")
    while count < attempt:
        a = (input("Введите отгадку: ")).lower()
        if a in solution:
            print(f"Вы угадали c {count} попытки.")
            return count
        else:
            print("Ошибка")
            count += 1
        if count == attempt:
            print("Вы исчерпали количество попыток")
            return 0


def riddle_box():
    dic = {"Зимой и летом одним цветом": ["ель", "елка", "елочка"],
           "Не лает, не кусает, в дом не пускает": ['замок', 'вахтер'],
           "Висит груша, нельзя скушать": ['лампа', 'лампочка']}
    for i, j in dic.items():
        riddle(i, j)


def riddle_result(text, f_attempt):
    _result[text] = f_attempt


def show_result():
    output = "\n ".join([f"Вы угадали загадку '{key}' с {value} попытки" for key, value in _result.items()])
    print(output)


_result = {}
