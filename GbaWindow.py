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

    def resizeWindow(self, x, y, width, height):
        win32gui.MoveWindow(self.hwnd, x, y, width, height, True)

    def openGame(self, x1, y1, x2, y2):
        win32gui.SetForegroundWindow(self.hwnd)

        with pyautogui.hold('ctrl'):
            pyautogui.press('o')

        time.sleep(.5)

        pyautogui.click(x1, y1, button='left')
        pyautogui.click(x2, y2, button='left')

    def loadGame(self, x1, y1, x2, y2):
        win32gui.SetForegroundWindow(self.hwnd)

        with pyautogui.hold('ctrl'):
            pyautogui.press('l')

        time.sleep(.5)

        pyautogui.click(x1, y1, button='left')
        pyautogui.click(x2, y2, button='left')
           

    def saveGame(self, x1, y1, x2, y2):
        win32gui.SetForegroundWindow(self.hwnd)

        with pyautogui.hold('ctrl'):
            pyautogui.press('s')

        time.sleep(.5)

        pyautogui.click(x1, y1, button='left')
        pyautogui.click(x2, y2, button='left')
        

    def toggleFastForward(self, command):
        pydirectinput.FAILSAFE = False
        
        if command == True:
            pydirectinput.keyDown('space')
        else:
            pydirectinput.keyUp('space')

    def kill(self):
        subprocess.Popen.kill(self.gba)

      