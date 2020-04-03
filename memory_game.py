import sys
import pygame
from numberss import Numberss
import game_functions as gf
from settings import Settings
from textscreen import TextScreen
def rungame():
    pygame.init()
    mg_settings=Settings()
    
    screen = pygame.display.set_mode((mg_settings.screen_width,mg_settings.screen_height))
    pygame.display.set_caption("MeMoRY GaMe")
    
    gameactive = True
    level = 1
    i = 2000
    r = 5
    while True:        
        text = TextScreen(screen,"SPACE FOR START THE GAME",800,80)
        game_control = gf.check_events2(screen)
        gf.update_screen2(mg_settings,screen,text)
        if game_control == "game":
            break

    text = TextScreen(screen,"YOU HAVE 3 HEALTH FOR EVERY LEVEL",800,80)
    game_control = gf.check_events2(screen)
    gf.update_screen2(mg_settings,screen,text)
    pygame.time.wait(3000)
    text = TextScreen(screen,"THE FIRST SIZE OF PATTERN WILL INCLUDE FIVE NUMBERS",1000,80)
    game_control = gf.check_events2(screen)
    gf.update_screen2(mg_settings,screen,text)
    pygame.time.wait(3000)

    while True:
        health = 3       
        text = TextScreen(screen,f"LEVEL {level}",800,80)
        game_control = gf.check_events2(screen)
        gf.update_screen2(mg_settings,screen,text)
        pygame.time.wait(3000)
        
        level += 1
        if gameactive == True:
            numberlist = [0,1,2,3,4,5,6,7,8,9]
            holding_number = []
            for x in range(r):
                number = Numberss(screen,numberlist)
                holding_number.append(number.number)
                gf.check_events(number)
                gf.update_screen(mg_settings,screen,number)
                pygame.time.wait(i)
                if r <= 9:
                    numberlist.remove(number.number)            
                
            r+=1
            if i<=50:
                i=50
            else:
                i-=50

            
        text = TextScreen(screen,"ENTER THE NUMBER",500)
        gf.update_screen2(mg_settings,screen,text)
        pygame.time.wait(2200)
        j=0
        while True:
            val = gf.check_events2(screen)
            gf.update_screen2(mg_settings,screen,text)
            if val == '0' or val == '1' or val == '2' or val == '3' or val == '4' or val == '5' or val == '6' or val == '7' or val == '8' or val == '9':
                gf.check_events2(screen)
                text = TextScreen(screen,val)
                gf.update_screen2(mg_settings,screen,text)
                pygame.time.wait(1500)
                text = TextScreen(screen,"...")
                gf.update_screen2(mg_settings,screen,text)
                pygame.time.wait(800)
                if str(holding_number[j]) == val:
                    text = TextScreen(screen,"CORRECT!",300,60)
                    gf.update_screen2(mg_settings,screen,text)
                    pygame.time.wait(1000)
                    j+=1
                else:
                    text = TextScreen(screen,"WRONG!",300,60)
                    gf.update_screen2(mg_settings,screen,text)
                    pygame.time.wait(1000)
                    health -= 1
                    if health == 0:
                        text = TextScreen(screen,"YOU FAILED!!!",300,60)
                        gf.update_screen2(mg_settings,screen,text)
                        pygame.time.wait(2000)
                        break
                
                if j >= len(holding_number):
                    text = TextScreen(screen,"WELL DONE!!!",400,60)
                    gf.update_screen2(mg_settings,screen,text)
                    pygame.time.wait(2000)
                    break
        if health == 0:
            while True:
                text = TextScreen(screen,"SPACE FOR NEW GAME",500,70)
                game_control = gf.check_events2(screen)
                gf.update_screen2(mg_settings,screen,text)
                level=1
                r=5
                i=2000
                if game_control == "game":
                    break
        else:
            while True:
                text = TextScreen(screen,"SPACE FOR NEXT LEVEL",500,70)
                game_control = gf.check_events2(screen)
                gf.update_screen2(mg_settings,screen,text)
                if game_control == "game":
                    break
            
        del holding_number
           
            
    

rungame()
