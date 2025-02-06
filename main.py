from loading_screen import LoadingScreen
from home_screen import HomeScreen
from plants.peashooter import Peashooter
from plants.sunflower import Sunflower
from plants.wallnut import Wallnut
from zombie.normal_zombie import NormalZombie
import pygame
import os
import random
import pygame_gui

pygame.init()

loading = LoadingScreen()
home = HomeScreen()

loading.loading_screen()
home.loadHomescreen()
loading.loading_screen()

#load gameplay game
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Plant Vs Zombie')
font = pygame.font.SysFont('comicsansms',20,bold=True)

font1 = pygame.font.SysFont('comicsansms',13,bold=True)

sun_count = 0
sun_text = font.render(str(sun_count),True,(0,0,0))
sunRect = sun_text.get_rect()
sunRect.topleft = (35,67)

#level text
level_text = "Level: "
level_text_show = font.render(level_text,True,(0,0,0))
level_text_rect = level_text_show.get_rect()
level_text_rect.bottomright = (695,30)

level_count_text = 1
level_count_text_show = font.render(str(level_count_text),True,(0,0,0))
level_count_rect = level_count_text_show.get_rect()
level_count_rect.bottomright = (700,30)

#zombie To Kill
zombie_text = "Zombies To Kill:"
zombie_text_show = font1.render(zombie_text,True,(0,0,0))
zombie_text_rect = zombie_text_show.get_rect()
zombie_text_rect.bottomright = (715,50)

zombie_count = 0
zombie_count_text = font1.render(str(zombie_count),True,(0,0,0))
zombie_count_rect = zombie_count_text.get_rect()
zombie_count_rect.bottomright = (725,50)
 
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

#store all plants
plants = []

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

#shovel card & image
shovel_card_img = pygame.image.load(os.path.join(images_dir,'shovel.png')).convert_alpha()
shovel_card_img = pygame.transform.scale(shovel_card_img, (55,75))
shovel_card_rect = shovel_card_img.get_rect()
shovel_card_rect.topleft = (550,3)

shovel_img = pygame.image.load(os.path.join(images_dir,'shovel_img.png')).convert_alpha()
shovel_img = pygame.transform.scale(shovel_img, (70,70))
shovel_rect = shovel_img.get_rect()
shovel_rect.topleft = (550,3)
dragging_shovel = False
offset_shovel_x = 0
offset_shovel_y = 0

#menu
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

grid_occupied = [[None for _ in range(columns)] for _ in range(rows)]

sun = []
for i in range(1):
    x = random.randrange(20,780)
    y = random.randrange(-50,-10)
    sun.append([x,y])

clock = pygame.time.Clock()

peashooter = Peashooter

bullets = []
bullets_to_remove = []

#zombie
normal_zombie_img = pygame.image.load(os.path.join(images_dir,'normal_zombie.png'))
normal_zombie_img = pygame.transform.scale(normal_zombie_img,(70,70))

normal_zombie = []

level_transition = False
level_start_time = pygame.time.get_ticks()

LEVELS = {
    1:{
        "zombie_count" : 3,
        "spawn_range": (0,4),
        "spawn_chance": 100,
    },
    2:{
        "zombie_count" : 6,
        "spawn_range": (0,4),
        "spawn_chance": 100,
    },
    3:{
        "zombie_count" : 9,
        "spawn_range": (0,4),
        "spawn_chance": 100,
    }
}

current_level = 1
zombie_spawned = 0
zombie_kill = 0

gamplay_running = True
window_size = (800,800)
manager = pygame_gui.UIManager(window_size)
alert_shown = False

