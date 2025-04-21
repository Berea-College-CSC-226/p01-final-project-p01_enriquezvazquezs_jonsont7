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
        boundaries.append(Boundary.Boundary([200, 200]))
        boundaries.append(Boundary.Boundary([125, 200]))
        self.runTestGameBoundary(tGame, boundaries)

    def runTestGameBoundary(self, tGame, boundaries):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tGame.running = False
            for boundary in boundaries:
                tGame.screen.blit(boundary.surf, boundary.rect)
            pygame.display.update()
            tGame.clock.tick(24)

    def testMaze(self):
        tGame = game.Game()
        matrix = [[False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False],
                  [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False],
                  [False, False, True, False, False, True, True, True, True, True, True, False, False, True, False, False],
                  [False, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False],
                  [False, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False],
                  [False, False, True, False, False, False, False, False, True, True, True, False, False, True, False, False],
                  [False, False, True, False, False, False, False, False, True, True, True, False, False, True, False, False],
                  [True, True, True, False, False, True, False, False, False, False, False, False, False, True, True, True],
                  [False, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False],
                  [False, False, True, False, False, True, True, True, True, True, True, False, False, True, False, False],
                  [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False],
                  [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False]]
        maze = Maze.Maze(matrix, [400, 300])
        print(maze.matrix)
        maze.makeBoundaries()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tGame.running = False
            maze.drawMaze(tGame.screen)
            pygame.display.update()
            tGame.clock.tick(24)


def main():
    tester = GameTest()
    tester.testMaze()
    #tester.testBoundary()

main()