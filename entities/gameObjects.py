import random, pygame

class Ball(object):

    def __init__(self, screenW, screenH):
        self.ballRadius = 5
        self.ballXSpeed = 1.25
        self.ballYSpeed = 1 + random.random()
        self.ballAngle = 45
        self.ballStartPos = [screenW - 20, screenH - 20]
        self.ballCurPos = self.ballStartPos
        self.ballColor = (0, 0, 0)

    def updateBallPos(self):
        self.ballCurPos[0] -= self.ballXSpeed
        self.ballCurPos[1] -= self.ballYSpeed

    def drawBall(self, gameSurface):
        pygame.draw.circle(gameSurface, self.ballColor, self.ballCurPos, self.ballRadius)

    def flipBallYSpeed(self, topOrBot):
        if topOrBot:
            self.ballYSpeed = -abs(self.ballYSpeed)
        else:
            self.ballYSpeed = abs(self.ballYSpeed)
    
    def flipBallXSpeed(self):
        self.ballXSpeed = -self.ballXSpeed

class Paddle(object):

    def __init__(self):
        self.rectSize = self.rectWidth, self.rectHeight = 10, 100
        self.rectStartPos = self.rectStartX, self.rectStartY = 0, 0
        self.rectSpeed = 1
        self.gameRect = pygame.Rect(self.rectStartX, self.rectStartY, self.rectWidth, self.rectHeight)
        self.rectColor = (180, 20, 180)

    def paddleMove(self, up):
        if not up:
            self.gameRect.move_ip(0, +self.rectSpeed)
        else:
            self.gameRect.move_ip(0, -self.rectSpeed)

    def updateRect(self, gameSurface):
        pygame.draw.rect(gameSurface, self.rectColor, self.gameRect)

    