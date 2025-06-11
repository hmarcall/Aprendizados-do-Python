import pyautogui
import time

print("Você tem 5 segundos para posicionar o mouse sobre o botão 'Escrever' no Gmail...")
time.sleep(5)
print("Posição atual do mouse:", pyautogui.position())
