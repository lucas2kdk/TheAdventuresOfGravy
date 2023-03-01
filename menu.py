import pygame
import os
from main import play
from game.characters.player import Player
from game.characters.enemy import Enemy

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

# Set background
background_image = pygame.image.load(os.path.join('game', 'baggrunde', 'Bo.png')).convert()
picture = pygame.transform.scale(background_image, (1280, 720))
screen.blit(picture, (0, 0))

# Set up the font
font = pygame.font.SysFont(None, 48)

def create_button(position, size, color, text, text_color):
    # Create a new surface for the button
    button = pygame.Surface(size)
    # Fill the button with the specified color
    button.fill(color)
    # Render the button text and center it on the button surface
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=button.get_rect().center)
    button.blit(text_surf, text_rect)
    # Position the button at the specified position
    button_rect = button.get_rect(center=position)
    # Return the button surface and rect
    return button, button_rect

# Set up the buttons
button_size = (200, 100)
button_y = screen.get_height() // 2 - button_size[1] // 2
button_positions = [
    (screen.get_width() // 4, button_y),
    (screen.get_width() * 3 // 4, button_y),
]
buttons = [
    {"id": 1, "color": (255, 255, 255), "text": "start", "text_color": (0, 0, 0)},
    {"id": 2, "color": (255, 0, 0), "text": "Exit", "text_color": (255, 255, 255)},
]
button_surfaces = []
for i, button in enumerate(buttons):
    button_surface, button_rect = create_button(button_positions[i], button_size, button["color"], button["text"], button["text_color"])
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

    # Fill the screen with black
    #screen.fill((0, 0, 0))
    # Draw the buttons to the screen
    for i, button_surface in enumerate(button_surfaces):
        screen.blit(button_surface, buttons[i]["rect"])
    # Update the display
    pygame.display.update()
