import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Create an empty pygame window"""
    #Initialize game, settings, and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the first fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Set the background color.
    bg_color = (230, 230, 230)

    #Start the main loop of the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        # Update ship movement
        ship.update()

        #Update bullets
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

        # Update aliens
        gf.update_aliens(ai_settings, aliens)

        # Update screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()