import pyautogui
from time import sleep
import os

# - Clicar no botão iniciar do Windows
pyautogui.click(441,743, duration=2)
# Clicar no botão de pesquisa do Windows
pyautogui.click(431,85, duration=2)
pyautogui.write('Opera')
pyautogui.press('enter')
# 1-Clicar no Opera
#pyautogui.click(730,745, duration=2)
# 2-Clicar no Youtube
pyautogui.click(911,102, duration=3)
# 3-Clicar no campo de pesquisa
pyautogui.click(410,150, duration=3)
pyautogui.write('Liniker Caju')
# 4-Digitar o nome da musica
pyautogui.click(948,155, duration=2)

# 5-Clicar em pesquisar
pyautogui.click(364,335, duration=2)
# 6-Dar play na musica

