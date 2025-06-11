import pyautogui
import time
import webbrowser
import pyperclip


webbrowser.open("https://mail.google.com")
time.sleep(5)

pyautogui.click(x=150, y=200)
time.sleep(3)

with open("Automacao/Auto email/email.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

destinatario = linhas[0].split(":", 1)[1].strip()
assunto = linhas[1].split(":", 1)[1].strip()
mensagem = linhas[2].split(":", 1)[1].strip()

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
time.sleep(1)

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
time.sleep(1)

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")