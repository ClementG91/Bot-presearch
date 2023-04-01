from random_word import RandomWords
import pyautogui
import webbrowser
import time
import os


r = RandomWords()

url = 'https://www.presearch.com/'

for i in range (2):
    random_word = r.get_random_word()
    webbrowser.open_new(url)
    time.sleep(3)
    pyautogui.typewrite(random_word)
    time.sleep(3)
    pyautogui.hotkey('enter')
    time.sleep(5)
os.system("taskkill /im brave.exe /f")