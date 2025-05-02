from math import hypot

import pygame
import random
from NPC import NPC
import math


class Mouse(NPC):
    move_distance = 50
    directions = ["north", "east", "south", "west"]

    def __init__(self, screen_size, imgName, position = [0, 0]):
        """
        Represents the Mouse NPC in the game.

        :param screen_size: Screen size, for keeping character on the screen
        :param imgName: Selects the image file
        :param position: NPC sprite starting point
        """
        super().__init__(screen_size, imgName)
        self.move_distance = 4
        self.rect.move_ip(position[0], position[1])

    def movement(self, others):
        """
        Moves the Mouse away from the closest cat

        :param others: The other cat NPC's
        :return: None
        """

        self.moveAwayFromOther(self.get_closest_cat_position(others))

    def get_closest_cat_position(self, others):
        """
        Finds the closest cat from a list of other sprites

        :param others: The other cat NPC's
        :return: Closest cats position
        """
        cat_positions = [(cat.rect.centerx, cat.rect.centery) for cat in others]
        min_distance = float('inf')
        closest_cat = None

        for cat_pos in cat_positions:
            distance = self.calculation_cat(self.rect.center, cat_pos)
            if distance < min_distance:
                min_distance = distance
                closest_cat = cat_pos

        return closest_cat

    def calculation_cat(self, pos1, pos2):
        """
        Calculates the Euclidean distance between two points

        :param pos1: First position
        :param pos2: Second position
        :return: Represents the distance between pos1 and pos2
        """
        a = pos1[0] - pos2[0]
        b = pos1[1] - pos2[1]
        return math.sqrt(a ** 2 + b ** 2)



    def moveAwayFromOther(self, other):
        """
        Moves the Mouse the opposite way of the cat

        :param other: The other cat NPC's
        :return: None
        """
        selfPos = (self.rect.centerx, self.rect.centery)

        yDistance = selfPos[1] - other[1]
        xDistance = selfPos[0] - other[0]
        scale = 1/hypot(xDistance, yDistance)
        yDistance = yDistance * scale
        xDistance = xDistance * scale

        self.rect.move_ip(xDistance*self.move_distance, yDistance*self.move_distance)