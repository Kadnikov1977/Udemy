# -*- coding: utf-8 -*-

import telebot
import datetime
import smtplib
from email.mime.text import MIMEText


bot = telebot.TeleBot('1240054802:AAFa6dzhYut_8R12nY09AzJd0sy0uQ5DRHM')

otdel = ""
contact = ""
problema = ""

@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id, "Здравствуйте, Вас приветствует служба поддержки Межрегионгаз Самара")
    bot.send_message(message.from_user.id, "Введите пожалуйста название Вашего отдела")
    bot.register_next_step_handler(message, get_otdel)

def get_otdel(message):
    global otdel
    otdel = message.text
    bot.send_message(message.from_user.id, 'Введите Ваш контактный телефон')
    bot.register_next_step_handler(message, get_contact)

def get_contact(message):
    global contact
    contact = message.text
    bot.send_message(message.from_user.id, 'Опишите коротко проблему')
    bot.register_next_step_handler(message, get_problema)

def get_problema(message):
    global problema
    problema = message.text
    nomer = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    text = 'Номер заявки: ' + nomer + '\n' + 'Отделение: ' + otdel + '\n' + 'Контактный телефон: ' + contact + '\n' + 'Описание проблемы: ' + problema
    bot.send_message(message.from_user.id, text)

    msg = MIMEText(text)
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('545175@gmail.com', 'Globalharry1977#')
    smtpObj.sendmail("545175@gmail.com", "43623@mail.ru", msg.as_string())
    smtpObj.quit()
    bot.send_message(message.chat.id, "Ваша заявка принята! Для создания новой заявки - "
                                      "отправте команду /start.")

bot.polling(none_stop=True, interval=0)

