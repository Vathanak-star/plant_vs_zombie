import pygame

class Peashooter:
    def __init__(self,x,y,peashooter_img):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 70
        self.peashooter_img = peashooter_img

    def show_peashooter_img(self, screen):
        screen.blit(self.peashooter_img, (self.x,self.y))