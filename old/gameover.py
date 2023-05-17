import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load font
font = pygame.font.Font(None, 48)

def game_over_menu():
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Restart the game
                    return

        # Clear the screen
        screen.fill(BLACK)

        # Render text
        game_over_text = font.render("Game Over", True, WHITE)
        restart_text = font.render("Press Enter to Exit", True, WHITE)

        # Center the text on the screen
        game_over_rect = game_over_text.get_rect(center=(info.current_w // 2, info.current_h // 2 - 50))
        restart_rect = restart_text.get_rect(center=(info.current_w // 2, info.current_h // 2 + 50))

        # Draw text on the screen
        screen.blit(game_over_text, game_over_rect)
        screen.blit(restart_text, restart_rect)

        # Update the display
        pygame.display.flip()

        pygame.quit()
        quit()