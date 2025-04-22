import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class to create and move the bullets """

    def __init__(self, ai_game):
        # Creates bullet
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        """ Laser asset made by me in the program 'Pixelorama' """
        self.image = pygame.image.load('alien_Invasion_pygame\Assets\images\laser1.png')
        self.rect = self.image.get_rect()

        self.rect.midtop = ai_game.ship.rect.midtop

        # Stores bullet position
        self.y = float(self.rect.y)

    def update(self):
        # Moves bullet
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # Draws bullet
        self.screen.blit(self.image, self.rect)
