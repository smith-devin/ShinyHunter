import time
import pyautogui
import pydirectinput
from datetime import datetime

class ShinyPokemonBot:
    def pressA(time):
        pydirectinput.press('z', interval=time)

    def pressB(time):
        pydirectinput.press('x', interval=time)

    def pressUp(time):
        pydirectinput.press('up', interval=time)
        
    def pressDown(time):
        pydirectinput.press('down', interval=time)

    def pressLeft(time):
        pydirectinput.press('left', interval=time)

    def pressRight(time):
        pydirectinput.press('right', interval=time)

    def toggleFastForward(command):
        if command == True:
            pydirectinput.keyDown('space')
        else:
            pydirectinput.keyUp('space')

    def debugTrainerNumber():
        pydirectinput.press('enter') # open menu
        ShinyPokemonBot.pressDown(.2)
        ShinyPokemonBot.pressA(.2)

        trainerID = pyautogui.screenshot()
        filepath = 'images\TID_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
        trainerID.save(filepath)

        ShinyPokemonBot.pressB(.2)
        ShinyPokemonBot.pressB(.2)
    
    def advanceToSquirtle():
        # Choose a trainer name
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)

        ShinyPokemonBot.pressDown(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)

        time.sleep(.5)
        
        # Debug
        #ShinyPokemonBot.debugTrainerNumber()

        # Get out of bedroom
        ShinyPokemonBot.pressRight(.5)
        ShinyPokemonBot.pressUp(.5)
        ShinyPokemonBot.pressLeft(.5)

        # Get out of living room
        ShinyPokemonBot.pressDown(.5)
        ShinyPokemonBot.pressLeft(.2)
        ShinyPokemonBot.toggleFastForward(False)
        ShinyPokemonBot.pressLeft(.2)
        ShinyPokemonBot.toggleFastForward(True)
        ShinyPokemonBot.pressDown(.2)

        # Go to Prof. Oak
        ShinyPokemonBot.pressRight(.2)
        ShinyPokemonBot.toggleFastForward(False)
        ShinyPokemonBot.pressRight(.2)
        ShinyPokemonBot.toggleFastForward(True)

        ShinyPokemonBot.pressUp(.2)
        ShinyPokemonBot.pressUp(.2)

        time.sleep(.5)

        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)

        time.sleep(1)

        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)

        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)

        ShinyPokemonBot.toggleFastForward(False)

        ShinyPokemonBot.pressDown(.2)
        ShinyPokemonBot.pressDown(.2)

        ShinyPokemonBot.pressRight(.2)
        ShinyPokemonBot.pressRight(.2)
        ShinyPokemonBot.pressRight(.2)
        ShinyPokemonBot.pressRight(.2)

        ShinyPokemonBot.pressUp(.2)

        ShinyPokemonBot.toggleFastForward(True)

    def getSquirtle():
        # Accept pokemon
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)

        # Advance dialouge 
        ShinyPokemonBot.pressA(.2)
        time.sleep(1)

        # Decline to nickname
        ShinyPokemonBot.pressDown(.2)
        ShinyPokemonBot.pressB(.2)

        # Advance dialouge 
        time.sleep(1)
        ShinyPokemonBot.pressA(.2)

    def checkForShinySquirtle():
        pydirectinput.press('enter') # open menu
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)

        squirtleShellColor = pyautogui.pixel(2076, 623)

        if squirtleShellColor == (184, 104, 0):
            return False, ""
        else:
            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)
            return True, filepath

    def run():
        ShinyPokemonBot.advanceToSquirtle()
        ShinyPokemonBot.getSquirtle()
        isShinyPokemonFound = ShinyPokemonBot.checkForShinySquirtle()

        return isShinyPokemonFound

    






        

