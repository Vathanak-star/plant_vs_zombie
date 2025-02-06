import os
import pygame

class HomeScreen:
    def __init__(self):

        # Screen Dimensions
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Plants vs Zombies")

        #Define Paths to the image
        self.base_dir = os.path.dirname(__file__)
        self.assets_dir = os.path.join(self.base_dir, 'assets')
        self.images_dir = os.path.join(self.assets_dir, 'images')

        # Load Background Image
        self.background_image = pygame.image.load(os.path.join(self.images_dir, 'bg2.png')).convert()
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))


        # Load First Overlay Image (Button on Stone)
        self.overlay1 = pygame.image.load(os.path.join(self.images_dir,"adventure_tomb.png")).convert_alpha()
        self.overlay1 = pygame.transform.smoothscale(self.overlay1, (215, 217))  
        self.overlay1_x, self.overlay1_y = 375, 88
        self.button1_rect = pygame.Rect(self.overlay1_x, self.overlay1_y, self.overlay1.get_width(), self.overlay1.get_height())

        # Load Second Overlay Image
        self.overlay2 = pygame.image.load(os.path.join(self.images_dir,"exitgame_tomb.png")).convert_alpha()
        self.overlay2 = pygame.transform.smoothscale(self.overlay2, (167, 170))  
        self.overlay2_x, self.overlay2_y = 385, 240  
        self.button2_rect = pygame.Rect(self.overlay2_x, self.overlay2_y, self.overlay2.get_width(), self.overlay2.get_height())

    # Function to move the first overlay up
    def move_overlay1_up():
        global overlay1_y, button1_rect
        overlay1_y -= 80
        button1_rect.y = overlay1_y

    def loadHomescreen(self):
        # Main Loop
        running = True
        while running:
            self.screen.blit(self.background_image, (0, 0))  
            self.screen.blit(self.overlay1, (self.overlay1_x, self.overlay1_y))  
            self.screen.blit(self.overlay2, (self.overlay2_x, self.overlay2_y))  

            # Get Mouse Position
            mouse_pos = pygame.mouse.get_pos()

            # Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button1_rect.collidepoint(event.pos):
                        running = False
                    elif self.button2_rect.collidepoint(event.pos):
                        pygame.quit()
                        quit()

            pygame.display.flip()