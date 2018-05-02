import os

import telebot

from base import Base
from word import Word

try:
    from googletrans import Translator

    GOOGLE_TRANSLATE_AVAILABLE = True

except ImportError:
    GOOGLE_TRANSLATE_AVAILABLE = False

token = "384175895:AAFOE3jCL1yDXvtEDttHZEaoHJRleGeVdSc"
bot = telebot.TeleBot(token)
LANGUAGES = {
    '<Detect language>': None,
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Arabic': 'ar',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Bengali': 'bn',
    'Belarusian': 'be',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Chinese Simplified': 'zh-CN',
    'Chinese Traditional': 'zh-TW',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hebrew': 'iw',
    'Hindi': 'hi',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Kannada': 'kn',
    'Korean': 'ko',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Macedonian': 'mk',
    'Malay': 'ms',
    'Maltese': 'mt',
    'Norwegian': 'no',
    'Persian': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Serbian': 'sr',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Spanish': 'es',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Yiddish': 'yi'
}


@bot.message_handler(content_types=["text"])
def handle_text_doc(message):
    # if (message.chat.id != 307781954):
    #     bot.send_message(message.chat.id, "айди не совпал, пошол нахуй")
    #     return

    if message.text[0] == '/':
        runCommand(message.text, message.chat.id)
        return
    myTranslate = translate(message.text)
    bot.send_message(message.chat.id, myTranslate)
    base = Base(message.chat.id)
    nWord = Word()
    nWord.create(message.text, myTranslate)
    base.insert(nWord)
    # a = open('p1.jpg', 'rb')
    # bot.send_message(message.chat.id, 'gj')
    # bot.send_photo(message.chat.id, a)


# ========================

def translate(text):
    translator = Translator()
    language_src = Word.wtf(text)
    dest = ""
    if language_src == 'ru':
        dest = 'en'
    elif language_src == 'en':
        dest = 'ru'
    else:
        return "Я чот не понял на каком это"
    params = dict(
        dest=dest,
        text=text
    )

    try:
        tr = translator.translate(**params)

    except Exception:
        print('blat')
        return False
    else:
        return tr.text


# +++++++++++++++++++++

def runCommand(command, chatId):
    base = Base(chatId)
    if command == '0' or command == '/repeat':
        words = base.findNewData()
        if len(words) == 0:
            bot.send_message(chatId, "Новых слов на сегодня нет!")

        bot.send_message(chatId, "На сегодня {} слов: ".format(len(words)))
        result = 0
        # for i in words:
        #     prompt = "{} - ".format(i.rus)
        #     answer = input(prompt)
        #     if i.test(answer):
        #         result += 1
        #     base.update(i)
        # print("\n Итого {}/{} правильных ответов".format(result, len(words)))
        # wait()
        # cls()

    elif command == '1' or command == '/list':
        words = base.findAllData()
        mass = ""
        bot.send_message(chatId, "Сейчас в безе {} записей: ".format(len(words)))
        for i in words:
            mass += ("{} \r\n".format(i))
        if len(mass) > 0:
            bot.send_message(chatId, mass)

    elif command == '/CLEAR_ALL_DATA':
        del base
        os.remove("{}.db".format(chatId))


# ==========================

def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    # bot.send_message(message.chat.id, message.text)

    command = message.text

    print("Новое слово: \t{}".format(command))
    translate = input("Введи перевод: \t > ")
    nWord = Word()
    nWord.create(command, translate)
    base.insert(nWord)
    cls()
    print("Получено сообщение: {}".format(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def wait():
    input("\t Нажми любую кнопку...")


base = Base()
while 1:
    command = input('Введи новое слово или команду (см. /help) \n> ')
