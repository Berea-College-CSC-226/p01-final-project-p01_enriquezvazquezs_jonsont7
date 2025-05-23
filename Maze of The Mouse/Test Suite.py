import unittest
import pygame
import Maze
import NPC
import player
import Boundary
import game
class GameTest(unittest.TestCase):
    def testBoundary(self):
        """
        Tests if the boundaries appear on the screen

        :return: None
        """
        tGame = game.Game()
        boundaries = []
        boundaries.append(Boundary.Boundary([200, 200]))
        boundaries.append(Boundary.Boundary([125, 200]))
        self.runTestGameBoundary(tGame, boundaries)

    def runTestGameBoundary(self, tGame, boundaries):
        """
        Draws the boundary on the screen

        :param tGame:
        :param boundaries: list of boundaries to draw
        :return:None
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tGame.running = False
            for boundary in boundaries:
                tGame.screen.blit(boundary.surf, boundary.rect)
            pygame.display.update()
            tGame.clock.tick(24)

    def testMaze(self):
        """
        Tests maze drawn on the matrix

        :return: None
        """
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
        maze = Maze.Maze(matrix)
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
    """
    Running the tests

    :return:None
    """
    tester = GameTest()
    tester.testMaze()
    #tester.testBoundary()

main()