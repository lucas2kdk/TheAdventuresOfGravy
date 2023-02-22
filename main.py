import os
import pygame
from game.characters.player import Player

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (1280, 720)

# Set up the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the window title
pygame.display.set_caption("The Adventures of Young Gravy")

# Set the background color to white
background_color = (255, 255, 255)

# Set the path for the sprites folder
SPRITES_PATH = os.path.join('game', 'sprites')

# Load the player image
player_image = pygame.image.load(os.path.join(SPRITES_PATH, 'player.png')).convert_alpha()

# Create the player object and the sprite group
player = Player(WINDOW_SIZE)
all_sprites = pygame.sprite.Group(player)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the player
    keys = pygame.key.get_pressed()
    player.update(keys)
    
    # Fill the screen with the background color
    screen.fill(background_color)
    
    # Draw the sprites
    all_sprites.draw(screen)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
