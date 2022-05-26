import pygame
import sys
size = width, height = 500, 800 

black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0
blue = 0, 0, 255

screen = pygame.display.set_mode(size)
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 70               #x               -           y                   -     width   -      height
BackButton = pygame.Rect((width/2)-BUTTON_WIDTH/2, (height/1.5)-BUTTON_HEIGHT/2, BUTTON_WIDTH, BUTTON_HEIGHT)
LeaveButton = pygame.Rect((width/2)-BUTTON_WIDTH/2, (height/1.5)-BUTTON_HEIGHT/2+100, BUTTON_WIDTH, BUTTON_HEIGHT)

def menu():
    menu = True
    while menu:
        screen.blit(pygame.image.load("./japaneseBackgroud.jpg"), (-600,-50))
        pygame.draw.rect(screen, red, BackButton)  # draw back button
        pygame.draw.rect(screen, blue, LeaveButton)  # draw leave button

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if BackButton.collidepoint(pygame.mouse.get_pos()):
                    menu = False

                if LeaveButton.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

            #leave game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
