import pygame

class Peashooter:
    def __init__(self,x,y,peashooter_img,ammo_img):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 70
        self.peashooter_img = peashooter_img
        self.ammo_img = ammo_img
        self.last_shot_time = 0
        self.shot_cooldown = 1000
        self.health = 100
        self.rect = pygame.Rect (x,y,70,70)

    def show_peashooter_img(self,screen):
        screen.blit(self.peashooter_img, (self.x,self.y))
    
    def shoot(self,current_time):
        if current_time - self.last_shot_time > self.shot_cooldown:
            self.last_shot_time = current_time
            return Bullet(self.x + self.width, self.y + self.height // 22,self.ammo_img)
        return None

class Bullet:
    def __init__(self,x,y,ammo_img):
        self.x = x
        self.y = y
        self.speed = 5
        self.ammo_img = ammo_img

    def move(self):
        self.x += self.speed
    
    def show_ammo_img(self,screen):
        screen.blit(self.ammo_img, (self.x,self.y))