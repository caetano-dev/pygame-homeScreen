from menu import menu
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
PlayButton = pygame.Rect((width/2)-BUTTON_WIDTH/2, (height/1.5)-BUTTON_HEIGHT/2-100, BUTTON_WIDTH, BUTTON_HEIGHT)
MenuButton = pygame.Rect((width/2)-BUTTON_WIDTH/2, (height/1.5)-BUTTON_HEIGHT/2, BUTTON_WIDTH, BUTTON_HEIGHT)
LeaveButton = pygame.Rect((width/2)-BUTTON_WIDTH/2, (height/1.5)-BUTTON_HEIGHT/2+100, BUTTON_WIDTH, BUTTON_HEIGHT)

pygame.init()

def intro():
    intro = True
    while intro:
        screen.blit(pygame.image.load("./japaneseBackgroud.jpg"), (-600,-50))

        pygame.draw.rect(screen, green, PlayButton)  # draw play button
        pygame.draw.rect(screen, red, MenuButton)  # draw manu button
        pygame.draw.rect(screen, blue, LeaveButton)  # draw leave button


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if PlayButton.collidepoint(pygame.mouse.get_pos()):
                    print("Play button clicked")
                    # play()

                if MenuButton.collidepoint(pygame.mouse.get_pos()):
                    print("Menu button clicked")
                    menu()

                if LeaveButton.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
intro()
