import os
import pygame

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images asset
filepath = os.path.dirname(__file__)
RED_SPACE_SHIP = pygame.image.load(os.path.join(
    filepath, "assets/pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join(
    filepath, "assets/pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join(
    filepath, "assets/pixel_ship_blue_small.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(
    os.path.join(filepath, "assets/pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join(
    filepath, "assets/pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join(
    filepath, "assets/pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join(
    filepath, "assets/pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join(
    filepath, "assets/pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join(
    filepath, "assets/background-black.png")), (WIDTH, HEIGHT))
