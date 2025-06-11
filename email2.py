import pyautogui
import time
import webbrowser
import pyperclip
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQLNV87-CA9wsG9KFXEN5v1DbEmnPy0AP4DNLITjOYKR0NNgdeteWVtchsj8M_ldsmS0uxjY0M9QE8x/pub?output=csv'
df = pd.read_csv(url)

webbrowser.open("https://mail.google.com")
time.sleep(5)

for index, row in df.iterrows():
    nome = row['Nome']
    email = row['Email']

    assunto = f"Relatório Atualizado - {nome}"
    mensagem = f"""
Olá {nome},

Segue abaixo o relatório atualizado com suas informações:

{row.drop(labels=['Timestamp']).to_string()}

Atenciosamente,
Kayk
"""

    pyautogui.click(x=128, y=178)
    time.sleep(4)

    pyperclip.copy(email)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")
    time.sleep(2)

    pyperclip.copy(assunto)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")
    time.sleep(2)

    pyperclip.copy(mensagem)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)

    pyautogui.hotkey("ctrl", "enter")
    time.sleep(3)
