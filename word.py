from datetime import datetime
from datetime import timedelta


class Word:
    id = 0
    eng = ""
    rus = ""
    nextRepeat = ""
    repeatCount = 1

    def wtf(word=""):
        if ('а' <= word[0] <= 'я'):
            return 'ru'
        elif ('a' <= word[0] <= 'z'):
            return 'en'
        elif ('А' <= word[0] <= 'Я'):
            return 'ru'
        elif ('A' <= word[0] <= 'Z'):
            return 'en'
        else:
            return "я не понял, что это за язык"

    def create(self, theword="", translate=""):
        if ('а' <= theword[1] <= 'я'):
            self.eng = translate
            self.rus = theword
        elif ('a' <= theword[1] <= 'z'):
            self.eng = theword
            self.rus = translate
        else:
            print("я не смог понять, какой это язык, поэтому будем думать что английский :)")
            self.eng = theword
            self.rus = translate
        nextRepeat = datetime.today() + timedelta(days=self.repeatCount)
        self.nextRepeat = str(nextRepeat.date())

    def __init__(self, id=0, eng="", rus="", nextRepeat="", repeatCount=1):
        self.id = id
        self.eng = eng
        self.rus = rus
        self.nextRepeat = nextRepeat
        self.repeatCount = repeatCount

    def __str__(self):
        return "{0}  {1} - {2}\t||\t{3} ({4})".format(self.id, self.eng, self.rus,
                                                      self.nextRepeat, self.repeatCount)

    def correct(self):
        self.repeatCount *= 2
        nextDay = datetime.today() + timedelta(days=self.repeatCount)
        self.nextRepeat = str(nextDay.date())
        print("\tПравильно! следующее повторение через {} дней".format(self.repeatCount))
        return 1

    def incorrect(self):
        print("Ошибочка! Правильный ответ: \t {}".format(self.eng))
        answer = input("Опечатка? [да/НЕТ] ")
        if self._answerAnalise(answer):
            self.correct()
            return

        if self.repeatCount > 2:
            self.repeatCount /= 2
        nextDay = datetime.today() + timedelta(days=self.repeatCount)
        self.nextRepeat = str(nextDay.date())

        print("Следующее повторение: {}".format(self.nextRepeat))
        return 0

    def test(self, answer):
        eng = self.eng.lower()
        answer = answer.lower()
        if eng == answer:
            self.correct()
            return 1
        else:
            self.incorrect()
            return 0

    def _answerAnalise(self, answer):
        a = answer.lower()
        if a == 'да' or a == 'д' or a == 'y' or a == 'yes':
            return 1
        else:
            return 0
