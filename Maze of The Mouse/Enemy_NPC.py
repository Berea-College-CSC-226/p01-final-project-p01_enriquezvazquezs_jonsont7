from pdb import post_mortem
from math import hypot
import pygame, random
from NPC import NPC

class Enemy_NPC(NPC):
    def __init__(self, screen_size, imgName, position = [0, 0]):
        """
        Represents the competitors of the players

        :param screen_size: Screen size, for keeping character on the screen
        :param imgName: Selects the image file
        :param position = [0, 0]: NPC sprite starting point
        """
        super().__init__(screen_size, imgName)
        self.rect.move_ip(position[0], position[1])
        self.direction = 0

    def moveUp(self):
        """
        Moves NPC sprite up on the screen

        :return: None
        """
        self.rect.move_ip(0, -self.move_distance)

    def moveDown(self):
        """
        Moves NPC sprite down on the screen

        :return: None
        """
        self.rect.move_ip(0, self.move_distance)

    def moveRight(self):
        """
        Moves NPC sprite right on the screen

        :return: None
        """
        self.rect.move_ip(self.move_distance, 0)

    def moveLeft(self):
        """
        Moves NPC sprite left on the screen

        :return: None
        """
        self.rect.move_ip(-self.move_distance, 0)

    def moveForward(self):
        """
        Moves NPC sprite forward on the screen

        :return: None
        """
        if self.direction == 0:
            self.moveRight()
        elif self.direction == 1:
            self.moveUp()
        elif self.direction == 2:
            self.moveLeft()
        else:
            self.moveDown()

    def turnLeft(self):
        """
        Turns NPC sprite left on the screen

        :return: None
        """
        if self.direction == 3:
            self.direction = 0
        else:
            self.direction += 1

    def turnRight(self):
        """
        Moves NPC sprite right on the screen

        :return: None
        """
        if self.direction == 0:
            self.direction = 3
        else:
            self.direction -= 1

    def pathway1(self):
        """
        Pathway of Taco Cat in the Maze

        :return: None
        """
        self.moveForward()
        print (str(self.rect.x) + ", " + str(self.rect.y))
        if self.rect.x == 580 and self.rect.y == 510:
            self.turnRight()
        if self.rect.x == 580 and self.rect.y == -5:
            self.turnRight()
        if self.rect.x == 765 and self.rect.y == 0:
            self.turnRight()
            self.turnRight()
        if self.rect.x == 570 and self.rect.y == 0:
            self.turnLeft()
        if self.rect.x == 570 and self.rect.y == 165:
            self.turnRight()
        if self.rect.x == 325 and self.rect.y == 165:
            self.turnLeft()
        if self.rect.x == 325 and self.rect.y == 380:
            self.turnLeft()
        if self.rect.x == 565 and self.rect.y == 375:
            self.turnRight()
        if self.rect.x == 565 and self.rect.y == 515:
            self.turnLeft()
        if self.rect.x == 725 and self.rect.y == 515:
            self.turnLeft()
        if self.rect.x == 725 and self.rect.y == 510:
            self.turnLeft()
    def pathway2(self):
        """
        Pathway of Whiskers on the Maze

        :return: None
        """
        self.moveForward()
        if self.rect.x == 200 and self.rect.y == 25:
            self.turnRight()
        if self.rect.x == 200 and self.rect.y == 275:
            self.turnLeft()
        if self.rect.x == 325 and self.rect.y == 275:
            self.turnLeft()
        if self.rect.x == 325 and self.rect.y == 150:
            self.turnRight()
        if self.rect.x == 575 and self.rect.y == 150:
            self.turnRight()
        if self.rect.x == 575 and self.rect.y == 400:
            self.turnRight()
        if self.rect.x == 300 and self.rect.y == 400:
            self.turnRight()
        if self.rect.x == 300 and self.rect.y == 280:
            self.turnLeft()
        if self.rect.x == 200 and self.rect.y == 280:
            self.turnLeft()
        if self.rect.x == 200 and self.rect.y == 550:
            self.turnRight()
        if self.rect.x == 195 and self.rect.y == 550:
            self.turnRight()
        if self.rect.x == 195 and self.rect.y == 30:
            self.turnLeft()
        if self.rect.x == 25 and self.rect.y == 30:
            self.turnRight()
        if self.rect.x == 25 and self.rect.y == 25:
            self.turnRight()
