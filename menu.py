from utils import quit, width, height, red, screen
import pygame

black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0
blue = 0, 0, 255

button_width = 200
button_height = 70     

BackButton = pygame.Rect(width/2 - button_width/2, height/2 - button_height/2+160, button_width, button_height)

def menu():
    menu = True
    while menu:
        screen.blit(pygame.image.load("./japaneseBackgroud.jpg"), (-600,-50))
        pygame.draw.rect(screen, red, BackButton)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BackButton.collidepoint(pygame.mouse.get_pos()):
                    menu = False

            elif event.type == pygame.QUIT:
                quit()
        pygame.display.update()
