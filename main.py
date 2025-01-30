import pygame
import os
import random

pygame.init()

#Set up screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Plant Vs Zombie')
font = pygame.font.SysFont('inkfree',30,italic=True,bold=True)

display_text = 'Sun Count: '
display_text = font.render(display_text,True,(0,0,0))
display_textRect = display_text.get_rect()
display_textRect.topleft = (20,20)

sun_count = 0
sun_text = font.render(str(sun_count),True,(0,0,0))
sunRect = sun_text.get_rect()
sunRect.topleft = (60,50)

#Define Paths to the image
base_dir = os.path.dirname(__file__)
assets_dir = os.path.join(base_dir, 'assets')
images_dir = os.path.join(assets_dir, 'images')

background_image = pygame.image.load(os.path.join(images_dir, 'pvz_background.jpg')).convert()
background_image = pygame.transform.scale(background_image, (800, 800))
sun_image = pygame.image.load(os.path.join(images_dir,'sun.png')).convert_alpha()
sun_image = pygame.transform.scale(sun_image, (40,40))

#Peashooter_card
peashooter_card_img = pygame.image.load(os.path.join(images_dir, 'peashooter_card_image.jpg')).convert()
peashooter_card_img = pygame.transform.scale(peashooter_card_img, (80, 80))
peashooter_card_rect = peashooter_card_img.get_rect()
peashooter_card_rect.topleft = (200,10)

#peashooter
peashooter_img = pygame.image.load(os.path.join(images_dir, 'peashooter.png')).convert_alpha()
peashooter_img = pygame.transform.scale(peashooter_img, (100, 100))
peashooter_rect = peashooter_card_img.get_rect()
peashooter_rect.topleft = (200,10)

dragging_peashooter = False
offset_x = 0
offset_y = 0

ghost_peashooter_img = peashooter_img.copy()
ghost_peashooter_img.set_alpha(150)
placed_peashooter = []

valid_area = pygame.Rect(50,100,740,700)

sun = []
for i in range(5):
    x = random.randrange(0,800)
    y = random.randrange(-50,-10)
    sun.append([x,y])

clock = pygame.time.Clock()

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
                    sun_count = sun_count + 100
                    print(sun_count)
                    sun.remove(sun_drop) 
                    x = random.randrange(0,800)
                    y = random.randrange(-50,-10)
                    sun.append([x,y])
                    sun_text = font.render(str(sun_count),True,(0,0,0))
                    sunRect = sun_text.get_rect()
                    sunRect.topleft = (60,50)
            if peashooter_card_rect.collidepoint(mouse_pos) and not dragging_peashooter:
                print('Peashooter Clicked')
                peashooter_rect.bottomright = (270,80)
                if sun_count > 0: 
                    dragging_peashooter = True
                    mouse_x, mouse_y = event.pos
                    offset_x = peashooter_rect.x - mouse_x
                    offset_y = peashooter_rect.y - mouse_y
            elif dragging_peashooter:
                if valid_area.collidepoint(mouse_pos):
                    placed_peashooter.append(peashooter_rect.topleft)
                    dragging_peashooter = False
                    sun_count = sun_count - 100
                    sun_text = font.render(str(sun_count),True,(0,0,0))
                    sunRect = sun_text.get_rect()
                    sunRect.topleft = (60,50)
        elif event.type == pygame.MOUSEMOTION and dragging_peashooter:
            mouse_x,mouse_y = event.pos
            peashooter_rect.x = mouse_x + offset_x
            peashooter_rect.y = mouse_y + offset_y

    screen.blit(background_image,(0,0))
    screen.blit(sun_text,sunRect)
    screen.blit(display_text,display_textRect)
    screen.blit(peashooter_card_img,peashooter_card_rect)

    for pos in placed_peashooter:
        screen.blit(peashooter_img, pos)

    if dragging_peashooter:
        screen.blit(ghost_peashooter_img,peashooter_rect)
        pygame.draw.rect(screen, (0,255,0), valid_area,2)

    for sun_drop in sun:
        screen.blit(sun_image, (sun_drop[0], sun_drop[1]))
        sun_drop[1]+= 1
        if sun_drop[1] > 800:
            sun_drop[1] = random.randrange(-50,-10)
            sun_drop[0] = random.randrange(0,800)


    pygame.display.update()
    clock.tick(40)