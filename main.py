from menu import menu
from utils import button, leave, play, width, height, green, blue, screen, button_height, button_width
import pygame

pygame.init()

def intro():
    intro = True
    while intro:
        print("intro")
        screen.blit(pygame.image.load("./japaneseBackgroud.jpg"), (-600,-50))

        button("Play", width/2 - button_width/2, height/2 - button_height/2, button_width, button_height, green, blue, play)
        button("Menu", width/2 - button_width/2, height/2 + button_height/2, button_width, button_height, green, blue, menu)
        button("Leave", width/2 - button_width/2, height/2 + button_height*2, button_width, button_height, green, blue, leave)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leave()
        pygame.display.update()
intro()
