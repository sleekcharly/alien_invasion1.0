import pygame

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

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Set the background color.
    bg_color = (230, 230, 230)

    #Start the main loop of the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ship)

        # Update ship movement
        ship.update()

        # Update screen
        gf.update_screen(ai_settings, screen, ship)

run_game()