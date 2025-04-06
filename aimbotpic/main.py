import pyautogui as pg
import time as t
import os

t.sleep(3)
print('ctrl+c at terminal to stop the code')
key = r'C:\Users\460226\Desktop\coding\pyautoguitest\aimcheating\bot.png'

while True:
    try:
        find = pg.locateCenterOnScreen(key,confidence=0.8)
        if find is not None:
            x,y=find
            pg.click(x,y)
    except pg.ImageNotFoundException:
        pass
    t.sleep(0.05)