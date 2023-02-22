import pygame

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (1280, 720)

# Set up the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the window title
pygame.display.set_caption("Blank White Canvas")

# Set the background color to white
background_color = (255, 255, 255)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with the background color
    screen.fill(background_color)
    
    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
