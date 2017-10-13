import time
from random import choice
import os
import glob
import threading

def alarm(query):

      awut = query.split(' ')
      awut = ' '.join(awut[2:])
      ct = time.strftime("%X")
      true_files = glob.glob('G:\VK_Music\*.mp3')
      folder = ('G:\VK_Music')
      file = choice(true_files)
      fullname = os.path.join(folder, file) # получаем полное имя
      print(fullname)
      while awut > ct:
        ct = time.strftime("%X")
        print(ct, awut)
        if ct > awut:
          os.startfile(fullname)
          print(fullname)
          print(ct, awut)
        time.sleep(1*10)
