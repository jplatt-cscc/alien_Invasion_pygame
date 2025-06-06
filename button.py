import pygame.font

class Button:
    """ A class to build buttons for the game """

    def __init__(self, ai_game, msg):
        # Initialize button
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        """ Font from Google Fonts: https://fonts.google.com/specimen/Rubik+Moonrocks """
        self.font = pygame.font.Font('alien_Invasion_pygame\Assets\Fonts\Rubik_Moonrocks\RubikMoonrocks-Regular.ttf', 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # Turn text into an image & center on button
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw button and text
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)