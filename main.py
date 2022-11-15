import time
from GbaWindow import GbaWindow
from EmailService import EmailService
from ShinyPokemonBot import ShinyPokemonBot

if __name__ == '__main__':
    counter = 6

    TOP_ROW_Y = 0
    TOP_ROW_OPEN_LOAD_Y = 98

    BOT_ROW_Y = 390
    BOT_ROW_OPEN_LOAD_Y = 480

    LEFT_COLUMN_X = 1800
    LEFT_OPEN_LOAD_X = 2287
    
    MIDDLE_COLUMN_X = LEFT_COLUMN_X + 480
    MIDDLE_OPEN_LOAD_X = LEFT_OPEN_LOAD_X + 480

    RIGHT_COLUMN_X = MIDDLE_COLUMN_X + 480
    RIGHT_OPEN_LOAD_X = MIDDLE_OPEN_LOAD_X + 480
    
    WIDTH = 500
    HEIGHT = 400

    # Open the gba emulators
    gbaWindowOne   = GbaWindow(LEFT_COLUMN_X,   TOP_ROW_Y, WIDTH, HEIGHT, LEFT_OPEN_LOAD_X,   TOP_ROW_OPEN_LOAD_Y)
    gbaWindowTwo   = GbaWindow(MIDDLE_COLUMN_X, TOP_ROW_Y, WIDTH, HEIGHT, MIDDLE_OPEN_LOAD_X, TOP_ROW_OPEN_LOAD_Y)
    gbaWindowThree = GbaWindow(RIGHT_COLUMN_X,  TOP_ROW_Y, WIDTH, HEIGHT, RIGHT_OPEN_LOAD_X,  TOP_ROW_OPEN_LOAD_Y)
    gbaWindowFour  = GbaWindow(LEFT_COLUMN_X,   BOT_ROW_Y, WIDTH, HEIGHT, LEFT_OPEN_LOAD_X,   BOT_ROW_OPEN_LOAD_Y)
    gbaWindowFive  = GbaWindow(MIDDLE_COLUMN_X, BOT_ROW_Y, WIDTH, HEIGHT, MIDDLE_OPEN_LOAD_X, BOT_ROW_OPEN_LOAD_Y)
    gbaWindowSix   = GbaWindow(RIGHT_COLUMN_X,  BOT_ROW_Y, WIDTH, HEIGHT, RIGHT_OPEN_LOAD_X,  BOT_ROW_OPEN_LOAD_Y)

    startTime = time.time()

    # Start checking for shiny pokemon
    while True:
        gbaWindowOne.toggleFastForward(True) # only need one to do this
        isShinyPokemonFound, filepath, window = ShinyPokemonBot.run()

        if isShinyPokemonFound:
            EmailService.sendEmailWithImage("SHINY ALERT", f"You found a shiny pokemon! Iterations: {counter}  Time(seconds): {int(time.time() - startTime)}", "smithdevin6@gmail.com", filepath)
            
            if window == 1:
                gbaWindowOne.saveGame()
            elif window == 2:
                gbaWindowTwo.saveGame()
            elif window == 3:
                gbaWindowThree.saveGame()
            elif window == 4:
                gbaWindowFour.saveGame()
            elif window == 5:
                gbaWindowFive.saveGame()
            else:
                gbaWindowSix.saveGame()
            
            break
        else:
            gbaWindowOne.loadGame() 
            gbaWindowTwo.loadGame()
            gbaWindowThree.loadGame()
            gbaWindowFour.loadGame()
            gbaWindowFive.loadGame()
            gbaWindowSix.loadGame()

        print(f'\rIterations: {counter}  Time(seconds): {int(time.time() - startTime)}', end='')
        counter += 6

    gbaWindowOne.kill()
    gbaWindowTwo.kill()
    gbaWindowThree.kill()
    gbaWindowFour.kill()
    gbaWindowFive.kill()
    gbaWindowSix.kill()