import pygame
import time
import os

class LoadingScreen:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Load and scale assets
        self.background = pygame.image.load(os.path.join(os.path.dirname(__file__), "img", "1.png"))
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))

        self.logo = pygame.image.load(os.path.join(os.path.dirname(__file__), "img", "0.png"))
        self.logo = pygame.transform.scale(self.logo, (100, 100))

        # Colors
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 200, 0)
        self.BLACK = (0, 0, 0)
        self.PINK = (255, 192, 203)  # RGB for pink

    # Fonts
        self.loading_font = pygame.font.SysFont('comicsansms', 20, bold=True)
        self.button_font = pygame.font.SysFont('tahoma', 40, bold=True)

    def draw_loading_bar(self,progress):
        """Draw a loading bar with rounded corners"""
        bar_width = 400
        bar_height = 30
        bar_x = (self.WIDTH - bar_width) // 2
        bar_y = self.HEIGHT - 100
        border_radius = 10

        # Draw background
        pygame.draw.rect(self.screen, self.BLACK, (bar_x, bar_y, bar_width, bar_height), border_radius=border_radius)
        # Draw progress
        pygame.draw.rect(self.screen, self.GREEN, (bar_x, bar_y, bar_width * progress, bar_height), border_radius=border_radius)

    def loading_screen(self):
        """Show loading screen with progress bar"""
        progress = 0
        running = True

        while running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.logo, (self.WIDTH - self.logo.get_width() - 10, 10))

            # Draw loading bar
            self.draw_loading_bar(progress)
            
            # Loading text
            loading_text = self.loading_font.render(f"Loading {int(progress * 100)}%", True, self.WHITE)
            self.screen.blit(loading_text, (self.WIDTH//2 - 50, self.HEIGHT - 130))

            pygame.display.flip()
            time.sleep(0.2)
            progress += 0.2

            if progress >= 1:
                running = False
