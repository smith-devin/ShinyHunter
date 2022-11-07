import time
import pyautogui
from GbaWindow import GbaWindow
from EmailService import EmailService
from ShinyPokemonBot import ShinyPokemonBot

if __name__ == '__main__':
    error = 0
    counter = 1
    startTime = time.time()
    time.sleep(3)

    # Open the gba emulator
    gbaWindow = GbaWindow()
    gbaWindow.openGame()
    gbaWindow.resizeWindow()
    gbaWindow.loadGame()
    
    # Start checking for shiny pokemon
    while True:
        gbaWindow.toggleFastForward(True)
        isShinyPokemonFound, filepath = ShinyPokemonBot.run()

        if isShinyPokemonFound:
            try:
                backpackfound = pyautogui.locateOnScreen("images\\backpack.png")
                error += 1
            except:
                EmailService.sendEmailWithImage("SHINY ALERT", f"You found a shiny pokemon after {counter} iterations! It took {time.time() - startTime} seconds. Number of false positives: {error}", "smithdevin6@gmail.com", filepath)
                gbaWindow.saveGame()
                break
        else:
            gbaWindow.loadGame()

        print(f'\rNumber of iterations: {counter}  Time elapsed: {time.time() - startTime}', "Number of false positives: {error}", end='')
        counter += 1

    gbaWindow.kill()