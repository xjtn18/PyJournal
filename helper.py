from os import system, name
import os.path
import pickle
import time
from datetime import datetime
from helper import *
from constants import *


def pause(sec : float):
    time.sleep(sec)


def screen_clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def yes_no(question : str) -> bool:
    while True:
        response = input(question + " (y/n) ")
        if response not in 'yn':
            print("invalid: 'y' or 'n'")
            pause(PAUSE_TIME)
            continue
        return response == 'y'


def add_escapes(s : str) -> str:
    res = ''
    for i in range(len(s)):
        res += s[i] if s[i] not in SYMBOLS else '\\' + s[i]

    return res


