import settings
from ship import Ship
from laser import Laser
import pygame


class Player(Ship):
    """ A idle that represents player, can shoot lasers and display healthbar """

    def __init__(self, x, y, health=100):
        """ Initialize player class """
        super().__init__(x, y, health)
        self._ship_img = settings.YELLOW_SPACE_SHIP
        self._laser_img = settings.YELLOW_LASER
        self._mask = pygame.mask.from_surface(self._ship_img)
        self._max_health = health

    def draw(self, window):
        """ Draw out the ship in the Game Window """
        super().draw(window)
        self.healthbar(window)

    def move_lasers(self, vel, objs):
        """ handling player's lasers in the list"""
        for laser in self._lasers:
            laser.move(vel)
            if laser.is_off_screen(settings.HEIGHT):
                self._lasers.remove(laser)
            else:
                for obj in objs:  # Check if laser hit any enemy
                    if laser.check_collision(obj):
                        objs.remove(obj)  # Remove the enemy from enemies list
                        self._lasers.remove(laser)

    def check_collision(self, obj):
        """ Check if a player hit the enemy """
        offset_x = int(obj.x - self.x)
        offset_y = int(obj.y - self.y)
        return self._mask.overlap(obj._mask, (offset_x, offset_y)) != None

    def healthbar(self, window):
        """ Set up 2 rectangles that display player's health """
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y +
                                               self._ship_img.get_height() + 10, self._ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self._ship_img.get_height() +
                                               10, self._ship_img.get_width() * (self.health/self._max_health), 10))
