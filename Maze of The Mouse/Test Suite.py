import unittest
import pygame
import Maze
import NPC as NPC
import player as player
import game
import Mouse_NPC


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def main(self):
        (game.run(Mouse_NPC) == False)

if __name__ == '__main__':
    unittest.main()
