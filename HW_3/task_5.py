# Задание №5
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

my_l = [1, 1, 1, 2, 2, 3, 6, 6, 7, 7, 7]
new_l = []
for i, num in enumerate(my_l, start=1):
    if num % 2 != 0:
        new_l.append(i)
print(new_l)