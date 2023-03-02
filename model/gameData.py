import pygame, sys

class Data(object):

    def __init__(self):
        self.rallies = 0
        self.lives = 3
        self.running = True
        self.winLose = False

    def updateRallyCounter(self):
        self.rallies = self.rallies + 1

    def updateLivesCounter(self):
        self.lives = self.lives - 1
