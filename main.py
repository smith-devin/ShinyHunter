import time
from GbaWindow import GbaWindow
from EmailService import EmailService
from ShinyPokemonBot import ShinyPokemonBot

if __name__ == '__main__':
    # Setup the statistics variables 
    time.sleep(3)
    counter = 1

    startTime = time.time()
    time.sleep(1)

    # Open the gba emulator
    gbaWindow = GbaWindow()
    gbaWindow.openGame()
    gbaWindow.resizeWindow()
    gbaWindow.loadGame()
    
    # Start checking for shiny pokemon
    while True:
        gbaWindow.toggleFastForward(True)
        isShinyPokemonFound = ShinyPokemonBot.run()

        if isShinyPokemonFound:
            EmailService.sendEmailWithImage("SHINY ALERT", f"You found a shiny pokemon after {counter} iterations! It took {time.time() - startTime} seconds.", "smithdevin6@gmail.com", "images\shinySquirtle.png")
            gbaWindow.saveGame()
            break
        else:
            gbaWindow.loadGame()

        print(f'\rNumber of iterations: {counter}  Time elapsed: {time.time() - startTime}', end='')
        counter += 1

    gbaWindow.kill()