import pygame

class Settings:

    def __init__(self):
        # Initialize settings

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (150, 150, 150)
        """ Background image "Space Backdrop" by: beren77, from OpenGameArt.Org """
        self.bg_image = pygame.image.load('alien_Invasion_pygame\Assets\images\spacefield_a-000.png')

        # Ship Settings
        self.ship_speed = 2
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # 1 = right, -1 = left
        self.fleet_direction = 1

        # Difficulty settings
        self.speedup_scale = 1.5

        # Scoring settings
        self.score_scale = 1.5        

        # Dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initial dynamic settings values
        self.ship_speed = 2
        self.bullet_speed = 5
        self.alien_speed = 0.5
        # 1 = right, -1 = left
        self.fleet_direction = 1
        # Scoring settings
        self.alien_points = 25

    def increase_speed(self):
        # Increases speed
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # Increases score per hit
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

    

