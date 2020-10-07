import settings
from ship import Ship
from laser import Laser
import pygame


class Enemy(Ship):
    COLOR_MAP = {  # Create a dictionary so that we can randomly select tuples from it
        "red": (settings.RED_SPACE_SHIP, settings.RED_LASER),
        "green": (settings.GREEN_SPACE_SHIP, settings.GREEN_LASER),
        "blue": (settings.BLUE_SPACE_SHIP, settings.BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        """ Initialize the enemy object """
        super().__init__(x, y, health)
        self._ship_img, self._laser_img = self.COLOR_MAP[color]
        self._mask = pygame.mask.from_surface(self._ship_img)

    def move(self, vel):
        """ Move the enemy object down in the window """
        self.y += vel

    def shoot(self):
        laser = Laser(self.x-20, self.y, self._laser_img)
        self._lasers.append(laser)

    def is_off_screen(self, height):
        """ check if the enemy is off the screen """
        return not(self.y <= height)
