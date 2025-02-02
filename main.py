from plants.peashooter import Peashooter
from plants.sunflower import Sunflower
from plants.wallnut import Wallnut

import pygame
import os
import random

pygame.init()

#Set up screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Plant Vs Zombie')
font = pygame.font.SysFont('comicsansms',20,bold=True)

sun_count = 0
sun_text = font.render(str(sun_count),True,(0,0,0))
sunRect = sun_text.get_rect()
sunRect.topleft = (35,67)

#Define Paths to the image
base_dir = os.path.dirname(__file__)
assets_dir = os.path.join(base_dir, 'assets')
images_dir = os.path.join(assets_dir, 'images')

#gameplay background image
background_image = pygame.image.load(os.path.join(images_dir, 'pvz_background.jpg')).convert()
background_image = pygame.transform.scale(background_image, (800, 800))

sun_image = pygame.image.load(os.path.join(images_dir,'sun.png')).convert_alpha()
sun_image = pygame.transform.scale(sun_image, (40,40))

#woodboard pvz
woodboard_img = pygame.image.load(os.path.join(images_dir,'woodboard_pvz.png')).convert_alpha()
woodboard_img = pygame.transform.scale(woodboard_img,(550,100))
woodboard_rect = woodboard_img.get_rect()
woodboard_rect.topleft = (0,0)

#Peashooter_card
peashooter_card_img = pygame.image.load(os.path.join(images_dir, 'peashooter_card_image.png')).convert()
peashooter_card_img = pygame.transform.scale(peashooter_card_img, (55, 75))
peashooter_card_rect = peashooter_card_img.get_rect()
peashooter_card_rect.topleft = (90,12)

#peashooter
peashooter_img = pygame.image.load(os.path.join(images_dir, 'peashooter.png')).convert_alpha()
peashooter_img = pygame.transform.scale(peashooter_img, (70, 70))
peashooter_rect = peashooter_card_img.get_rect()
peashooter_rect.center = (200,10)

#peashooter ammo or bullet
ammo_img = pygame.image.load(os.path.join(images_dir, 'peashooter_ammo.png')).convert_alpha()
ammo_img = pygame.transform.scale(ammo_img, (30, 30))

dragging_peashooter = False
offset_x = 0
offset_y = 0

ghost_peashooter_img = peashooter_img.copy()
ghost_peashooter_img.set_alpha(150)
placed_peashooter = []


#sunflower Card
sunflower_card_img = pygame.image.load(os.path.join(images_dir,'sunflower_card_img.png')).convert_alpha()
sunflower_card_img = pygame.transform.scale(sunflower_card_img, (55,75))
sunflower_card_rect = sunflower_card_img.get_rect()
sunflower_card_rect.topleft = (155,12)


#sunflower Image
sunflower_img = pygame.image.load(os.path.join(images_dir,'sunflower_img.png')).convert_alpha()
sunflower_img = pygame.transform.scale(sunflower_img, (70,70))
sunflower_rect = sunflower_img.get_rect()
sunflower_rect.center = (300,10)

dragging_sunflower = False
offset_sunflower_x = 0
offset_sunflower_y = 0

ghost_sunflower_img = sunflower_img.copy()
ghost_sunflower_img.set_alpha(150)
placed_sunflower = []
active_suns = []

#wallnut card & plant
wallnut_card_img = pygame.image.load(os.path.join(images_dir,'wallnut_card_imge.png'))
wallnut_card_img = pygame.transform.scale(wallnut_card_img,(55,75))
wallnut_card_rect = wallnut_card_img.get_rect()
wallnut_card_rect.topleft = (220,12)

wallnut_img = pygame.image.load(os.path.join(images_dir, 'wallnut_img.png')).convert_alpha()
wallnut_img = pygame.transform.scale(wallnut_img, (70, 70))
wallnut_rect = wallnut_img.get_rect()
wallnut_rect.center = (220,12)

dragging_wallnut = False
offset_wallnut_x = 0
offset_wallnut_y = 0

ghost_wallnut_img = wallnut_img.copy()
ghost_wallnut_img.set_alpha(150)
placed_wallnut = []

