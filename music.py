import pygame

class Music:
    """ Controls for starting and stopping the music """

    def initialize_music(self):
        # Load & configure music
        """ Music created by me on 'BeepBox.co' """
        self.bg_music = pygame.mixer.music.load('alien_Invasion_pygame\Assets\sound\BeepBox-Song1.wav')
        self.bg_volume = pygame.mixer.music.set_volume(0.4)

    def start(self):        
        # Starts & stops the music
        pygame.mixer.music.play(loops = -1)

    def stop(self):
        pygame.mixer.music.stop()