import pyautogui
import time

print("Movendo o mouse em 3 segundos...")
time.sleep(3)
pyautogui.moveTo(500, 500, duration=1)