#lawn mowing car
lawn_car_img = pygame.image.load(os.path.join(images_dir,'lawn_mowing.png'))
lawn_car_img = pygame.transform.scale(lawn_car_img,(60,60))

lawn_car_rect1 = lawn_car_img.get_rect()
lawn_car_rect1.topleft = (0,150)

lawn_car_rect2 = lawn_car_img.get_rect()
lawn_car_rect2.topleft = (0,290)

lawn_car_rect3 = lawn_car_img.get_rect()
lawn_car_rect3.topleft = (-5,420)

lawn_car_rect4 = lawn_car_img.get_rect()
lawn_car_rect4.topleft = (-10,570)

lawn_car_rect5 = lawn_car_img.get_rect()
lawn_car_rect5.topleft = (-15,710)

shovel_card_img = pygame.image.load(os.path.join(images_dir,'shovel.png')).convert_alpha()
shovel_card_img = pygame.transform.scale(shovel_card_img, (55,75))
shovel_card_rect = shovel_card_img.get_rect()
shovel_card_rect.topleft = (550,3)

menu_card_img = pygame.image.load(os.path.join(images_dir,'menu.png')).convert_alpha()
menu_card_img = pygame.transform.scale(menu_card_img, (60,60))
menu_card_rect = menu_card_img.get_rect()
menu_card_rect.topleft = (740,3)


#doing row and colunms to create cell
valid_area = pygame.Rect(50,100,740,700)

rows = 5
columns = 9
cell_width = valid_area.width // columns
cell_height = valid_area.height // rows

grid = []
for row in range(rows):
    grid.append([])
    for col in range(columns):
        cell_rect = pygame.Rect(
            valid_area.x + col * cell_width,
            valid_area.y + row * cell_height,
            cell_width,
            cell_height
        )
        grid[row].append(cell_rect)

grid_occupied = [[False for _ in range(columns)] for _ in range(rows)]

sun = []
for i in range(5):
    x = random.randrange(0,800)
    y = random.randrange(-50,-10)
    sun.append([x,y])

clock = pygame.time.Clock()

peashooter = Peashooter

