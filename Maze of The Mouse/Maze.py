import pygame
import Boundary
import game

class Maze:
    def __init__(self, matrix):
        self.matrix = matrix
        self.boundaries = []

    def makeBoundaries(self):
        """
        Makes the boundaries of the maze

        :return: None
        """
        xPos = 0
        yPos = 0
        for row in self.matrix:
            for cell in row:
                if cell:
                    self.boundaries.append(Boundary.Boundary([xPos, yPos]))
                xPos += 50
            xPos = 0
            yPos += 50


    def drawMaze(self, screen):
        """
        Displays boundaries in the Maze

        :param screen: Screen size, for keeping character on the screen
        :return: None
        """
        for boundary in self.boundaries:
            screen.blit(boundary.surf, boundary.rect)
