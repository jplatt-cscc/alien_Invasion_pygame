import sys
import pygame
import random
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:

    def __init__(self):
        # Initializes the game
        pygame.init()
        # Creates game tick rate & settings vars
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        # Intializes display
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.game_active = True


    def run_game(self):
        # Starts the game loop
        while True:
            # Watches for inputs
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            # Sets game tick rate
            self.clock.tick(60)

    def _check_events(self):
        # Checks for inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # Key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # Key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _create_alien(self, x_position, y_position):
        # Creates aliens
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _create_fleet(self):
        # Creates fleets
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 6 * alien_height):
            while current_x < (self.settings.screen_width - 4 * alien_width):
                # Randomizes the fleet (1 in X spawn chance (currently 1 in 3)
                chance = random.randint(1,3)
                if chance == 1:
                    self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _update_aliens(self):
        # Moves the aliens
        self._check_fleet_edges()
        self.aliens.update()
        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            print("Ship hit!")
        # Check for aliens hitting the bottom
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        # Check if fleet hits edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # Changes fleet direction and lowers fleet
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        # Creates bullets
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        # Update bullet position
        self.bullets.update()
        # Get rid of bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet) 

        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        # Check for bullet hitting aliens
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        # Check if fleet is destroyed
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
    
    def _check_aliens_bottom(self):
        # Check if fleet hits the bottom
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
    
    def _ship_hit(self):
        # Lower ships lives
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Destroy existing bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Displays frames
        pygame.display.flip()


if __name__ == '__main__':
    # Run the game.
    ai = AlienInvasion()
    ai.run_game()
    pass
