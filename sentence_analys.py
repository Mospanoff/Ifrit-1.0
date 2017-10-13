# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 17:09:59 2017

@author: user
"""

command = 'включи будильник '
command = command.split(" ")

print(command)

class Objects():
    def alarm():
        time = Numbers.get_time()# получаем время в формате чч:мм
        if time == '':
            x = input("Укажите время: ")
            print("Будильник установлен на", x)
        if time != '':
            print("Будильник установлен на", time)

    def music():
        time = Numbers.counter()# получаем отсчет времени в формате чч:мм
        to_do = Settings.set_values()# получаем необходимое действие
        print(to_do)
        print("музыка будет", to_do, time)

    def movie():
        time = Numbers.get_time()# получаем время в формате чч:мм
        print("смотри кино в", time)

class Settings():
    global command
    on = ["включи", "запусти", "открой", "начни", "включай", "запускай", "сыграй"]
    off = ["выключи", "останови", "закрой", "закончи", "выключай", "останавливай"]
    show = ["покажи", "показать"]
    say = ["скажи", "ответь", "подскажи"]
    info = ["уточни", "узнай", "проверь"]
    def set_values():
        for i in command:
            if any(i in command for i in Settings.on):
                i = ''
                return i
                break
            if any(cognate in command for cognate in Settings.off):
                Objects.music()
                break
            if any(cognate in command for cognate in Settings.show):
                Objects.movie()
                break
            if any(cognate in command for cognate in Settings.say):
                Objects.movie()
                break
            if any(cognate in command for cognate in Settings.info):
                Objects.movie()
                break

class Numbers():
    global command
    def get_time():
        global command
        numbers = [i for i in command if i.isdigit()]# удяляем все значения, кроме цифр
        time = ':'.join(numbers[0:])# добавляем разделитель между цифрами
        return time
    def counter():
        count_time = Numbers.get_time()
        return count_time


class Cognates():
    global command
    alarm = ["будильник", "разбуди"]
    music = ["музыка", "музыку", "играй", "сыграй"]
    movie = ["кино", "фильм", "сериал", "посмотрим"]
    for i in command:
        if any(i in command for i in alarm):
            Objects.alarm()
            break
        if any(cognate in command for cognate in music):
            Objects.music()
            break
        if any(cognate in command for cognate in movie):
            Objects.movie()
            break

Cognates()