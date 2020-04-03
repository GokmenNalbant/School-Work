import sys
import pygame
from textscreen import TextScreen
def check_events(number):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
def check_events2(screen):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                   return '0'
                elif event.key == pygame.K_1:
                    return '1'
                elif event.key == pygame.K_2:
                    return '2'
                elif event.key == pygame.K_3:
                    return '3'
                elif event.key == pygame.K_4:
                    return '4'
                elif event.key == pygame.K_5:
                    return '5'
                elif event.key == pygame.K_6:
                    return '6'
                elif event.key == pygame.K_7:
                    return '7'
                elif event.key == pygame.K_8:
                    return '8'
                elif event.key == pygame.K_9:
                    return '9'
                elif event.key == pygame.K_SPACE:
                    return "game"

def update_screen(mg_settings,screen,number):
    screen.fill(mg_settings.back_ground_color)
    number.blitme()

    pygame.display.flip()

def update_screen2(mg_settings,screen,text):
    screen.fill(mg_settings.back_ground_color2)
    text.blitme()

    pygame.display.flip()
