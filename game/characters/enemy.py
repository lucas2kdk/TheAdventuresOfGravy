import pygame
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()

        # Load and scale enemy image
        self.image = pygame.image.load(os.path.join('game', 'sprites', 'enemy.jpg')).convert_alpha()
        self.rect = self.image.get_rect()

        # Set enemy properties
        self.speed = 0.8
        self.position = pygame.math.Vector2(screen_size[0] / 2, screen_size[1] / 2)

        # Scale enemy to 4% of screen size
        scale_factor = int(screen_size[0] * 0.04) / self.rect.width
        self.image = pygame.transform.rotozoom(self.image, 0, scale_factor)
        self.rect = self.image.get_rect()

    def update(self, player_position):
        # Move the enemy towards the player
        direction = player_position - self.position
        if direction.length() > self.speed:
            direction.scale_to_length(self.speed)
        self.position += direction
        self.rect.center = self.position
