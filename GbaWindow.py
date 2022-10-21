import time
import subprocess
import pyautogui
import pydirectinput

class GbaWindow:
    def __init__(self):
        self.gba = subprocess.Popen("") 
        self.hwnd = None

        time.sleep(.5)

    def openGame(self):
        with pyautogui.hold('ctrl'):
            pyautogui.press('o')

        time.sleep(.5)

        pyautogui.click(x=2500, y=607, button='left')

        pyautogui.click(x=2810, y=852, button='left')

    def loadGame(self):
        with pyautogui.hold('ctrl'):
            pyautogui.press('l')

        time.sleep(.5)

        pyautogui.click(x=2500, y=664, button='left')

        pyautogui.click(x=2810, y=852, button='left')

    def saveGame(self):
        with pyautogui.hold('f1'):
            pyautogui.press('s')

    def toggleFastForward(self, command):
        if command == True:
            pydirectinput.keyDown('space')
        else:
            pydirectinput.keyUp('space')

    def kill(self):
        subprocess.Popen.kill(self.gba)

      