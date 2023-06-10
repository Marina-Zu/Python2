# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions

''' Не получилось сделать первое действие в функции. Не пойму, как туда надо передать строки
def start(str1: str, str2: str) -> list[int, int]:
    i = 0
    while i <= 2:
        str1 = '1/3'
        str2 = '3/5'
        i += 1
        if str1.count('/') == 1 and str2.count('/') == 1:
            num1: list = [int(item) for item in str1.split('/')]
            num2 = [int(item) for item in str2.split('/')]
            i = 3
        else:
            print('Неверный ввод. Необходимо вводить в формате a/b')
        if num1[1] != 0 and num2[1] != 0:
            i = 3
        else:
            print('Знаменатель дроби не может быть равен нулю')
    return num1, num2
'''


i = 0
while i < 3:
    str1 = input('Введите первую дробь ')
    str2 = input('Введите вторую дробь ')
    i += 1
    if str1.count('/') == 1 and str2.count('/') == 1:
        num1 = [int(item) for item in str1.split('/')]
        num2 = [int(item) for item in str2.split('/')]
    else:
        print('Неверный ввод. Необходимо вводить в формате a/b')
        continue
    if num1[1] != 0 and num2[1] != 0:
        break
    else:
        print('Знаменатель дроби не может быть равен нулю')
else:
    print('Все попытки исчерпаны')
    quit()


def result_sum(frac1: list[int, int], frac2: list[int, int]) -> list[int, int]:
    if frac1[1] != frac2[1]:
        result = [frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1]]
    else:
        result = [frac1[0] + frac2[0], frac1[1]]
    return result


def result_mult(frac1: list[int, int], frac2: list[int, int]) -> list[int, int]:
    result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    return result


def fraction_reduction(frac: list[int, int]) -> list[int, int]:
    for i in range(2, min(frac[0], frac[1]) + 1):
        if frac[0] % i == 0 and frac[1] % i == 0:
            frac[0] /= i
            frac[1] /= i
    return [int(frac[0]), int(frac[1])]


def show_result(res: list[int, int]):
    if res[0] == res[1]:
        return f'{res[0] / res[1]}'
    else:
        return f'{res[0]}/{res[1]}'


res_sum = show_result(fraction_reduction(result_sum(num1, num2)))
res_mult = show_result(fraction_reduction(result_mult(num1, num2)))
print(f'{num1[0]}/{num1[1]} + {num2[0]}/{num2[1]} = {res_sum}')
print(f'{num1[0]}/{num1[1]} * {num2[0]}/{num2[1]} = {res_mult}')

print('Проверка:')
f1 = fractions.Fraction(num1[0], num1[1])
f2 = fractions.Fraction(num2[0], num2[1])
print(f'{f1} + {f2} = {f1 + f2}')
print(f'{f1} * {f2} = {f1 * f2}')
