import settings
import time
import random
from player import Player
from enemies import Enemy
import pygame

pygame.font.init()

# Create A Main Game


def main():
    # Initialize pygame setting
    run = True
    clock = pygame.time.Clock()
    FPS = 60  # 60 frames in one second
    # Initialize game info
    lost = False
    enemies = []
    level, lives, wave_length = (0, 3, 10)
    player_vel, enemy_vel, laser_vel = (10, 3, 8)

    player = Player(int(settings.WIDTH/2-50), 600)
    # Set up Display text
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 40)
    restart_font = pygame.font.SysFont("comicsans", 40)

    def redraw_window():
        settings.WIN.blit(settings.BG, (0, 0))
        # Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        settings.WIN.blit(lives_label, (10, 10))
        settings.WIN.blit(level_label, (settings.WIDTH -
                                        level_label.get_width()-10, 10))
        for enemy in enemies:
            enemy.draw(settings.WIN)

        player.draw(settings.WIN)

        if lost:
            lost_label = lost_font.render("GAME OVER", 1, (255, 255, 255))
            settings.WIN.blit(
                lost_label, (int(settings.WIDTH/2 - lost_label.get_width()/2), 350))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        # check player status
        if player.health <= 0 & lives >= 0:
            player.health = player._max_health
            lives -= 1
        elif lives <= 0:
            lost = True

        redraw_window()
        if not lost:
            # Each level Generate a bunch of enemies
            if len(enemies) == 0:
                level += 1
                wave_length += 5
                for _ in range(wave_length):
                    enemy = Enemy(random.randrange(50, settings.WIDTH-100),
                                  random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                    enemies.append(enemy)
            # Iterate through enemies[]
            for enemy in enemies:
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)       # 1. move enemy

                if random.randrange(0, 3*60) == 1:         # 2. shoot laser
                    enemy.shoot()

                if player.check_collision(enemy):          # 3. Check collision
                    player.health -= 20
                    enemies.remove(enemy)

                elif enemy.is_off_screen(settings.HEIGHT):  # 4. remove enemy
                    lives -= 1
                    enemies.remove(enemy)

            player.move_lasers(-laser_vel, enemies)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:  # Left
            player.x -= player_vel
        elif keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < settings.WIDTH:  # Right
            player.x += player_vel
        elif keys[pygame.K_UP] and player.y - player_vel > 0:  # Up
            player.y -= player_vel
        elif keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < settings.HEIGHT:  # Down
            player.y += player_vel
        elif keys[pygame.K_SPACE]:
            player.shoot()


main()
