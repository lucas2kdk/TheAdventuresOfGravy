import pygame
import os
from main import play
from game.characters.player import Player
from game.characters.enemy import Enemy
from threading import Thread
import playsound

# Initialize Pygame
pygame.init()

t = Thread(target=playsound.playsound, args=["main theme.mp3"])

t.start()

# Set up the window
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)

# Set background
background_image = pygame.image.load(os.path.join('game', 'baggrunde', 'Bo.png')).convert()
picture = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
screen.blit(picture, (0, 0))

# Set up the font
font = pygame.font.SysFont(None, int(screen.get_height() * 0.045))

def create_button(position, size, color, text, text_color,type):
    # Create a new surface for the button
    button = pygame.Surface(size)
    # Fill the button with the specified color
    button.fill(color)
    # Render the button text and center it on the button surface
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=button.get_rect().center)
    textsurf = str(text_surf)

    if type == "PLAY":
        charImage = pygame.image.load(os.path.join('game', 'sprites', 'knap.png'))
        charImage = pygame.transform.scale(charImage, (160, 80))
        charImage = charImage.convert()
        button.blit(charImage, button.get_rect())

    elif type == "EXIT":
        charImage = pygame.image.load(os.path.join('game', 'sprites', 'Exit Knap.png'))
        #charImage = pygame.transform.scale(charImage, (57, 26))
        charImage = pygame.transform.scale(charImage, (160, 80))
        charImage = charImage.convert()
        button.blit(charImage, button.get_rect())

    button.blit(text_surf, text_rect)
    button_rect = button.get_rect(center=position)
    return button, button_rect

# Set up the buttons
button_size = (int(screen.get_width() * 0.104), int(screen.get_height() * 0.093))
button_y = screen.get_height() // 2 - button_size[1] // 2
button_positions = [
    (int(screen.get_width() * 0.26), button_y),
    (int(screen.get_width() * 0.74), button_y),
]
buttons = [
    {"id": 1, "color": (255, 255, 255), "text": "star0t", "text_color": (0, 0, 0),"type":"PLAY"},
    {"id": 2, "color": (255, 0, 0), "text": "Exit", "text_color": (255, 255, 255),"type":"EXIT"},
]
button_surfaces = []
for i, button in enumerate(buttons):
    button_surface, button_rect = create_button(button_positions[i], button_size, button["color"], "", button["text_color"],button["type"]) #button["text"]
    button["rect"] = button_rect
    button_surfaces.append(button_surface)

while True:
    # Handle events
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit Pygame and exit the program
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse button was pressed over any of the buttons
            for button in buttons:
                if button["rect"].collidepoint(event.pos) and button["id"] == 1:
                    play(Player, Enemy)
                elif button["rect"].collidepoint(event.pos) and button["id"] == 2:
                    pygame.quit()
                    quit()

    clock.tick(5)

    # Draw the buttons to the screen
    for i, button_surface in enumerate(button_surfaces):
        screen.blit(button_surface, buttons[i]["rect"])
    # Update the display
    pygame.display.update()
