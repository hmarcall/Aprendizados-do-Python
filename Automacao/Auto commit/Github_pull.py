import pyautogui as pa
import time

pa.PAUSE = 2
for tecla in ['`', "'"]:
    pa.hotkey('ctrl', 'shift', tecla)
pa.write('git pull')
pa.press('ENTER')