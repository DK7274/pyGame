import pygame
import time
pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Hello Pygame Window")
screen.fill((0,0,0))

sprite1 = pygame.image.load("Images/amogus.png")

# main loop

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # command to actually quit the game by clicking the X button
            game_over = True
pygame.quit()