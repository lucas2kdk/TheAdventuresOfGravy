import pygame
from game.characters.player import Player
from game.characters.enemy import Enemy
from main import play

class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)

# Initialize Pygame
pygame.init()

# Background audio
pygame.mixer.init()
pygame.mixer.music.load("game/sounds/Main_theme.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(0,0)

# Set up the window
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)

# Set background
background_image = pygame.image.load("game/baggrunde/Bo.png").convert()
picture = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
screen.blit(picture, (0, 0))

# Set up the font
font = pygame.font.Font('game/fonts/treasure.ttf', int(screen.get_height() * 0.045))

# Set up the title
title = "The Adventures of Gravy"
title_surface = font.render(title, True, (255,255,255))
title_rect = title_surface.get_rect(center=(info.current_w/2, info.current_h/4)) 
screen.blit(title_surface, title_rect)

# Set up the buttons
button_size = (200, 100)  # Adjust button size as needed
start_image = pygame.transform.scale(pygame.image.load("game/graphics/start.png"), button_size)  
quit_image = pygame.transform.scale(pygame.image.load("game/graphics/stop.png"), button_size)  
start_button = Button(start_image, info.current_w/2, info.current_h/2)
quit_button = Button(quit_image, info.current_w/2, info.current_h/2 + button_size[1] + 20)  # The "+ 20" gives some vertical space between the buttons

while True:
    # Handle events
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            # Quit Pygame and exit the program
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_over(pos):
                play(Player, Enemy)  # Assuming 'play' starts the game
            if quit_button.is_over(pos):
                pygame.quit()
                quit()

    # Redraw the screen and buttons
    screen.blit(picture, (0, 0))
    screen.blit(title_surface, title_rect)
    start_button.draw(screen)
    quit_button.draw(screen)

    clock.tick(60)

    # Update the display
    pygame.display.update()
