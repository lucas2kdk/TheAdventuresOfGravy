import os
import pygame
from game.characters.player import Player
from game.characters.enemy import Enemy
#from pygame.locals import *

# make a main function
def play(Player, Enemy):

    # Initialize Pygame
    pygame.init()

    # Set the window size
    WINDOW_SIZE = (1280, 720)

    # Set up the window
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)

    # Set the window title
    pygame.display.set_caption("The Adventures of Young Gravy")

    # Set the background color to white
    background_color = (255, 255, 255)

    # Create the player and enemy objects and the sprite group
    player = Player(WINDOW_SIZE)
    enemy = Enemy(WINDOW_SIZE)
    all_sprites = pygame.sprite.Group(player, enemy)

    # Exit function
    def exitfn(keys):
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

    # Main game loop
    running = True
    while running:
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

        # Update the screen
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()