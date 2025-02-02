import pygame

class Wallnut:
    def __init__(self,x,y,wallnut_img):
        self.x = x
        self.y = y
        self.wallnut_img = wallnut_img
    
    def show_wallnut_img(self,screen):
        screen.blit(self.wallnut_img, (self.x,self.y))