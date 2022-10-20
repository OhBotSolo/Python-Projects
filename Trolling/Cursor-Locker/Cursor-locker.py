from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed("f") == False:
    click(1000, 0)
    click(0, 1000)
    click(50, 0)
    click(0, 50)
    click(500, 500)
