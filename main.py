import os
import pygame
from game.characters.player import Player
from game.characters.enemy import Enemy
#from pygame.locals import *

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

# Create the player and enemy objects and the sprite group
player = Player(WINDOW_SIZE)
enemy = Enemy(WINDOW_SIZE)
all_sprites = pygame.sprite.Group(player, enemy)

# Set up the clock to limit the game to 60 fps
clock = pygame.time.Clock()

# Set up the font to display the FPS counter
font = pygame.font.Font(None, 36)

# Exit function
def exitfn(keys):
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

# Main game loop
running = True
while running:
    # Limit the game to 60 fps
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the sprites
    all_sprites.draw(screen)

    # Update the player and enemy
    keys = pygame.key.get_pressed()
    player.update(keys)
    enemy.update(player.position)

    # Run exitfn function
    exitfn(keys)

    # Draw the FPS counter in the top left corner of the screen
    fps_text = font.render("FPS: {:.2f}".format(clock.get_fps()), True, (0, 0, 0))
    screen.blit(fps_text, (10, 10))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
