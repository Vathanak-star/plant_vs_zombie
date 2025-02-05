import pygame

class NormalZombie:
    def __init__(self,x,y,zombie_img):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 70
        self.zombie_img = zombie_img
        self.speed = 1
        self.health = 100
        self.is_moving = True
        self.rect = pygame.Rect (x,y,70,70)

    def zombie_move(self):
        if self.is_moving :
            self.x -= self.speed
            self.rect.x = self.x
    
    def show_zombie_img(self,screen):
        screen.blit(self.zombie_img,(self.x,self.y))