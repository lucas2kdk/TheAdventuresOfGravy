import os
import pygame
from game.characters.player import Player
from game.characters.enemy import Enemy
from pygame.locals import *
from game.characters.enemy import *
from time import sleep
import threading
#from sys import exit

# make a main function
def play(Player, Enemy):

    # Initialize Pygame
    pygame.init()

    # Set up the window
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)

    # Set the window title
    pygame.display.set_caption("The Adventures of Young Gravy")

    # Load the background image
    background_image = pygame.image.load(os.path.join('game', 'baggrunde', 'Kirkegaard.png')).convert()
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    # Create the player and enemy objects and the sprite group
    player = Player((screen.get_width(), screen.get_height()))
    enemy = Enemy((screen.get_width()/2, screen.get_height()/2))
    all_sprites = pygame.sprite.Group(player, enemy)
    health = 5


    # Exit function
    def exitfn(keys):
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

    # Main game loop
    clock = pygame.time.Clock()
    running = True
    
    def healthCheck(playerHealth):
        print("HEALTH",playerHealth)
        while playerHealth > 0:
            if player.rect.colliderect(enemy.rect):
                playerHealth -= 1
                print("PLAYERHEALTH:",playerHealth)
                sleep(1)
            # else:
            #     pygame.quit()
            #     quit()
        pygame.quit()
        quit()
        
    t1 = threading.Thread(target=healthCheck, args=(health,))
    t1.start()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Update the player and enemy
        keys = pygame.key.get_pressed()
        player.update(keys)
        enemy.update(player.position)
        # print(player.bottomRight)

        # Blit the background image onto the screen
        screen.blit(background_image, (0, 0))

        # Draw the sprites
        all_sprites.draw(screen)
        screen.blit(enemy.frame_list[enemy.current_frame], (0, 0))

        # Draw helth
        

        # Run exitfn function
        exitfn(keys)


        # Update the screen
        pygame.display.flip()

        # Limit the frame rate to 60 fps
        clock.tick(60)
        
    # Quit Pygame
    pygame.quit()
    quit()
