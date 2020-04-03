import pygame.font

class TextScreen():
    def __init__(self,screen,val,x=30,y=50):
        self.screen = screen
        #self.liste = liste
        self.screen_rect = screen.get_rect()
        
        self.width = x
        self.height = y
        self.box_color = (0,255,222)
        self.text_color = (80,20,20)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.prep_val(val)
    
    def prep_val(self,val):
        self.val_image = self.font.render(val,True,self.text_color,self.box_color)
        self.val_image_rect = self.val_image.get_rect()
        self.val_image_rect.center = self.rect.center
    
    def blitme(self):
        self.screen.fill(self.box_color,self.rect)
        self.screen.blit(self.val_image,self.val_image_rect)
