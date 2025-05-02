import pygame

class Boundary(pygame.sprite.Sprite):
    def __init__(self, position):
        """
        Represents a single cell in the maze wall
        :param position: Pixel position of where the sprite is at
        """
        super().__init__()
        self.position = position
        self.surf = pygame.image.load('images/BoundaryImage.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.move_ip(position[0], position[1])
