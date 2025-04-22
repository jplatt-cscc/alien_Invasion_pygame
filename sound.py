import pygame

class Sound:
    """ Controls for sound effects """

    def initialize_sound(self):
        # Loads sound effects
        pygame.mixer.init()
        """ Sound effects created by 'bfxr' program """
        self.sound_bullet = pygame.mixer.Sound('alien_Invasion_pygame\Assets\sound\Laser_Shoot1.wav')
        self.sound_explosion = pygame.mixer.Sound('alien_Invasion_pygame\Assets\sound\Explosion1.wav')

    def _play_sound(self, effect):
        # Plays given sound effect
        pygame.mixer.Sound.set_volume(effect, 0.2)
        pygame.mixer.Sound.play(effect)

        