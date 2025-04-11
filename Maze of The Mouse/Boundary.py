import pygame

class Boundary(pygame.sprite.Sprite):
    def __init__(self, position, height, width):
        super().__init__()
        self.position = position
        self.surf = pygame.image.load('images/BoundaryImage.png').convert_alpha()
        self.rect = pygame.Rect(0, height, width, 1)
        self.rect.move_ip(position[0], position[1])