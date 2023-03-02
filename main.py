import random, pygame, sys
from entities import gameObjects
from model import gameData
from view import displayUpdate

#game screen
screen = displayUpdate.ScreenInfo()

#rectangle obj
paddle = gameObjects.Paddle()

#ball obj
ball = gameObjects.Ball(screen.SCREEN_WIDTH, screen.SCREEN_HEIGHT)

#game data
data = gameData.Data()

pygame.init()

#font
myFont = pygame.font.SysFont("Times New Roman", 18)

#window title
pygame.display.set_caption("Pong But Better")

#set screen and screen size
surface = pygame.display.set_mode(screen.SCREEN_SIZE)

#instance of the game ball
screen.drawBall(ball)

#Game loop
while data.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            data.running = False
            pygame.quit()
            sys.exit()
    #change back to 30
    if data.rallies >= 10 or data.lives <= 0:
        data.winLose = True
        ball.ballXSpeed = 0
        ball.ballYSpeed = 0

    #color the screen
    surface.fill(screen.screenColor)
    #make sure rect dont move out of screen
    paddle.gameRect.clamp_ip(surface.get_rect())
    #check keys pressed
    keys = pygame.key.get_pressed()
    #check keys pressed to update game rect position
    if keys[pygame.K_DOWN] and (paddle.gameRect.y + paddle.rectHeight) < screen.SCREEN_HEIGHT and not data.winLose:
        paddle.paddleMove(False)
    elif keys[pygame.K_UP] and paddle.gameRect.y > 0 and not data.winLose:
        paddle.paddleMove(True)

    #bool for collisions with ball
    col = paddle.gameRect.collidepoint(ball.ballCurPos[0], ball.ballCurPos[1])
    #if the collide bool is true (a collision between gameRect and ball has happened)
    if (col):
        #check for collide position so the ball bounces off at weird angles
        if(ball.ballCurPos[0] <= paddle.rectWidth and ball.ballCurPos[0] > 0):
            ball.ballCurPos[0] = paddle.rectWidth + ball.ballRadius
        colPos = ball.ballCurPos[1]
        #if the ball hit the top half of the paddle
        if colPos >= paddle.gameRect.y and colPos <= paddle.gameRect.y + (paddle.rectHeight / 2):
            #send tht thing up
            ball.ballYSpeed = -abs(ball.ballYSpeed)
        #if the ball hit the bottom half of the paddle
        elif colPos >= paddle.gameRect.y + (paddle.rectHeight/2) and colPos <= paddle.gameRect.y + paddle.rectHeight:
            #send tht thing down
            ball.ballYSpeed = abs(ball.ballYSpeed)
        #invert X speed either way
        ball.ballXSpeed = ball.ballXSpeed * -1
        #increment rallied obj
        data.updateRallyCounter()
    #if the ball hit the top or bottom of the screen
    if (ball.ballCurPos[1] + ball.ballRadius <= 0) or (ball.ballCurPos[1] + ball.ballRadius >= screen.SCREEN_HEIGHT):
        #invert the ballYSpeed
        ball.ballYSpeed = ball.ballYSpeed * -1
    #if the ball hit the right side of the screen
    if (ball.ballCurPos[0] + ball.ballRadius >= screen.SCREEN_WIDTH):
        #invert ballXSpeed
        ball.ballXSpeed = ball.ballXSpeed * -1
    #if the ball hit the left side of the screen (and missed the paddle)
    if (ball.ballCurPos[0] - ball.ballRadius <= 0):
        #invert ballXSpeed
        ball.ballXSpeed = ball.ballXSpeed * -1
        #decrement lives obj
        data.updateLivesCounter()
    

    #Display Labels
    RallyLabel = myFont.render("Rallies: ", 1, (0, 0, 0))
    RallyDisplay = myFont.render(str(data.rallies), 1, (0, 0, 0))
    LivesLabel = myFont.render("Lives: ", 1, (0, 0, 0))
    LivesDisplay = myFont.render(str(data.lives), 1, (0, 0, 0))

    #thing tht make label appear
    surface.blit(RallyLabel, (0, 100))
    surface.blit(RallyDisplay, (65, 100))  
    surface.blit(LivesLabel, (0, 150))
    surface.blit(LivesDisplay, (65, 150))

    #helper call
    ball.updateBallPos()
    
    #update displays
    screen.updateDisp(paddle, ball)

    
    if data.rallies >= 10 and data.lives > 0:
        WinLabel = myFont.render("You WIN!!", 1, (0, 0, 0))
        surface.blit(WinLabel, (screen.SCREEN_WIDTH/2, screen.SCREEN_HEIGHT/2))
    elif data.rallies < 10 and data.lives <= 0:
        WinLabel = myFont.render("You Lose.", 1, (0, 0, 0))
        surface.blit(WinLabel, (screen.SCREEN_WIDTH/2, screen.SCREEN_HEIGHT/2))
    

    #update screen
    pygame.display.update()
