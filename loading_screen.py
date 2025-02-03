import pygame
import time
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background_path = os.path.join(os.path.dirname(__file__), "img", "1.png")  # Adjust the path as needed
background = pygame.image.load(background_path)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

logo_path = os.path.join(os.path.dirname(__file__), "img", "0.png")  # Adjust the path as needed
logo = pygame.image.load(logo_path)  # Load your logo image
logo = pygame.transform.scale(logo, (100, 100))  # Resize logo if necessary

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont('comicsansms',20,bold=True)

def draw_loading_bar(progress):
    """ Draws a simple loading bar on the screen with rounded corners. """
    bar_width = 400
    bar_height = 30
    bar_x = (WIDTH - bar_width) // 2
    bar_y = HEIGHT - 100
    border_radius = 10  # Set the border radius

    pygame.draw.rect(screen, BLACK, (bar_x, bar_y, bar_width, bar_height), border_radius=border_radius)  # Border
    pygame.draw.rect(screen, GREEN, (bar_x, bar_y, bar_width * progress, bar_height), border_radius=border_radius)  # Fill

def loading_screen():
    """ Displays a loading screen while simulating asset loading. """
    running = True
    progress = 0

    while running:
        screen.blit(background, (0, 0))  # Display background
        screen.blit(logo, (WIDTH - logo.get_width() - 10, 10))  # Display logo at top right

        draw_loading_bar(progress)  # Show loading progress

        # Display loading text with percentage near the loading bar
        loading_text = font.render(f"Loading {int(progress * 100)}%", True, WHITE)
        screen.blit(loading_text, (WIDTH // 2 - 50, HEIGHT - 130))

        pygame.display.flip()
        time.sleep(0.2)  # Simulate loading time
        progress += 0.2

        if progress >= 1:
            running = False  # Exit when loading completes

# Run loading screen
loading_screen()

def main_game():
    """ Main game loop. """
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)  # Clear screen with white color
        # Add your game logic and drawing code here

        pygame.display.flip()

# Run main game after loading screen
main_game()

# Quit Pygame
pygame.quit()
