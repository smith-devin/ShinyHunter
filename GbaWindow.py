import time
import subprocess
import win32gui
import win32process
import pyautogui
import pydirectinput

class GbaWindow:
    def __init__(self):
        self.gba = subprocess.Popen("C:\\Users\\moonc\\OneDrive\\Desktop\\Games\\VisualBoyAdvance.exe") 
        self.hwnd = None

        time.sleep(.5)
        self.findGbaWindow()
        self.resizeWindow()

    def findGbaWindow(self):
        def callback (hwnd, hwnds):
            if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
                _, found_pid = win32process.GetWindowThreadProcessId (hwnd)

                if found_pid == self.gba.pid:
                    hwnds.append (hwnd)

            return True
        
        # Make a list of py handle windows and get the one that matches our pid
        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        self.hwnd = hwnds[0]

    def resizeWindow(self):
        win32gui.MoveWindow(self.hwnd, 1713, 0, 1735, 1440, True)

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

        pyautogui.click(x=2500, y=645, button='left')

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

      