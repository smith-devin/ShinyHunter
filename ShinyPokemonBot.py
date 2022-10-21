import time
import pyautogui
import pydirectinput

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
        
    def getSquirtle():
        time.sleep(.5)

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
        pydirectinput.press('enter') # open menux
        ShinyPokemonBot.pressA(.5)

        ShinyPokemonBot.pressA(.5)

        ShinyPokemonBot.pressA(.5)

        squirtleShellColor = pyautogui.pixel(2076, 623)

        if squirtleShellColor == (184, 104, 0):
            return False
        else:
            shinySquirtle = pyautogui.screenshot()
            shinySquirtle.save('images\shinySquirtle.png')
            return True 

    def run():
        ShinyPokemonBot.getSquirtle()
        isShinyPokemonFound = ShinyPokemonBot.checkForShinySquirtle()

        return isShinyPokemonFound

    






        