while gamplay_running:
    time_delta = clock.tick(40) / 1000.0 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if alert_shown and event.type == pygame_gui.UI_WINDOW_CLOSE and event.ui_element == alert_dialog and current_level == 3:
            screen = pygame.display.set_mode((800,600))
            pygame.display.set_caption('Plant Vs Zombie')
            gamplay_running = False
            manager.process_events(event)

        manager.process_events(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for sun_drop in sun[:]:
                sun_rect = pygame.Rect(sun_drop[0] , sun_drop[1], 35, 35)
                if sun_rect.collidepoint(mouse_pos):
                    sun_count = sun_count + 50
                    sun.remove(sun_drop) 
                    x = random.randrange(20,780)
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
                peashooter_rect.bottomright = (130,80)
                if sun_count >= 100: 
                    dragging_peashooter = True
                    mouse_x, mouse_y = event.pos
            elif dragging_peashooter:
                for row in range(rows):
                    for col in range(columns):
                        if grid[row][col].collidepoint(mouse_pos) and grid_occupied[row][col] is None:
                            cell_peashooter_rect = grid[row][col]
                            pos_x = cell_peashooter_rect.centerx - peashooter_img.get_width() // 2
                            pos_y = cell_peashooter_rect.centery - peashooter_img.get_height() // 2
                            # placed_peashooter.append((pos_x,pos_y))
                            new_peashooter = Peashooter(pos_x,pos_y,peashooter_img,ammo_img)
                            plants.append(new_peashooter)
                            grid_occupied[row][col] = new_peashooter
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
                sunflower_rect.bottomright = (220,80)
                if sun_count >= 50:
                    dragging_sunflower = True
                    mouse_sun_x, mouse_sun_y = event.pos
            elif dragging_sunflower:
                for row in range(rows):
                    for col in range(columns):
                        if grid[row][col].collidepoint(mouse_pos) and grid_occupied[row][col] is None:
                            cell_sunflower_rect = grid[row][col]
                            pos_sun_x = cell_sunflower_rect.centerx - sunflower_img.get_width() // 2
                            pos_sun_y = cell_sunflower_rect.centery - sunflower_img.get_height() // 2
                            # placed_sunflower.append((pos_sun_x,pos_sun_y))
                            new_sunflower = Sunflower(pos_sun_x,pos_sun_y,sunflower_img,sun_image)
                            plants.append(new_sunflower)
                            grid_occupied[row][col] = new_sunflower
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
                wallnut_rect.bottomright = (280,80)
                if sun_count >= 50:
                    dragging_wallnut = True
                    mouse_wall_x, mouse_wall_y = event.pos
            elif dragging_wallnut:
                for row in range(rows):
                    for col in range(columns):
                        if grid[row][col].collidepoint(mouse_pos) and grid_occupied[row][col] is None:
                            cell_wallnut_rect = grid[row][col]
                            pos_wall_x = cell_wallnut_rect.centerx - wallnut_img.get_width() // 2
                            pos_wall_y = cell_wallnut_rect.centery - wallnut_img.get_height() // 2
                            # placed_wallnut.append((pos_wall_x,pos_wall_y))
                            new_wallnut = Wallnut(pos_wall_x,pos_wall_y,wallnut_img)
                            plants.append(new_wallnut)
                            grid_occupied[row][col] = new_wallnut
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

            #shovel
            if shovel_card_rect.collidepoint(mouse_pos) and not dragging_shovel:
                print('Shovel Clicked')
                shovel_rect.bottomright = (610,80)
                dragging_shovel = True
                mouse_shovel_x, mouse_shovel_y = event.pos
            elif dragging_shovel:
                clicked_cell = False
                for row in range(rows):
                    for col in range(columns):
                        if grid[row][col].collidepoint(mouse_pos):
                            clicked_cell = True
                            if grid_occupied[row][col] is not None:
                                plant_to_remove = grid_occupied[row][col]
                                if plant_to_remove in plants:
                                    plants.remove(plant_to_remove)
                                grid_occupied[row][col] = None
                            dragging_shovel = False
                            shovel_rect.bottomright = (offset_shovel_x,offset_shovel_y)
                            break
                    if clicked_cell:
                        break

                if not clicked_cell:
                    dragging_shovel = False
                    shovel_rect.topleft = (550,3)

                                    
                                
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
        #shovel motion
        elif event.type == pygame.MOUSEMOTION and dragging_shovel:
            mouse_shovel_x,mouse_shovel_y = event.pos
            shovel_rect.center = (mouse_shovel_x,mouse_shovel_y)
            

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

    screen.blit(level_text_show,level_text_rect)
    screen.blit(level_count_text_show,level_count_rect)

    screen.blit(zombie_text_show,zombie_text_rect)
    screen.blit(zombie_count_text,zombie_count_rect)

    current_time = pygame.time.get_ticks()
    manager.update(time_delta)



    #wallnut
    for plant in plants:
        # screen.blit(wallnut_img,wallnut)
        if isinstance(plant, Wallnut):
             plant.show_wallnut_img(screen)
        elif isinstance(plant,Sunflower):
            plant.show_sunflower_img(screen)
            new_sun = plant.produce_sun(current_time)
            if new_sun:
                active_suns.append(new_sun)
        elif isinstance(plant,Peashooter):
            plant.show_peashooter_img(screen)
            new_bullets = plant.shoot(current_time)
            if new_bullets:
                bullets.append(new_bullets)
    
    for suns in active_suns:
        suns.move()
        suns.show_sun_img(screen)

    for bullet in bullets:
        bullet.move()
        bullet.show_ammo_img(screen)

    transiton_start_time = 0
    if zombie_spawned >= LEVELS[current_level]["zombie_count"] and zombie_kill == LEVELS[current_level]["zombie_count"]:
        if current_level < max(LEVELS.keys()):
            level_transition = True
            transiton_start_time = 0
            if not alert_shown:
                alert_dialog = pygame_gui.windows.UIMessageWindow(
                    rect=pygame.Rect((250, 200), (300, 150)),
                    html_message='<b>Level Completed</b><br>Welcome To New Level',
                    manager=manager,
                    window_title='Congratulations'
                )
                alert_shown = True
        else:
            if not alert_shown:
                alert_dialog = pygame_gui.windows.UIMessageWindow(
                    rect=pygame.Rect((250, 200), (300, 150)),
                    html_message='<b>You Win!</b><br>Game Completed.',
                    manager=manager,
                    window_title='Congratulations'
                )
                alert_shown = True
    if level_transition and zombie_kill == LEVELS[current_level]["zombie_count"]:
        if pygame.time.get_ticks() - transiton_start_time >= 10000:
            zombie_kill = 0
            level_transition = False
            current_level += 1
            zombie_spawned = 0
            level_start_time = pygame.time.get_ticks()
            print(f"Start Level {current_level}")
            level_count_text_show = font.render(str(current_level),True,(0,0,0))
            level_count_rect.bottomright = (700,30)
            plants.clear()
            grid_occupied = [[None for _ in range(columns)] for _ in range(rows)]
            bullets.clear()
            normal_zombie.clear()
            sun_count = 0
            sun_text = font.render(str(sun_count),True,(0,0,0))
            sunRect = sun_text.get_rect()
            if sun_count == 0:
                sunRect.topleft = (35,67)
            alert_shown = False

    if not level_transition:
        current_times = pygame.time.get_ticks()
        zombie_count_text = font1.render(f"{LEVELS[current_level]['zombie_count']}", True, (0,0,0))
        screen.blit(zombie_count_text, zombie_count_rect)
        level_data = LEVELS[current_level]
        if (current_times - level_start_time > 10000 and
            random.randint(0, level_data['spawn_chance']) == 0 and
            zombie_spawned < level_data['zombie_count']):
            min_rox, max_row = level_data["spawn_range"]
            row = random.randint(min_rox, max_row)

            cell_height = valid_area.height // rows
            spawn_y = valid_area.y + row * cell_height + (cell_height - 115)

            spawn_x = valid_area.right
            normal_zombie.append(NormalZombie(spawn_x,spawn_y,normal_zombie_img))
            zombie_spawned += 1
            print(zombie_spawned)




    for zombie in normal_zombie:
        zombie.zombie_move()
        zombie.show_zombie_img(screen)

    for zombie in normal_zombie:
        for bullet in bullets:
            if zombie.x < bullet.x < zombie.x + zombie.width and zombie.y < bullet.y < zombie.y + zombie.height:
                zombie.health -= 20
                bullets.remove(bullet)
                if zombie.health <= 0:
                    normal_zombie.remove(zombie)
                    zombie_kill = zombie_kill + 1
                    print( "zomebie kill: " + str(zombie_kill))
                    break

    for zombie in normal_zombie:
        zombie.is_moving = True
        for plant in plants:
            if zombie.rect.colliderect(plant.rect):
                zombie.is_moving = False
                plant.health -= 20
                if plant.health <= 0:
                    for row in range(rows):
                        for col in range(columns):
                            grid_occupied[row][col] = None
                    plants.remove(plant)
                    zombie.is_moving = True
                break


    if dragging_peashooter:
        screen.blit(ghost_peashooter_img,peashooter_rect)
        for row in range(rows):
            for col in range(columns):
                cell_rect = grid[row][col]
                if grid_occupied[row][col] is None:
                    pygame.draw.rect(screen, (0,255,0), cell_rect,1)
                else:
                    pygame.draw.rect(screen, (255,0,0), cell_rect,1)

    if dragging_sunflower:
        screen.blit(ghost_sunflower_img,sunflower_rect)
        for row in range(rows):
            for col in range(columns):
                cell_rect = grid[row][col]
                if grid_occupied[row][col] is None:
                    pygame.draw.rect(screen, (0,255,0), cell_rect,1)
                else:
                    pygame.draw.rect(screen, (255,0,0), cell_rect,1)

    if dragging_wallnut:
        screen.blit(ghost_wallnut_img,wallnut_rect)
        for row in range(rows):
            for col in range(columns):
                cell_rect = grid[row][col]
                if grid_occupied[row][col] is None:
                    pygame.draw.rect(screen, (0,255,0), cell_rect,1)
                else:
                    pygame.draw.rect(screen, (255,0,0), cell_rect,1)

    if dragging_shovel:
        screen.blit(shovel_img,shovel_rect)
        for row in range(rows):
            for col in range(columns):
                cell_rect = grid[row][col]
                if grid_occupied[row][col] is None:
                    pygame.draw.rect(screen, (0,255,0), cell_rect,1)
                else:
                    pygame.draw.rect(screen, (255,0,0), cell_rect,1)

    for sun_drop in sun:
        screen.blit(sun_image, (sun_drop[0], sun_drop[1]))
        sun_drop[1]+= 1
        if sun_drop[1] > 800:
            sun_drop[1] = random.randrange(-50,-10)
            sun_drop[0] = random.randrange(0,800)

    manager.draw_ui(screen)
    pygame.display.flip()
    clock.tick(60)

loading.loading_screen()
home.loadHomescreen()