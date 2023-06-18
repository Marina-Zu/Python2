# В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re
import string

text = "Гостеприимно распахнуло двери перед своими будущими учениками в 1992 году Краснодарское хореографическое училище – " \
       "первое среднее профессиональное образовательное учреждение в области хореографического искусства на Северном Кавказе. " \
       "130 учащихся и 50  педагогов объединены одной общей целью: создание атмосферы творческого труда, взаимопонимания, " \
       "высокого профессионального мастерства. Ведь каждый день жизни училища – это огромная, кропотливая до пота работа " \
       "его педагогов. Итог этой работы ежегодно виден на отчетном концерте училища. Краснодарское хореографическое училище " \
       "дает высококачественное профессиональное образование через исторически сложившуюся и значимую для культуры " \
       "систему хореографического искусства, готовя специалистов по двум направлениям: «Артист балета, преподаватель», " \
       "«Артист балета ансамбля песни и танца танцевального коллектива, преподаватель». Сегодня училище вышло на новый " \
       "уровень развития благодаря огромной поддержке министерства культуры Краснодарского края, совместной работе " \
       "с руководством ведущих театрально-концертных учреждений г. Краснодара: Краснодарское творческое объединение " \
       "«Премьера» им. Л.Г. Гатова, Краснодарская филармония имени Г.Ф. Пономаренко, Кубанский казачий хор, " \
       "Краснодарское творческое объединение «Премьера». Уже стало традиционным, что обучающиеся училища выступают на " \
       "одной сцене с лучшими артистами балета. Училище еще молодое, но устремлено в будущее, открыто всему новому, " \
       "ведь оно – частичка огромного сердца Кубани, которая живет с ней едиными стремительными современными ритмами."


NUM_WORDS = 10

new_text = text.replace('–', '').lower().split()

for i in range(len(new_text)):
    new_text[i] = new_text[i].strip('.,-"/*!?;:«»{}()')

dict_text = {}
for item in new_text:
    dict_text[item] = dict_text.get(item, [new_text.count(item)]) # Создаем словарь слово - количество

#Сортируем словарь по убыванию значений
sort_text = {key: value for key, value in sorted(dict_text.items(), key=lambda item: item[1], reverse=True)}

for el in range(NUM_WORDS):
       print(list(sort_text.keys())[el], '-', list(sort_text.values())[el])