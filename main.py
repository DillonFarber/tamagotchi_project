import pygame, os, sys
from pygame.locals import *

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
    
    icon = pygame.image.load('assets/icons/tamagotchi.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Tamagatchie')
    window = pygame.display.set_mode((500,250))
    screen = pygame.display.get_surface()
    
    # screen.blit()
    pygame.display.flip()
    
    running = True
    while running:
        input(pygame.event.get())
        screen.fill(( 255, 255, 255))
        pygame.display.update()
    
    
if __name__=='__main__':
    main()
    
