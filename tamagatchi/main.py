import pygame, os, sys
from pygame.locals import *
from modules.Food import food

#handlig input
def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            # print(event)
            i = 1

def main():
    print('Tomogatchi Project Startup, in development stage')
    #init pygame
    pygame.init()
    
    fd = food.Food()
    item = fd.get_food('Tin')
    print(item['RFID'])
    
    icon = pygame.image.load('tamagatchi/assets/icons/tamagotchi.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Tamagatchie')
    # The window size w x h
    # window = pygame.display.set_mode((500,250), pygame.NOFRAME)
    window = pygame.display.set_mode((500,250))
    screen = pygame.display.get_surface()
    
    # screen.blit()
    pygame.display.flip()
    
    running = True
    while running:
        input(pygame.event.get())
        screen.fill(( 0, 0, 0))
        pygame.display.update()
    
    
if __name__=='__main__':
    main()
    
