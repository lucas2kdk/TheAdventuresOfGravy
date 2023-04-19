import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()

        # Set player properties
        self.health = 100
        self.speed = 0.02 * screen_size[0]

        # Load and scale player image
        self.image = pygame.image.load(os.path.join('game', 'sprites', 'player.png')).convert_alpha()
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(screen_size[0] // 2, screen_size[1] // 2)
        self.screen_size = screen_size
        self.scale_factor = int(self.screen_size[0] * 0.1) / self.original_image.get_width()
        self.image = pygame.transform.rotozoom(self.original_image, 0, self.scale_factor)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, keys):
        # Handle player movement
        Kx = keys[pygame.K_d] - keys[pygame.K_a]
        Ky = keys[pygame.K_s] - keys[pygame.K_w]
        movement_vector = pygame.math.Vector2(Kx, Ky)
        if movement_vector.length() > 0:
            movement_vector.normalize()
            movement_vector *= self.speed
        self.position += movement_vector
        self.rect.center = self.position
