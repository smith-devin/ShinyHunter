import time
import subprocess
import win32gui
import win32process
import pyautogui
import pydirectinput

class GbaWindow:
    def __init__(self, x_resize, y_resize, w_resize, h_resize, x_open_load, y_open_load):
        self.gba = subprocess.Popen("C:\\Users\\moonc\\OneDrive\\Desktop\\Games\\VisualBoyAdvance.exe") 
        self.hwnd = None
        self.x_resize = x_resize
        self.y_resize = y_resize
        self.w_resize = w_resize
        self.h_resize = h_resize
        self.x_open_load = x_open_load
        self.y_open_load = y_open_load

        time.sleep(.5)
        self.findGbaWindow()
        self.resizeWindow()
        self.openGame()
        self.resizeWindow()
        self.loadGame()

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
        win32gui.MoveWindow(self.hwnd, self.x_resize, self.y_resize, self.w_resize, self.h_resize, True)

    def openGame(self):
        win32gui.SetForegroundWindow(self.hwnd)

        with pyautogui.hold('ctrl'):
            pyautogui.press('o')

        time.sleep(.5)

        pyautogui.click(self.x_open_load, self.y_open_load, button='left')
        pyautogui.click(self.x_open_load, self.y_open_load + 250, button='left')

    def loadGame(self):
        win32gui.SetForegroundWindow(self.hwnd)

        with pyautogui.hold('ctrl'):
            pyautogui.press('l')

        time.sleep(.5)

        pyautogui.click(self.x_open_load, self.y_open_load + 40, button='left')
        pyautogui.click(self.x_open_load, self.y_open_load + 250, button='left')
           

    def saveGame(self):
        win32gui.SetForegroundWindow(self.hwnd)

        with pyautogui.hold('ctrl'):
            pyautogui.press('s')

        time.sleep(.5)

        pyautogui.click(self.x_open_load, self.y_open_load + 70, button='left')
        pyautogui.click(self.x_open_load, self.y_open_load + 270, button='left')
        

    def toggleFastForward(self, command):
        pydirectinput.FAILSAFE = False
        
        if command == True:
            pydirectinput.keyDown('space')
        else:
            pydirectinput.keyUp('space')

    def kill(self):
        subprocess.Popen.kill(self.gba)

      