import pygame

class Boundary(pygame.sprite.Sprite):
    def __init__(self, position, height, width):
        super().__init__()
        self.surf = pygame.image.load('BoundaryImage.png').convert_alpha()
        self.rect = pygame.Rect(position, height, width, 1)