from os import path
import pygame
from core.enemy import Enemy
from core.player import Player
from core.const import *

img_dir = path.join(path.dirname(__file__), '../img')

class App:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    def __init__(self):
        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("UAS Bahasa Pemrograman 1")

        # Load all game graphics
        self.background = pygame.image.load(path.join(img_dir, "bg.png")).convert()
        self.background_rect = self.background.get_rect()
        player_img = pygame.image.load(path.join(img_dir, "player.png")).convert()
        meteor_img = pygame.image.load(path.join(img_dir, "meteor.png")).convert()

        App.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = Player(player_img)
        App.all_sprites.add(self.player)
        for i in range(8):
            enemy = Enemy(meteor_img)
            App.all_sprites.add(enemy)
            self.enemies.add(enemy)

        self.running = False

    def on_playing(self):
        self.check_collision(self.player, self.enemies)


    def stop(self):
        self.running = False

    def check_collision(self, sprite, group, dokill=True):
        return pygame.sprite.spritecollide(sprite, group, dokill)

    def run(self):
        # Game loop
        self.running = True
        while self.running:
            # keep loop running at the right speed
            App.clock.tick(FPS)
            # Process input (events)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    self.running = False

            self.on_playing()

            # Update
            App.all_sprites.update()

            # Draw / render
            App.screen.fill(BLACK)
            App.screen.blit(self.background, self.background_rect)
            App.all_sprites.draw(BaseApp.screen)
            # *after* drawing everything, flip the display
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
         theApp = App()
         theApp.run()