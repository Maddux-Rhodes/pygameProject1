import pygame, sys
class ScreenInfo(object):

    def __init__(self):
        self.SCREEN_SIZE = self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 800
        self.surface = pygame.display.set_mode(self.SCREEN_SIZE)
        self.screenColor = (50, 50, 50)

    def colorScreen(self):
        self.surface.fill(self.screenColor)

    def updateDisp(self, gameRect, gameBall):
        pygame.draw.rect(self.surface, gameRect.rectColor, gameRect.gameRect)
        pygame.draw.circle(self.surface, gameBall.ballColor, gameBall.ballCurPos, gameBall.ballRadius)
    
    def drawBall(self, gameBall):
        pygame.draw.circle(self.surface, gameBall.ballColor, gameBall.ballCurPos, gameBall.ballRadius)
