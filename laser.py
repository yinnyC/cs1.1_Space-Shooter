import pygame


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self._mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        """ Move the laser torward the target"""
        self.y += vel

    def is_off_screen(self, height):
        """ check if the laser is off the screen """
        return not(self.y <= height and self.y >= 0)

    def check_collision(self, obj):
        """ Check if a laser hit the ship """
        offset_x = int(obj.x - self.x)
        offset_y = int(obj.y - self.y)
        return self._mask.overlap(obj._mask, (offset_x, offset_y)) != None
