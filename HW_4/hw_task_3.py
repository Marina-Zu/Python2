# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

"""Не смогла сделать единую функцию main. Не видит глобальные переменные"""
MULTI = 50
PERCENT_CASH = 1.5
LIMIT_DOWN = 30
LIMIT_UP = 600
PERCENT_COUNT = 3
RICH = 5_000_000
TAX_RICH = 10
balance = 0
count = 0


def add_money(balance: int) -> int:
    money = int(input('Введите сумму, кратную 50 у.е.-> '))
    if money % MULTI == 0:
        balance += money
    else:
        print('Некорректный ввод, повторите')
    return balance


def pop_money(balance: int) -> int:
    money = int(input('Введите сумму, кратную 50 у.е.-> '))
    cent = 0
    if money % MULTI == 0:
        cent = money / 100 * PERCENT_CASH
    else:
        print('Некорректный ввод, повторите')
    if cent < LIMIT_DOWN:
        cent = LIMIT_DOWN
    elif cent > LIMIT_UP:
        cent = LIMIT_UP
    if balance >= money + cent:
        balance -= money + cent
    else:
        print('Недостаточно средств на счете')
    return balance


def exit():
    print('Ждем Вас снова!')
    quit()


def riches(balance: int):
    if balance > RICH:
        balance -= balance / 100 * TAX_RICH
        print(f'Снят налог на богатство {TAX_RICH}%. Баланс равен {round(balance, 2)} ')
    return balance


def main(count, balance):
    while True:
        count += 1
        balance = riches(balance)
        choice = int(input('Выберите действие (1 - пополнить, 2 - снять, 3 - выйти): '))
        if choice == 1:
            balance = add_money(balance)
        elif choice == 2:
            balance = pop_money(balance)
        elif choice == 3:
            exit()
        else:
            print('Неверно введено действие')
        print('Текущий баланс равен', round(balance, 2))
        if count == 3:
            balance += round(balance / 100 * PERCENT_COUNT, 2)
            print(f'Пополнение баланса на {PERCENT_COUNT}%. Баланс равен {balance}')
            count = 0
        else:
            continue


main()
