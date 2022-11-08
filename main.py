import time
import pyautogui
from datetime import datetime
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
            backpackfound = pyautogui.locateOnScreen("images\\backpack.png", confidence=.7)
            
            if backpackfound is not None:
                error += 1
                gbaWindow.loadGame()
            else:
                EmailService.sendEmailWithImage("SHINY ALERT", f"You found a shiny pokemon! Iterations: {counter}  False positives: {error}  Time(seconds): {int(time.time() - startTime)}", "smithdevin6@gmail.com", filepath)
                gbaWindow.saveGame()
                break
        else:
            gbaWindow.loadGame()

        print(f'\rIterations: {counter}  False positives: {error}  Time(seconds): {int(time.time() - startTime)}', end='')
        counter += 1

    gbaWindow.kill()