import sys
import pyautogui
import keyboard
from time import sleep
autoclick = False


def stop_autoclick():
    global autoclick
    autoclick = False
    print('stopped')


def start_autoclick():
    global autoclick
    autoclick = True
    print('started')


keyboard.add_hotkey('ctrl + shift + [', start_autoclick, args=())
keyboard.add_hotkey('ctrl + shift + ]', stop_autoclick, args=())
keyboard.add_hotkey('ctrl + shift + /', sys.exit, args=())

print('program running')
while True:
    while autoclick:
        print('auto-clicking is a go')
        pyautogui.tripleClick()
        sleep(0.02)


#made by Ludimeus, have fun!
