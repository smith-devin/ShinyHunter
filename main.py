import time
from GbaWindow import GbaWindow
from EmailService import EmailService
from ShinyPokemonBot import ShinyPokemonBot

if __name__ == '__main__':
    counter = 2
    x = 700
    y = 0
    yBottom = 700
    width = 700
    height = 720
    offset = 20
    openGameHeightTop = 250
    openGameHeightBottom = 945

    # Open the gba emulator #1
    gbaWindowOne = GbaWindow()
    gbaWindowOne.resizeWindow(x, y, width, height)
    gbaWindowOne.openGame(x1=1284, y1=openGameHeightTop, x2=1284, y2=(openGameHeightTop * 2))
    gbaWindowOne.resizeWindow(x, y, width, height)
    gbaWindowOne.loadGame(x1=1284, y1=285, x2=1284, y2=(openGameHeightTop * 2))

    # Open the gba emulator #2
    gbaWindowTwo = GbaWindow()
    gbaWindowTwo.resizeWindow(x + width - offset, y, width, height)
    gbaWindowTwo.openGame(x1=1965, y1=openGameHeightTop, x2=1965, y2=(openGameHeightTop * 2))
    gbaWindowTwo.resizeWindow(x + width - offset, y, width, height)
    gbaWindowTwo.loadGame(x1=1965, y1=285, x2=1965, y2=(openGameHeightTop * 2))

    # Open the gba emulator #3
    gbaWindowThree = GbaWindow()
    gbaWindowThree.resizeWindow(x + (width * 2) - (offset * 2), y, width, height)
    gbaWindowThree.openGame(x1=2650, y1=openGameHeightTop, x2=2650, y2=(openGameHeightTop * 2))
    gbaWindowThree.resizeWindow(x + (width * 2) - (offset * 2), y, width, height)
    gbaWindowThree.loadGame(x1=2650, y1=285, x2=2650, y2=(openGameHeightTop * 2))
    
    # Open the gba emulator #4
    gbaWindowFour = GbaWindow()
    gbaWindowFour.resizeWindow(x + (width * 3) - (offset * 3), y, width, height)
    gbaWindowFour.openGame(x1=3329, y1=openGameHeightTop, x2=3329, y2=(openGameHeightTop * 2))
    gbaWindowFour.resizeWindow(x + (width * 3) - (offset * 3), y, width, height)
    gbaWindowFour.loadGame(x1=3329, y1=285, x2=3329, y2=(openGameHeightTop * 2))

    # Open the gba emulator #5
    gbaWindowFive = GbaWindow()
    gbaWindowFive.resizeWindow(x, yBottom, width, height)
    gbaWindowFive.openGame(x1=1284, y1=openGameHeightBottom, x2=1284, y2=(openGameHeightBottom + 250))
    gbaWindowFive.resizeWindow(x, yBottom, width, height)
    gbaWindowFive.loadGame(x1=1284, y1=980, x2=1284, y2=(openGameHeightBottom + 250))

    # Open the gba emulator #6
    gbaWindowFive = GbaWindow()
    gbaWindowFive.resizeWindow(x + width - offset, yBottom, width, height)
    gbaWindowFive.openGame(x1=1967, y1=openGameHeightBottom, x2=1967, y2=(openGameHeightBottom + 250))
    gbaWindowFive.resizeWindow(x + width - offset, yBottom, width, height)
    gbaWindowFive.loadGame(x1=1967, y1=980, x2=1967, y2=(openGameHeightBottom + 250))

    # Open the gba emulator #7
    gbaWindowFive = GbaWindow()
    gbaWindowFive.resizeWindow(x + (width * 2) - (offset * 2), yBottom, width, height)
    gbaWindowFive.openGame(x1=2649, y1=openGameHeightBottom, x2=2649, y2=(openGameHeightBottom + 250))
    gbaWindowFive.resizeWindow(x + (width * 2) - (offset * 2), yBottom, width, height)
    gbaWindowFive.loadGame(x1=2649, y1=980, x2=2649, y2=(openGameHeightBottom + 250))

    # Open the gba emulator #8
    gbaWindowFive = GbaWindow()
    gbaWindowFive.resizeWindow(x + (width * 3) - (offset * 3), yBottom, width, height)
    gbaWindowFive.openGame(x1=3329, y1=openGameHeightBottom, x2=3329, y2=(openGameHeightBottom + 250))
    gbaWindowFive.resizeWindow(x + (width * 3) - (offset * 3), yBottom, width, height)
    gbaWindowFive.loadGame(x1=3329, y1=980, x2=3329, y2=(openGameHeightBottom + 250))

    startTime = time.time()

    # Start checking for shiny pokemon
    while True:
        gbaWindowOne.toggleFastForward(True) # only need one to do this
        isShinyPokemonFound, filepath, window = ShinyPokemonBot.run()

        if isShinyPokemonFound:
            EmailService.sendEmailWithImage("SHINY ALERT", f"You found a shiny pokemon! Iterations: {counter}  Time(seconds): {int(time.time() - startTime)}", "smithdevin6@gmail.com", filepath)
            
            if window == 1:
                gbaWindowOne.saveGame(x1=2500, y1=246, x2=2810, y2=489)
            elif window == 2:
                gbaWindowOne.saveGame(x1=2500, y1=246, x2=2810, y2=489)
            elif window == 3:
                gbaWindowOne.saveGame(x1=2500, y1=246, x2=2810, y2=489)
            elif window == 4:
                gbaWindowOne.saveGame(x1=2500, y1=246, x2=2810, y2=489)
            elif window == 5:
                gbaWindowOne.saveGame(x1=2500, y1=246, x2=2810, y2=489)
            elif window == 6:
                gbaWindowOne.saveGame(x1=2500, y1=246, x2=2810, y2=489)
            elif window == 7:
                gbaWindowTwo.saveGame(x1=2500, y1=957, x2=2810, y2=1204)
            elif window == 8:
                gbaWindowOne.saveGame(x1=2500, y1=246, x2=2810, y2=489)
            
            break
        else:
            gbaWindowOne.loadGame(x1=2500, y1=285, x2=2810, y2=489)
            gbaWindowTwo.loadGame(x1=2500, y1=1000, x2=2810, y2=1204)
        
        print(f'\rIterations: {counter}  Time(seconds): {int(time.time() - startTime)}', end='')
        counter += 2

    gbaWindowOne.kill()
    gbaWindowTwo.kill()
    gbaWindowThree.kill()
    gbaWindowFour.kill()