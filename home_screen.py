import pygame
import time
import os

class HomeScreen:

    def __init__(self):
        
        # Screen dimensions
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
        self.button_font = pygame.font.SysFont('tahoma', 40, bold=True)

    def main_menu(self):
        """Main menu with quit button"""
        # Create button
        button_width, button_height = 110, 60
        button = pygame.Rect(
            (self.WIDTH - button_width) // 2,
            (self.HEIGHT - button_height) // 2,
            button_width,
            button_height
        )

        button_gameplay = pygame.Rect(
            300,
            360,
            220,
            60
        )

        button_surface = self.button_font.render('Quit', True, self.WHITE)

        button_surface_gameplay = self.button_font.render('Gameplay', True, self.WHITE)

        running = True
        while running:
            self.screen.fill(self.PINK)
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.collidepoint(event.pos):
                        pygame.quit()
                        quit()
                    if button_gameplay.collidepoint(event.pos):
                        running = False

            # Hover effect
            mouse_pos = pygame.mouse.get_pos()
            button_color = (180, 180, 180) if button.collidepoint(mouse_pos) else (110, 110, 110)
            button_color_gameplay = (180, 180, 180) if button_gameplay.collidepoint(mouse_pos) else (110, 110, 110)
            pygame.draw.rect(self.screen, button_color, button)
            pygame.draw.rect(self.screen,button_color_gameplay,button_gameplay)
            
            # Draw button text
            self.screen.blit(button_surface, (button.x + 5, button.y + 5))
            self.screen.blit(button_surface_gameplay, (button_gameplay.x + 5, button_gameplay.y + 5))
            
            pygame.display.flip()