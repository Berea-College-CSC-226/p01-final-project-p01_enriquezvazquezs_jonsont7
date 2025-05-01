from pdb import post_mortem

import pygame, random, math
from NPC import NPC

class Enemy_NPC(NPC):
    def __init__(self, screen_size, imgName, position = [0, 0]):
        super().__init__(screen_size, imgName)
        # self.path_points = path_points  # II.A.1: list of (x, y) points
        self.path_index = 0  # current target index in the path
        # self.detection_radius = detection_radius
        self.following_mouse = False
        self.mouse_target = None
        self.rect.move_ip(position[0], position[1])
        self.direction = 0

    def moveUp(self):
        self.rect.move_ip(0, -self.move_distance)

    def moveDown(self):
        self.rect.move_ip(0, self.move_distance)

    def moveRight(self):
        self.rect.move_ip(self.move_distance, 0)

    def moveLeft(self):
        self.rect.move_ip(-self.move_distance, 0)

    def moveForward(self):
        if self.direction == 0:
            self.moveRight()
        elif self.direction == 1:
            self.moveUp()
        elif self.direction == 2:
            self.moveLeft()
        else:
            self.moveDown()

    def turnLeft(self):
        if self.direction == 3:
            self.direction = 0
        else:
            self.direction += 1

    def turnRight(self):
        if self.direction == 0:
            self.direction = 3
        else:
            self.direction -= 1

    def pathway1(self):
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
        pass