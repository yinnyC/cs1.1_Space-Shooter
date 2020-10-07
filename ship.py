import settings
from laser import Laser


class Ship:
    """ A parent Class of Player/Enimes, define basic feature of a ship """

    def __init__(self, x, y, health=100):
        """ Initialize a ship object """
        self.x = x
        self.y = y
        self.health = health
        self._ship_img = None
        self._laser_img = None
        self._lasers = []

    def draw(self, window):
        """ Draw out the ship in the Game Window """
        window.blit(self._ship_img, (self.x, self.y))
        for laser in self._lasers:
            laser.draw(window)

    def shoot(self):
        """ create a laser object and append it into the list """
        laser = Laser(self.x, self.y, self._laser_img)
        self._lasers.append(laser)

    def move_lasers(self, vel, obj):
        """ handling _lasers in the list"""
        for laser in self._lasers:
            laser.move(vel)
            # remove the laser that is off the screen
            if laser.is_off_screen(settings.HEIGHT):
                self._lasers.remove(laser)
            elif laser.check_collision(obj):  # check if laser hit the target
                obj.health -= 10
                self._lasers.remove(laser)

    def get_width(self):
        """ Return the width of the ship img """
        return self._ship_img.get_width()

    def get_height(self):
        """ Return the height of the ship img """
        return self._ship_img.get_height()
