import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """" Class to handle creating & moving the aliens """

    def __init__(self, ai_game):
        # Initialized aliens
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image
        """ Alien asset made by me in the program 'Pixelorama' """
        self.image = pygame.image.load('alien_Invasion_pygame\Assets\images\enemy1.png')
        self.rect = self.image.get_rect()

        # Start each new alien nat the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stores alien position
        self.x = float(self.rect.x)

    def update(self):
        # Move the aliens
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        # Checks if aliens hit the edges
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)



