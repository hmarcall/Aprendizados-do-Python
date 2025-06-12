import pyautogui
import time
import webbrowser

webbrowser.open("https://mail.google.com")
time.sleep(15)  # tempo para carregar o Gmail

# Descubra a posição do botão escrever antes com print(pyautogui.position())
pyautogui.moveTo(128, 178, duration=1)
pyautogui.click()
