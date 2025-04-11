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
        boundaries = []
        boundaries.append(Boundary.Boundary([200, 200], .01, .01))
        boundaries.append(Boundary.Boundary([100, 200], .01, .01))
        self.runTestGame(tGame, boundaries)



    def runTestGame(self, tGame, boundaries):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tGame.running = False
            for boundary in boundaries:
                tGame.screen.blit(boundary.surf, boundary.rect)
            pygame.display.update()
            tGame.clock.tick(24)

def main():
    GameTest.testBoundary()