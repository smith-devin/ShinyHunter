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
        ShinyPokemonBot.pressDown(1)
        ShinyPokemonBot.pressA(1)

        trainerID = pyautogui.screenshot()
        filepath = 'images\TID_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
        trainerID.save(filepath)

        ShinyPokemonBot.pressB(1)
        ShinyPokemonBot.pressB(1)
    
    def advanceToSquirtle():
        # Choose a trainer name
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)

        ShinyPokemonBot.pressDown(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)

        time.sleep(3)
        
        # Debug
        #ShinyPokemonBot.debugTrainerNumber()

        # Get out of bedroom
        ShinyPokemonBot.pressRight(1)
        ShinyPokemonBot.pressUp(1)
        ShinyPokemonBot.pressLeft(1)

        # Get out of living room
        ShinyPokemonBot.pressDown(1)
        ShinyPokemonBot.pressLeft(1)
        ShinyPokemonBot.toggleFastForward(False)
        ShinyPokemonBot.pressLeft(1)
        ShinyPokemonBot.toggleFastForward(True)
        ShinyPokemonBot.pressDown(1)

        # Go to Prof. Oak
        ShinyPokemonBot.pressRight(1)
        ShinyPokemonBot.toggleFastForward(False)
        ShinyPokemonBot.pressRight(1)
        ShinyPokemonBot.toggleFastForward(True)

        ShinyPokemonBot.pressUp(1)
        ShinyPokemonBot.pressUp(1)

        time.sleep(1.5)

        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)

        time.sleep(1.5)

        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)

        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)

        ShinyPokemonBot.toggleFastForward(False)

        ShinyPokemonBot.pressDown(1)
        ShinyPokemonBot.pressDown(1)

        ShinyPokemonBot.pressRight(1)
        ShinyPokemonBot.pressRight(1)
        ShinyPokemonBot.pressRight(1)
        ShinyPokemonBot.pressRight(1)

        ShinyPokemonBot.pressUp(1)

        ShinyPokemonBot.toggleFastForward(True)

    def getSquirtle():
        # Accept pokemon
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)

        # Advance dialouge 
        ShinyPokemonBot.pressA(1)
        time.sleep(1.5)

        # Decline to nickname
        ShinyPokemonBot.pressDown(1)
        ShinyPokemonBot.pressB(1)

        # Advance dialouge 
        time.sleep(1.5)
        ShinyPokemonBot.pressA(1)

    def checkForShinySquirtle():
        pydirectinput.FAILSAFE = False
        pydirectinput.press('enter') # open menu
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)
        ShinyPokemonBot.pressA(1)

        squirtleShellColorOne = pyautogui.pixel(2076, 331)
        squirtleShellColorTwo = pyautogui.pixel(2076, 331)
        squirtleShellColorThree = pyautogui.pixel(2076, 331)
        squirtleShellColorFour = pyautogui.pixel(2076, 331)
        squirtleShellColorFive = pyautogui.pixel(2076, 331)
        squirtleShellColorSix = pyautogui.pixel(2076, 331)
        squirtleShellColorSeven = pyautogui.pixel(2076, 331)
        squirtleShellColorEight = pyautogui.pixel(2076, 331)

        if squirtleShellColorOne == (104, 152, 24):
            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 1

        elif squirtleShellColorTwo == (104, 152, 24):

            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 2

        elif squirtleShellColorThree == (104, 152, 24):

            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 3

        elif squirtleShellColorFour == (104, 152, 24):

            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 4

        elif squirtleShellColorFive == (104, 152, 24):

            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 5

        elif squirtleShellColorSix == (104, 152, 24):

            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 6

        elif squirtleShellColorSeven == (104, 152, 24):

            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 7

        elif squirtleShellColorEight == (104, 152, 24):

            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 8
        else:
            return False, "", None

    def run():
        ShinyPokemonBot.advanceToSquirtle()
        ShinyPokemonBot.getSquirtle()
        isShinyPokemonFound, filepath, isTop = ShinyPokemonBot.checkForShinySquirtle()
        return isShinyPokemonFound, filepath, isTop

    






        

