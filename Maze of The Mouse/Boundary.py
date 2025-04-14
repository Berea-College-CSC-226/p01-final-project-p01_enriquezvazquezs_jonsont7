import pygame

class Boundary(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.surf = pygame.image.load('images/BoundaryImage.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.move_ip(position[0], position[1])
