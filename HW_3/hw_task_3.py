#  Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант

dict = {'кружка': 0.3, 'ложка': 0.2, 'фонарик': 0.5, 'спички': 0.1, 'веревка': 2, 'палатка': 9,
        'спальник': 2.5, 'термос': 0.5, 'котелок': 1.8, 'пенка': 1, 'компас': 0.4, 'полотенце': 1.5,
        'консервы': 1.3, 'крупа': 0.9, 'ботинки': 3, 'носки': 0.2}

MAX_LOAD = 13

weight_backpack = 0
dict_backpack = {}
for key, value in dict.items():
    if weight_backpack + value <= MAX_LOAD:
        weight_backpack += value
        dict_backpack[key] = value

for i, backpack in enumerate(dict_backpack, start=1):
    print(i, backpack)

print(f'Итого {round(weight_backpack, 2)} кг')