bullets = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for sun_drop in sun[:]:
                sun_rect = pygame.Rect(sun_drop[0] , sun_drop[1], 35, 35)
                if sun_rect.collidepoint(mouse_pos):
                    sun_count = sun_count + 50
                    print(sun_count)
                    sun.remove(sun_drop) 
                    x = random.randrange(0,800)
                    y = random.randrange(-50,-10)
                    sun.append([x,y])
                    sun_text = font.render(str(sun_count),True,(0,0,0))
                    sunRect = sun_text.get_rect()
                    if sun_count == 0:
                        sunRect.topleft = (35,67)
                    elif sun_count > 0 and sun_count < 100:
                        sunRect.topleft = (30,67)
                    elif sun_count >= 100 and sun_count < 1000:
                        sunRect.topleft = (24,67)
                    elif sun_count >= 1000:
                        sunRect.topleft = (19,67)

            for active_sun_drop in active_suns[:]:
                active_sun_rect = pygame.Rect(active_sun_drop.x, active_sun_drop.y, 35,35)
                if active_sun_rect.collidepoint(mouse_pos):
                    active_suns.remove(active_sun_drop)
                    sun_count = sun_count + 50
                    print(sun_count)
                    sun_text = font.render(str(sun_count),True,(0,0,0))
                    sunRect = sun_text.get_rect()
                    if sun_count == 0:
                        sunRect.topleft = (35,67)
                    elif sun_count > 0 and sun_count < 100:
                        sunRect.topleft = (30,67)
                    elif sun_count >= 100 and sun_count < 1000:
                        sunRect.topleft = (24,67)
                    elif sun_count >= 1000:
                        sunRect.topleft = (19,67)
            
            #peashooter
            if peashooter_card_rect.collidepoint(mouse_pos) and not dragging_peashooter:
                print('Peashooter Clicked')
                peashooter_rect.bottomright = (130,80)
                if sun_count >= 100: 
                    dragging_peashooter = True
                    mouse_x, mouse_y = event.pos
                    offset_x = peashooter_rect.x - mouse_x // 2
                    offset_y = peashooter_rect.y - mouse_y // 2
            elif dragging_peashooter:
                for row in range(rows):
                    for col in range(columns):
                        if grid[row][col].collidepoint(mouse_pos) and not grid_occupied[row][col]:
                            cell_peashooter_rect = grid[row][col]
                            pos_x = cell_peashooter_rect.centerx - peashooter_img.get_width() // 2
                            pos_y = cell_peashooter_rect.centery - peashooter_img.get_height() // 2
                            # placed_peashooter.append((pos_x,pos_y))
                            placed_peashooter.append(Peashooter(pos_x,pos_y,peashooter_img,ammo_img))
                            grid_occupied[row][col] = True
                            dragging_peashooter = False
                            sun_count = sun_count - 100
                            sun_text = font.render(str(sun_count),True,(0,0,0))
                            sunRect = sun_text.get_rect()
                            if sun_count == 0:
                                sunRect.topleft = (35,67)
                            elif sun_count > 0 and sun_count < 100:
                                sunRect.topleft = (30,67)
                            elif sun_count >= 100 and sun_count < 1000:
                                sunRect.topleft = (24,67)
                            elif sun_count >= 1000:
                                sunRect.topleft = (19,67)
            #sunflower
            if sunflower_card_rect.collidepoint(mouse_pos) and not dragging_sunflower:
                print('Sunflower Clicked')
                sunflower_rect.bottomright = (220,80)
                if sun_count >= 50:
                    dragging_sunflower = True
                    mouse_sun_x, mouse_sun_y = event.pos
                    offset_sunflower_x = sunflower_rect.x - mouse_sun_x // 2
                    offset_sunflower_y = sunflower_rect.y - mouse_sun_y // 2
            elif dragging_sunflower:
                for row in range(rows):
                    for col in range(columns):
                        if grid[row][col].collidepoint(mouse_pos) and not grid_occupied[row][col]:
                            cell_sunflower_rect = grid[row][col]
                            pos_sun_x = cell_sunflower_rect.centerx - sunflower_img.get_width() // 2
                            pos_sun_y = cell_sunflower_rect.centery - sunflower_img.get_height() // 2
                            # placed_sunflower.append((pos_sun_x,pos_sun_y))
                            placed_sunflower.append(Sunflower(pos_sun_x,pos_sun_y,sunflower_img,sun_image))
                            grid_occupied[row][col] = True
                            dragging_sunflower = False
                            sun_count = sun_count -  50
                            sun_text = font.render(str(sun_count),True,(0,0,0))
                            sunRect = sun_text.get_rect()
                            if sun_count == 0:
                                sunRect.topleft = (35,67)
                            elif sun_count > 0 and sun_count < 100:
                                sunRect.topleft = (30,67)
                            elif sun_count >= 100 and sun_count < 1000:
                                sunRect.topleft = (24,67)
                            elif sun_count >= 1000:
                                sunRect.topleft = (19,67)

            #wallnut

            if wallnut_card_rect.collidepoint(mouse_pos) and not dragging_wallnut:
                print('Wallnut Clicked')
                wallnut_rect.bottomright = (280,80)
                if sun_count >= 50:
                    dragging_wallnut = True
                    mouse_wall_x, mouse_wall_y = event.pos
                    offset_wallnut_x = wallnut_rect.x - mouse_wall_x // 2
                    offset_wallnut_y = wallnut_rect.y - mouse_wall_y // 2
            elif dragging_wallnut:
                for row in range(rows):
                    for col in range(columns):
                        if grid[row][col].collidepoint(mouse_pos) and not grid_occupied[row][col]:
                            cell_wallnut_rect = grid[row][col]
                            pos_wall_x = cell_wallnut_rect.centerx - wallnut_img.get_width() // 2
                            pos_wall_y = cell_wallnut_rect.centery - wallnut_img.get_height() // 2
                            # placed_wallnut.append((pos_wall_x,pos_wall_y))
                            placed_wallnut.append(Wallnut(pos_wall_x,pos_wall_y,wallnut_img))
                            grid_occupied[row][col] = True
                            dragging_wallnut = False
                            sun_count = sun_count -  50
                            sun_text = font.render(str(sun_count),True,(0,0,0))
                            sunRect = sun_text.get_rect()
                            if sun_count == 0:
                                sunRect.topleft = (35,67)
                            elif sun_count > 0 and sun_count < 100:
                                sunRect.topleft = (30,67)
                            elif sun_count >= 100 and sun_count < 1000:
                                sunRect.topleft = (24,67)
                            elif sun_count >= 1000:
                                sunRect.topleft = (19,67)

        #peashooter_motion
        elif event.type == pygame.MOUSEMOTION and dragging_peashooter:
            mouse_x,mouse_y = event.pos
            peashooter_rect.center = (mouse_x,mouse_y)
        #sunflower_motion
        elif event.type == pygame.MOUSEMOTION and dragging_sunflower:
            mouse_sun_x, mouse_sun_y = event.pos
            sunflower_rect.center = (mouse_sun_x,mouse_sun_y)
        #wallnut motion
        elif event.type == pygame.MOUSEMOTION and dragging_wallnut:
            mouse_wall_x, mouse_wall_y = event.pos
            wallnut_rect.center = (mouse_wall_x,mouse_wall_y)
            

    screen.blit(background_image,(0,0))
    screen.blit(woodboard_img,woodboard_rect)
    screen.blit(sun_text,sunRect)
    screen.blit(sunflower_card_img,sunflower_card_rect)
    screen.blit(wallnut_card_img,wallnut_card_rect)
    screen.blit(peashooter_card_img,peashooter_card_rect)

    screen.blit(lawn_car_img,lawn_car_rect1)
    screen.blit(lawn_car_img,lawn_car_rect2)
    screen.blit(lawn_car_img,lawn_car_rect3)
    screen.blit(lawn_car_img,lawn_car_rect4)
    screen.blit(lawn_car_img,lawn_car_rect5)

    screen.blit(shovel_card_img,shovel_card_rect)
    screen.blit(menu_card_img,menu_card_rect)

    #wallnut
    for wallnut in placed_wallnut:
        # screen.blit(wallnut_img,wallnut)
        wallnut.show_wallnut_img(screen)

    #sunflower
    for sunflower in placed_sunflower:
        # screen.blit(sunflower_img, sunflower)
        sunflower.show_sunflower_img(screen)

    for sunflower in placed_sunflower:
        new_sun = sunflower.produce_sun(current_time)
        if new_sun:
            active_suns.append(new_sun)
    
    for suns in active_suns:
        suns.move()
        suns.show_sun_img(screen)

    for peashoot in placed_peashooter:
        # screen.blit(peashooter_img, peashoot)
        peashoot.show_peashooter_img(screen)

    current_time = pygame.time.get_ticks()
    for peashoot in placed_peashooter:
        new_bullets = peashoot.shoot(current_time)
        if new_bullets:
            bullets.append(new_bullets)

    for bullet in bullets:
        bullet.move()
        bullet.show_ammo_img(screen)


    if dragging_peashooter:
        screen.blit(ghost_peashooter_img,peashooter_rect)
        for row in range(rows):
            for col in range(columns):
                pygame.draw.rect(screen, (0,255,0), grid[row][col],1)

    if dragging_sunflower:
        screen.blit(ghost_sunflower_img,sunflower_rect)
        for row in range(rows):
            for col in range(columns):
                pygame.draw.rect(screen, (0,255,0), grid[row][col],1)

    if dragging_wallnut:
        screen.blit(ghost_wallnut_img,wallnut_rect)
        for row in range(rows):
            for col in range(columns):
                pygame.draw.rect(screen, (0,255,0), grid[row][col],1)

    for sun_drop in sun:
        screen.blit(sun_image, (sun_drop[0], sun_drop[1]))
        sun_drop[1]+= 1
        if sun_drop[1] > 800:
            sun_drop[1] = random.randrange(-50,-10)
            sun_drop[0] = random.randrange(0,800)


    pygame.display.update()
    clock.tick(40)