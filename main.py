import pygame

from player import Player

pygame.init()

#Always Global

WIDTH, HEIGHT = 145, 90
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("application")
clock = pygame.time.Clock()
FPS = 144
gameState = "startScreen"


running = True

#Player's current level
with open("Player-Data\CurrentPlayerLevel.txt") as level:
  playerLevel = int(level.read())

def openStartScreen():
    global WIDTH, HEIGHT, screen, clock, FPS, gameState
    playAndLevelsButtonsFont = pygame.font.SysFont(None, 24)
    quitFont = pygame.font.SysFont(None, 12)
    startScreenRunning = True
    menuIndex = 0
    while startScreenRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState = "endGame"
                startScreenRunning = False
                continue
            # Key Checks
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameState = "endGame"
                    startScreenRunning = False
                    continue
                # Menu Highlight / Selection Change
                if event.key == pygame.K_DOWN:
                    if menuIndex < 2:
                        menuIndex += 1
                if event.key == pygame.K_UP:
                    if menuIndex > 0:
                        menuIndex -= 1
                #---

                # Menu Selection Interactions
                if event.key == pygame.K_SPACE:
                    if menuIndex == 0:
                        gameState = "gamePlay"
                        startScreenRunning = False
                        continue
                    elif menuIndex == 1:
                        gameState = "levelsMenu"
                        startScreenRunning = False
                        continue
                    elif menuIndex == 2:
                        gameState = "endGame"
                        startScreenRunning = False
                        continue
                #---


def openGamePlay(level):
    global WIDTH, HEIGHT, screen, clock, FPS, running, gameState

def incrementLevel():
    with open("Player-Data\CurrentPlayerLevel.txt") as currLevel:
        currLevel.write(str(int(currLevel.read())+1))

def openPauseMenu():
    global WIDTH, HEIGHT, screen, clock, FPS, running, gameState


def openLoseScreen():
    global WIDTH, HEIGHT, screen, clock, FPS, running, gameState


def openLevelsMenu():
    print()

while running:
    if gameState == "startScreen":
        openStartScreen()
    elif gameState == "gamePlay":
        openGamePlay(playerLevel)
    elif gameState == "paused":
        openPauseMenu()
    elif gameState == "loseScreen":
        openLoseScreen()
    elif gameState == "levelsMenu":
        openLevelsMenu()
    elif gameState == "endGame":
        running = False

pygame.quit()