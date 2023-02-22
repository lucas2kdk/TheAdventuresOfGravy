import pygame
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()

        # Load ghost spritesheet
        spritesheet = pygame.image.load(os.path.join('game', 'sprites', 'ghost', 'ghost.png')).convert_alpha()

        # Set ghost properties
        self.speed = 5
        self.position = pygame.math.Vector2(screen_size[0] / 2, screen_size[1] / 2)

        # Define the sprite dimensions and animation frames
        frame_width = 60
        frame_height = 60
        num_frames = 11
        self.frames = [spritesheet.subsurface(pygame.Rect((i * frame_width, 0), (frame_width, frame_height)))
                       for i in range(num_frames)]
        self.current_frame = 0
        self.frame_delay = 6
        self.frame_count = 0

        # Scale ghost to 4% of screen size
        scale_factor = int(screen_size[0] * 0.08) / frame_width
        self.frames = [pygame.transform.rotozoom(frame, 0, scale_factor) for frame in self.frames]
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()

    def update(self, player_position):
        # Move the ghost towards the player
        direction = player_position - self.position
        if direction.length() > self.speed:
            direction.scale_to_length(self.speed)
        self.position += direction
        self.rect.center = self.position

        # Update the ghost sprite animation
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.frame_count = 0
