import time
import pyautogui
import pydirectinput
import logging
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

        time.sleep(1)
        
        # Debug
        #ShinyPokemonBot.debugTrainerNumber()

        # Get out of bedroom
        ShinyPokemonBot.pressRight(.2)
        ShinyPokemonBot.pressRight(.2)

        ShinyPokemonBot.pressUp(.2)
        ShinyPokemonBot.pressUp(.2)

        ShinyPokemonBot.pressLeft(.2)

        time.sleep(1)

        # Get out of living room
        ShinyPokemonBot.pressDown(.2)
        ShinyPokemonBot.pressDown(.2)

        ShinyPokemonBot.pressLeft(.2)

        ShinyPokemonBot.toggleFastForward(False)
        ShinyPokemonBot.pressLeft(.2)
        ShinyPokemonBot.pressLeft(.2)
        ShinyPokemonBot.pressLeft(.2)
        ShinyPokemonBot.toggleFastForward(True)

        ShinyPokemonBot.pressDown(.2)

        time.sleep(1)
        
        # Go to Prof. Oak
        ShinyPokemonBot.pressRight(.2)
        
        ShinyPokemonBot.toggleFastForward(False)

        ShinyPokemonBot.pressRight(.2)
        ShinyPokemonBot.pressRight(.2)
        ShinyPokemonBot.pressRight(.2)

        ShinyPokemonBot.toggleFastForward(True)
        
        # Zoom up
        ShinyPokemonBot.pressUp(.2)
        ShinyPokemonBot.pressUp(.2)
        ShinyPokemonBot.pressUp(.2)

        time.sleep(1)

        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)
        ShinyPokemonBot.pressA(.2)

        time.sleep(3)

        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        ShinyPokemonBot.pressA(.4)
        
        ShinyPokemonBot.pressDown(.2)
        ShinyPokemonBot.pressRight(.2)
        ShinyPokemonBot.pressUp(.2)

    def getSquirtle():
        # Accept pokemon
        ShinyPokemonBot.pressA(.5)
        ShinyPokemonBot.pressA(.5)
        ShinyPokemonBot.pressA(.5)

        # Advance dialouge 
        ShinyPokemonBot.pressA(.5)
        time.sleep(1)

        # Decline to nickname
        ShinyPokemonBot.pressDown(.5)
        ShinyPokemonBot.pressB(.5)

        # Advance dialouge 
        time.sleep(1)
        ShinyPokemonBot.pressA(.5)

    def checkForShinySquirtle():
        pydirectinput.FAILSAFE = False
        pydirectinput.press('enter') # open menu
        ShinyPokemonBot.pressA(.5)
        ShinyPokemonBot.pressA(.5)
        ShinyPokemonBot.pressA(.5)

        logging.info('Begin shiny checking each emulator')

        squirtleShellColorOne = pyautogui.pixel(1907, 195)
        squirtleShellColorTwo = pyautogui.pixel(2387, 195)
        squirtleShellColorThree = pyautogui.pixel(2867, 195)
        squirtleShellColorFour = pyautogui.pixel(1907, 586)
        squirtleShellColorFive = pyautogui.pixel(2387, 586)
        squirtleShellColorSix = pyautogui.pixel(2867, 586)

        if squirtleShellColorOne == (104, 152, 24):
            logging.info('Squirtle one is shiny')
            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 1

        elif squirtleShellColorTwo == (104, 152, 24):
            logging.info('Squirtle two is shiny')
            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 2

        elif squirtleShellColorThree == (104, 152, 24):
            logging.info('Squirtle three is shiny')
            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 3

        elif squirtleShellColorFour == (104, 152, 24):
            logging.info('Squirtle four is shiny')
            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 4

        elif squirtleShellColorFive == (104, 152, 24):
            logging.info('Squirtle five is shiny')
            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 5

        elif squirtleShellColorSix == (104, 152, 24):
            logging.info('Squirtle six is shiny')
            shinySquirtle = pyautogui.screenshot()
            filepath = 'images\shiny_' + datetime.now().strftime('%m-%d-%Y_%Hh%Mm%Ss') + '.png'
            shinySquirtle.save(filepath)

            return True, filepath, 6
        else:
            logging.info('No squirtle is shiny')
            return False, "", None

    def run():
        ShinyPokemonBot.advanceToSquirtle()
        ShinyPokemonBot.getSquirtle()

        isShinyPokemonFound, filepath, window = ShinyPokemonBot.checkForShinySquirtle()
        return isShinyPokemonFound, filepath, window

    






        

