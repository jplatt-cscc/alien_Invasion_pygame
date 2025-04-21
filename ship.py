import pygame

class Ship:

    def __init__(self, ai_game):
        # Initialize the ship
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load('alien_Invasion_pygame\Assets\images\ship1.png')
        self.rect = self.image.get_rect()

        # Start new ships at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Stores ship position
        self.x = float(self.rect.x)
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update ship movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    
    def center_ship(self):
        # Center the ship
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        # Draw the ship
        self.screen.blit(self.image, self.rect)