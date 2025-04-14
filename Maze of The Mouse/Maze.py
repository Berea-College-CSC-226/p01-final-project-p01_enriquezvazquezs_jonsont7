import pygame
import Boundary
import game

class Maze:
    def __init__(self, matrix, size):
        self.matrix = matrix
        self.size = size
        self.cellHeight = size[1]/len(matrix[0])
        self.cellWidth = size[0]/len(matrix)
        self.boundaries = []

    def makeBoundaries(self):
        """
        Makes the boundaries of the maze
        :return:
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
        for boundary in self.boundaries:
            screen.blit(boundary.surf, boundary.rect)
