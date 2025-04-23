
import pygame, random, NPC, math

class Enemy_NPC(NPC):
    def __init__(self, screen_size, path_points, detection_radius=100):
        super().__init__(screen_size)
        self.path_points = path_points  # II.A.1: list of (x, y) points
        self.path_index = 0  # current target index in the path
        self.detection_radius = detection_radius
        self.following_mouse = False
        self.mouse_target = None

    def update(self, mouse_pos):
        """
        Updates enemy behavior each frame.
        :param mouse_pos: (x, y) tuple of current mouse position
        """
        if self.is_mouse_close(mouse_pos):  # II.B.1
            self.mouse_target = mouse_pos  # II.B.2
            self.following_mouse = True
        else:
            self.following_mouse = False
            self.mouse_target = None

        if self.following_mouse and self.mouse_target:
            self.move_towards(self.mouse_target)  # II.B.3
        else:
            self.follow_path()  # II.A.2

    def is_mouse_close(self, mouse_pos):
        """ Check if mouse is within detection radius. """
        dx = self.rect.centerx - mouse_pos[0]
        dy = self.rect.centery - mouse_pos[1]
        distance = math.hypot(dx, dy)
        return distance < self.detection_radius

    def follow_path(self):
        """ Move toward the next point in the predefined path. """
        if not self.path_points:
            return

        target = self.path_points[self.path_index]
        self.move_towards(target)

        if self.reached_point(target):
            self.path_index = (self.path_index + 1) % len(self.path_points)  # loop

    def move_towards(self, target):
        """ Move the NPC toward a given (x, y) point. """
        dx = target[0] - self.rect.centerx
        dy = target[1] - self.rect.centery
        distance = math.hypot(dx, dy)
        if distance == 0:
            return

        dx, dy = dx / distance, dy / distance  # normalize
        self.rect.move_ip(dx * self.move_distance, dy * self.move_distance)

    def reached_point(self, point):
        """ Check if current position is close enough to a target point. """
        px, py = point
        return math.hypot(self.rect.centerx - px, self.rect.centery - py) < self.move_distance