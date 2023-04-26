import pygame
import os
from game.characters import spritsheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()

        # Set enemy properties
        self.speed = 0.8
        self.position = pygame.math.Vector2(screen_size[0] / 2, screen_size[1] / 2)

        # Create image and scale enemy to 4% of screen size
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 0, 0))
        scale_factor = int(screen_size[0] * 0.05) / self.image.get_width()
        self.image = pygame.transform.rotozoom(self.image, 0, scale_factor)

        # Set rect
        self.rect = self.image.get_rect()

        # Load sprite sheet and create frame list
        sprite_sheet_image = pygame.image.load(os.path.join('game', 'sprites', 'ghost', 'ghost.png')).convert_alpha()
        sprite_sheet = spritsheet.spritSheet(sprite_sheet_image)

        black = (0, 0, 0)

        self.frame_list = []
        animation_steps = 11

        for x in range(animation_steps):
            self.frame_list.append(sprite_sheet.get_img(x, 60, 60, 1.4, black))

        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 500
        self.current_frame = 0

    def update(self, player_position):
        # Move the enemy towards the player
        direction = player_position - self.position
        if direction.length() > self.speed:
            direction.scale_to_length(self.speed)
        self.position += direction
        self.rect.center = self.position

        # Update the enemy's animation frame
        current_time = pygame.time.get_ticks()
        if current_time - self.update_time >= self.animation_cooldown:
            self.current_frame = (self.current_frame + 1) % len(self.frame_list)
            self.update_time = current_time
