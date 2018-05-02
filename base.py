import sqlite3
from datetime import datetime

from word import Word


class Base:

    def __init__(self, chatID=0):
        name = "{}.db".format(chatID)
        self.connect = sqlite3.connect(name)
        self.cursor = self.connect.cursor()
        create_command = '''CREATE TABLE IF NOT EXISTS `words` (
         `ID` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
         `Eng` INT NOT NULL , 
         `Rus` INT NOT NULL , 
         `NextRepeat` DATE NOT NULL , 
         `RepeatCount` INT NOT NULL);'''
        self.cursor.execute(create_command)
        self.connect.commit()
        print("Подключение к БД удачно!")

    def findNewData(self):
        today = str(datetime.today().date())
        find_command = '''SELECT * FROM `words` WHERE (`NextRepeat`='{0}')
                '''.format(today)
        self.cursor.execute(find_command)
        result = self.cursor.fetchall()

        words = []
        for i in result:
            temp = Word(i[0], i[1], i[2], i[3], i[4])
            words.append(temp)
        return words

    def findAllData(self):
        find_command = '''SELECT * FROM `words`'''
        self.cursor.execute(find_command)
        result = self.cursor.fetchall()

        words = []
        for i in result:
            temp = Word(i[0], i[1], i[2], i[3], i[4])
            words.append(temp)
        return words

    def insert(self, word):
        insert_command = '''INSERT INTO `words` 
                (`Eng`, `Rus`, `NextRepeat`, `RepeatCount`)
                VALUES ('{0}', '{1}', '{2}', {3});
                '''.format(word.eng, word.rus, word.nextRepeat, word.repeatCount)
        # print(insert_command)
        self.connect.execute(insert_command)
        self.connect.commit()

    def update(self, word):
        update_command = '''UPDATE `words` SET
                `NextRepeat`='{0}',
                `RepeatCount`={1}; 
                '''.format(word.nextRepeat, word.repeatCount)
        # print(update_command)
        self.connect.execute(update_command)
        self.connect.commit()
