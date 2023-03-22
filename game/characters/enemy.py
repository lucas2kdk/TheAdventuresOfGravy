import pygame
import os
from game.characters import spritsheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()

        # Set enemy properties
        self.speed = 0.8
        self.position = pygame.math.Vector2(screen_size[0] / 2, screen_size[1] / 2)

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
        self.frame = 0


    def update(self, player_position, frame_list):
        # Move the enemy towards the player
        direction = player_position - self.position
        if direction.length() > self.speed:
            direction.scale_to_length(self.speed)
        self.position += direction
        self.rect.center = self.position

        update = pygame.time.get_ticks()
        animation_cooldown = 500 
        frame = 0

        current_time = pygame.time.get_ticks()
        if current_time - update >= animation_cooldown:
            frame += 1
            if frame >= len(frame_list):
                frame = 0