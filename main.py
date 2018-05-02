import os

from base import Base
from word import Word


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def wait():
    input("\t Нажми любую кнопку...")


base = Base()
while 1:
    command = input('Введи новое слово или команду (см. /help) \n> ')
    if command == '0' or command == '/repeat':
        words = base.findNewData()
        if len(words) == 0:
            print("Новых слов на сегодня нет!")
            wait()
            continue
        cls()
        print("На сегодня {} слов: ".format(len(words)))
        result = 0
        for i in words:
            prompt = "{} - ".format(i.rus)
            answer = input(prompt)
            if i.test(answer):
                result += 1
            base.update(i)
        print("\n Итого {}/{} правильных ответов".format(result, len(words)))
        wait()
        cls()

    elif command == '1' or command == '/list':
        cls()
        words = base.findAllData()
        print("Сейчас в безе {} записей: ".format(len(words)))
        for i in words:
            print("\t{}".format(i))
        print("\n")
        wait()
        cls()

    else:
        print("Новое слово: \t{}".format(command))
        translate = input("Введи перевод: \t > ")
        nWord = Word()
        nWord.create(command, translate)
        base.insert(nWord)
        cls()
