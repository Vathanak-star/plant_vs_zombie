import pygame
import random

class Sunflower:
    def __init__(self,x,y,sunflower_img,sun_img):
        self.x = x
        self.y = y
        self.sunflower_img = sunflower_img
        self.sun_img = sun_img
        self.last_sun_time = 0
        self.sun_cooldown = 5000
        self.fall_range = 70
        self.health = 5000
        self.rect = pygame.Rect (x,y,70,70)

    def show_sunflower_img(self,screen):
        screen.blit(self.sunflower_img, (self.x,self.y))

    def produce_sun(self,current_time):
        if current_time - self.last_sun_time >= self.sun_cooldown:
            self.last_sun_time = current_time

            sun_width = self.sun_img.get_width()
            spawn_x = self.x + random.randint(0, self.fall_range - sun_width)
            spawn_y = self.y

            stop_y = self.y + self.fall_range

            return SpawnSun(spawn_x,spawn_y, self.sun_img,stop_y)
        return None

class SpawnSun:
    def __init__(self,x,y,sun_img,stop_y):
        self.x = x
        self.y = y
        self.sun_img = sun_img
        self.speed = 1
        self.stop_y = stop_y
        self.is_moving = True

    def move(self):
        if self.is_moving:
            self.y += self.speed

            if self.y >= self.stop_y:
                self.is_moving = False
    
    def show_sun_img(self,screen):
        screen.blit(self.sun_img,(self.x,self.y))