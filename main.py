import time
from GbaWindow import GbaWindow
from EmailService import EmailService
from ShinyPokemonBot import ShinyPokemonBot

if __name__ == '__main__':
    counter = 1
    startTime = time.time()
    time.sleep(3)

    # Open the gba emulator #1
    gbaWindow = GbaWindow()
    gbaWindow.resizeWindow(1713, 0, 1735, 720)
    gbaWindow.openGame(True)
    gbaWindow.resizeWindow(1713, 0, 1735, 720)
    gbaWindow.loadGame(True)

    # Open the gba emulator #2
    gbaWindow = GbaWindow()
    gbaWindow.resizeWindow(1713, 710, 1735, 720)
    gbaWindow.openGame(False)
    gbaWindow.resizeWindow(1713, 710, 1735, 720)
    gbaWindow.loadGame(False)
    
    # Start checking for shiny pokemon
    while True:
        gbaWindow.toggleFastForward(True)
        isShinyPokemonFound, filepath, isTop = ShinyPokemonBot.run()

        if isShinyPokemonFound:
            EmailService.sendEmailWithImage("SHINY ALERT", f"You found a shiny pokemon! Iterations: {counter}  Time(seconds): {int(time.time() - startTime)}", "smithdevin6@gmail.com", filepath)
            gbaWindow.saveGame(isTop)
            break
        else:
            gbaWindow.loadGame(True)
            gbaWindow.loadGame(False)
        
        print(f'\rIterations: {counter}  Time(seconds): {int(time.time() - startTime)}', end='')
        counter += 2

    gbaWindow.kill()