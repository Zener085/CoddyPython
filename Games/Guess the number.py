from random import randint as rnd
from time import sleep

MIN_VALUE = 1  # минимальное число, которое можно загадать
MAX_VALUE = 10  # максимальное число, которое можно загадать
MIN_SLEEP = 1
MAX_SLEEP = 3


def guess() -> None:
    """ Компьютер загадывает число, пользователь должен его отгадать """

    number = rnd(MIN_VALUE, MAX_VALUE)  # берем случайное число, которое пользователь будет отгадывать

    print("Сейчас я загадал число от ", MIN_VALUE, " до ", MAX_VALUE, "\nУгадай, какое?", sep="")

    for i in range(MAX_VALUE):  # даём кол-во попыток
        if int(input()) == number:  # сравнимаем написанное число с загаданным
            print("Ты угадал!")
            return
        elif i < 10:  # если ещё есть попытки
            sleep(rnd(MIN_SLEEP, MAX_SLEEP))
            print("Нет, я загадал другое\nУ тебя осталось", MAX_VALUE - i - 1, "попыток.")

    print("Не угадал! Я загадал", number)


def find() -> None:
    """ Пользователь загадывает число, компьютер должен его отгадать """

    numbers = list(i for i in range(MIN_VALUE, MAX_VALUE + 1))  # создаем список чисел от минимального до максимального

    print("Сейчас загадай число от", MIN_VALUE, "до", MAX_VALUE, "а я попробую отгадать.\nЕсли я угадаю, напиши 'да'")

    for i in range(MAX_VALUE + 1):  # повторяем столько, сколько у нас есть попыток
        if len(numbers) == 0:  # если у нас закончились числа, которые мы ещё не проверяли
            sleep(rnd(MIN_SLEEP, MAX_SLEEP))
            print("Стоп... Ты меня обманул!")
            return

        number = rnd(0, len(numbers) - 1)  # берём случайное число из списка

        print("Это ", numbers[number], "?", sep="")
        answer = input().lower()  # сохраняем ответ, сразу изменяя регист всем буквам
        if answer in ["да", "да.", "да!"]:
            print("Ура, я угадал!")
            return
        else:
            sleep(rnd(MIN_SLEEP, MAX_SLEEP))
            print("Ладно, сейчас ещё попробую")
            numbers.pop(number)  # удаляем число из списка, которое уже спрашивали


print("Привет! Это игра 'Угадай число'. Смысл игры - один загадывает число, а второй его отгадывает.")
print("Если хочешь загадать число сам, напиши 'Загадать число', если хочешь отгадывать, напиши 'Угадать число', а" +
      " если ты больше не хочешь играть, то напиши выход")

while True:
    choice = input().lower()  # спрашиваем, что человек хочет выбрать, регистр букв не учитываем
    if choice in ["загадать число", "загадать число.", "загадать число!"]:
        find()
    elif choice in ["угадать число", "угадать число.", "угадать число!"]:
        guess()
    elif choice in ["выход", "выход.", "выход!"]:
        print("Завершение программы...")
        break  # заканчиваем бесконечный цикл (а с ним и всю программу)
    else:
        sleep(rnd(MIN_SLEEP, MAX_SLEEP))
        print("Пожалуйста, повтори, ты написал что-то непонятное.")

    sleep(rnd(MIN_SLEEP, MAX_SLEEP))
    print("Игра закончилась.")
    sleep(rnd(MIN_SLEEP, MAX_SLEEP))
    print("Если хочешь загадать число сам, напиши 'Загадать число', если хочешь отгадывать, напиши 'Угадать число'.")
