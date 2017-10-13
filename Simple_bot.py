# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 22:46:29 2017

@author: user
"""
import pyowm #weather mod
import telepot
import time
import threading
import wolframalpha
from random import choice
import os
from set_alarm import alarm as alarm
import glob
from recognition_list import Recognition_list as RL

owm = pyowm.OWM('ea8d1b7f144207b29d17ff21450232f4')
TOKEN = '345649609:AAHVl4j4ysRZI07FEntP17Jzpn4sAH2Bw4k'
bot = telepot.Bot(TOKEN)
app_id = "8JVQRK-PLK3U5EP88"
client = wolframalpha.Client(app_id)

def Simple_bot(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        query = msg['text']
        print('ID:',msg['chat']['id'])
        print('Имя:',msg['chat']['first_name'])
        print('ID сообщения:',msg['message_id'])
        print('Сообщение:', msg['text'])
        bot.sendMessage(chat_id, check(query))

def check(query):
    query = query.lower()
    if any(cognate in query for cognate in RL.WEATHER):
        return weather_owm()
    if any(cognate in query for cognate in RL.ALARM):
        alarm_.start()
        alarm_.join()
    else:
        return wolfram_alpha(query)

def wolfram_alpha(query):
    try:
        res = client.query(query)
        answer = next(res.results).text
        print(answer)
        return answer
    except:
      return 'I dont know'


def weather_owm():
    observation = owm.weather_at_place("Moscow, RU")
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')
    t = temperature['temp']
    answer = 'Средняя температура за окном:', t
    print(answer)
    return str(answer)

class A:
    def __call__(self):
        bot.message_loop(Simple_bot)
        print ('Listening bot 1...')
        print(threading.active_count())
        # Keep the program online.
        while 1:
            time.sleep(10)

class B:
    def __call__(self):
      alarm()

if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    a = A()
    b = B()

    main_ = threading.Thread(target=a)
    alarm_ = threading.Thread(target=b)

    main_.start()
    alarm_.start()

    alarm_.join()
    main_.join()
