import pyautogui as pa
import time
import pyperclip

pa.PAUSE = 3

pa.hotkey('ctrl', 'Shift', '`')
pa.write("git add .")
pa.press('ENTER')
pa.write("git commit -m '1.9'")
pa.press('ENTER')
time.sleep(3)
pa.write("git push")
pa.press('ENTER')
