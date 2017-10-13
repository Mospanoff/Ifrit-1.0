import time
from random import choice
import os
import glob
import responses
from Pascal import run_transcription_loop_slave as rtls
from Pascal import speak as speak



def alarm():
    true_files = glob.glob('D:\Phone_sync\Music\*.mp3')
    folder = ('D:\Phone_sync\Music')
    file = os.listdir(folder)
    print(file)

