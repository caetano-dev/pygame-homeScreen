from menu import menu
from utils import button, quit, play, width, height, green, blue, screen, button_height, button_width, shop
import pygame

pygame.init()

def intro():
    intro = True
    while intro:
        print("intro")
        screen.blit(pygame.image.load("./japaneseBackgroud.jpg"), (-600,-50))
        # add image to button
        button("Play", width/2 - button_width/2, height/2 - button_height/2+40, button_width, button_height, green, blue, play)
        button("Shop", width/2 - button_width/2, height/2 - button_height/2+140, button_width, button_height, green, blue, shop)
        button("Menu", width/2 - button_width/2, height/2 - button_height/2+240, button_width, button_height, green, blue, menu)
        button("Quit", width/2 - button_width/2, height/2 - button_height/2+340, button_width, button_height, green, blue, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()

if __name__ == "__main__":
    intro()
