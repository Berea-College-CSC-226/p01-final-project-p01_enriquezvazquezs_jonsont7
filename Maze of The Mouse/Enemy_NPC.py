from pdb import post_mortem

import pygame, random, math
from NPC import NPC

class Enemy_NPC(NPC):
    def __init__(self, screen_size, position = [0, 0]):
        super().__init__(screen_size)
        # self.path_points = path_points  # II.A.1: list of (x, y) points
        self.path_index = 0  # current target index in the path
        # self.detection_radius = detection_radius
        self.following_mouse = False
        self.mouse_target = None
        self.rect.move_ip(position[0], position[1])

    def moveUp(self):
        self.rect.move_ip(0, -self.move_distance)

    def moveDown(self):
        self.rect.move_ip(0, self.move_distance)

    def moveRight(self):
        self.rect.move_ip(self.move_distance, 0)

    def moveLeft(self):
        self.rect.move_ip(-self.move_distance, 0)

    def pathway1(self):
        pass

    def pathway2(self):
        pass