import pygame
from main import play
from game.characters.player import Player
from game.characters.enemy import Enemy

# Initialize Pygame
pygame.init()

# Set up the window
size = (640, 480)
screen = pygame.display.set_mode(size)

# Set up the font
font = pygame.font.SysFont(None, 48)

def create_button(rect, color, text, text_color):
    # Create a new surface for the button
    button = pygame.Surface(rect.size)
    # Fill the button with the specified color
    button.fill(color)
    # Render the button text and center it on the button surface
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=button.get_rect().center)
    button.blit(text_surf, text_rect)
    # Return the button surface
    return button

# Set up the buttons
buttons = [
    {"id": 1, "rect": pygame.Rect(200, 100, 200, 100), "color": (255, 255, 255), "text": "start", "text_color": (0, 0, 0)},
    {"id": 2, "rect": pygame.Rect(200, 300, 200, 100), "color": (255, 0, 0), "text": "Exit", "text_color": (255, 255, 255)},
]
button_surfaces = []
for button in buttons:
    button_surface = create_button(button["rect"], button["color"], button["text"], button["text_color"])
    button_surfaces.append(button_surface)

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit Pygame and exit the program
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse button was pressed over any of the buttons
            for button in buttons:
                if button["rect"].collidepoint(event.pos) and button["id"] == 1:
                    print("run game!")
                    play(Player, Enemy)
                elif button["rect"].collidepoint(event.pos) and button["id"] == 2:
                    pygame.quit()
                    quit()

    # Fill the screen with black
    screen.fill((0, 0, 0))
    # Draw the buttons to the screen
    for i, button_surface in enumerate(button_surfaces):
        screen.blit(button_surface, buttons[i]["rect"])
    # Update the display
    pygame.display.update()