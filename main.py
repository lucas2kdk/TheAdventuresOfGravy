import os
import sys
import pygame
from game.characters.player import Player
from game.characters.enemy import Enemy
from pygame.locals import *
from game.characters.enemy import *
import threading
from gameover import game_over_menu

# make a main function
def play(Player, Enemy):
    # Initialize Pygame
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("game/sounds/Menu theme but actually good.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(0,0)
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

    # Health lock
    health_lock = threading.Lock()

    # Exit function
    def exitfn(keys):
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

    # Main game loop
    clock = pygame.time.Clock()
    running = True

    def healthCheck():
        global running
        
        while player.currHealth > 0:    
            if player.rect.colliderect(enemy.rect):
                with health_lock:
                    player.currHealth -= 1
                print("PLAYER HEALTH:", player.currHealth)
            pygame.time.delay(100)  # Delay between health checks

        sound = pygame.mixer.Sound("game/sounds/death.wav")
        pygame.mixer.Sound.play(sound,1,2000,1500)
        running = False
        pygame.quit()
        quit()


    t1 = threading.Thread(target=healthCheck)
    t1.start()

    while running == True:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Update the player and enemy
        keys = pygame.key.get_pressed()
        player.update(keys)
        enemy.update(player.position)

        # Blit the background image onto the screen
        screen.blit(background_image, (0, 0))

        # Draw the sprites
        all_sprites.draw(screen)
        screen.blit(enemy.frame_list[enemy.current_frame], (0, 0))

        # Draw health
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Health: " + str(player.currHealth), 10, (255, 255, 255))
        screen.blit(label, (100, 20))

        # Run exitfn function
        exitfn(keys)

        # Update the screen
        pygame.display.flip()

        # Limit the frame rate to 60 fps
        clock.tick(60)

    # Quit Pygame
    pygame.quit()
    quit()
