import pygame
import random
class Numberss():

    def __init__(self,screen,numberlist):
        self.screen = screen
        self.number = random.choice(numberlist)
        
        if self.number == 0:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/0.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        elif self.number == 1:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/1.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        elif self.number == 2:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/2.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        elif self.number == 3:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/3.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        elif self.number == 4:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/4.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        elif self.number == 5:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/5.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        elif self.number == 6:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/6.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        elif self.number == 7:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/7.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        elif self.number == 8:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/8.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        elif self.number == 9:
            self.image = pygame.image.load("C:/Users/hacı/Desktop/memory game/9.bmp")
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
        self.place_width = random.randint(50,1150)
        self.place_height = random.randint(150,790)

        self.rect.centerx = self.place_width
        self.rect.bottom = self.place_height
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
