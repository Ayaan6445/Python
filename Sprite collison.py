import pygame
import random
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transfrorm.scale(pygame.image.load("bg.jpg"),
                                           (SCREEN_WIDTH, SCREEN_HEIGHT))


font = pygame.font.Sysfont("Times New Roman", FONT_SIZE)