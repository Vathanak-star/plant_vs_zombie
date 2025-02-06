from loading_screen import LoadingScreen
from home_screen import HomeScreen
import pygame
import os

pygame.init()

loading = LoadingScreen()
home = HomeScreen()

loading.loading_screen()
home.main_menu()