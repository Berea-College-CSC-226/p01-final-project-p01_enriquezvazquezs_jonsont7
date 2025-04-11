import unittest
import pygame
import Maze
import NPC
import player
import Boundary
import game

class GameTest(unittest.TestCase):
    def testBoundary(self):
        tGame = game.Game()
        boundary = Boundary.Boundary(30, 5, 5)
        self.runTestGame(tGame, boundary)



    def runTestGame(self, tGame, boundary):
        tGame.screen.blit()

def main():
    GameTest.testBoundary()