# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 22:56:52 2017

@author: user
"""
import requests
import json

def get_source():
  url = 'http://192.168.10.236:1925/1/sources/current'
  answer = requests.get(url).json()
  print(answer)

def push_ok():
  headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
  url = 'http://192.168.10.236:1925/1/input/key'
  payload = {"key": "Confirm"}
  answer = requests.post(url, data=json.dumps(payload), headers=headers)
  print(answer)

def mute():
  headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
  url = 'http://192.168.10.236:1925/1/input/key'
  payload = {"key": "Mute"}
  answer = requests.post(url, data=json.dumps(payload), headers=headers)
  print(answer)

def volume():
  headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
  url = 'http://192.168.10.236:1925/1/audio/volume'
  vol_level = input('Введите значение: ')
  payload = {"muted": "false", "current": vol_level}
  answer = requests.post(url, data=json.dumps(payload), headers=headers)
  print(answer)



push_ok()