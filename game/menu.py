import pygame

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
button_rects = [
    pygame.Rect(200, 100, 200, 100),
    pygame.Rect(200, 300, 200, 100),
]
button_colors = [
    (255, 255, 255),
    (255, 0, 0),
]
button_texts = [
    "start",
    "exit",
]
button_text_colors = [
    (0, 0, 0),
    (255, 255, 255),
]
buttons = []
for i in range(len(button_rects)):
    button = create_button(button_rects[i], button_colors[i], button_texts[i], button_text_colors[i])
    buttons.append(button)

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit Pygame and exit the program
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse button was pressed over any of the buttons
            for i in range(len(buttons)):
                if button_rects[i].collidepoint(event.pos):
                    print("Button", i+1, "clicked!")
                
    # Fill the screen with black
    screen.fill((0, 0, 0))
    # Draw the buttons to the screen
    for i in range(len(buttons)):
        screen.blit(buttons[i], button_rects[i])
    # Update the display
    pygame.display.update()
