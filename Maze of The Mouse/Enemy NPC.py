from math import hypot

import pygame
import random
from NPC import NPC
import math

class Enemy_NPC(NPC):
    move_distance = 10
    directions = ["north", "east", "south", "west"]

    def __init__(self, screen_size):
        """
        Represents the Enemy NPC in the game.
        """
        super().__init__(screen_size)
        self.move_distance = 4

    def movement(self, others):
        """
        Moves the Enemy towards the mouse
        """

        self.move_towards_mouse(self.get_mouse(others))

    def get_mouse(self, others, mouse_pos=None):
        """
        Finds the closest cat from a list of other sprites.
        """
        mouse_positions = [(cat.rect.centerx, cat.rect.centery) for cat in others]
        min_distance = float('inf')
        mouse_close = None

        for cat_pos in mouse_positions:
            distance = self.calculation_mouse(self.rect.center, cat_pos)
            if distance < min_distance:
                min_distance = distance
                mouse_close = mouse_pos

        return mouse_close

    def calculation_mouse(self, pos1, pos2):
        """
        Calculates the Euclidean distance between two points.
        """
        a = pos1[0] - pos2[0]
        b = pos1[1] - pos2[1]
        return math.sqrt(a ** 2 + b ** 2)

    def move_towards_mouse(self, other):
        selfPos = (self.rect.centerx, self.rect.centery)

        yDistance = selfPos[1] - other[1]
        xDistance = selfPos[0] - other[0]
        scale = 1 / hypot(xDistance, yDistance)
        yDistance = yDistance * scale
        xDistance = xDistance * scale

        self.rect.move_ip(xDistance * self.move_distance* 1, yDistance * self.move_distance*1)
