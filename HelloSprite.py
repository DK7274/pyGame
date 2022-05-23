import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000,500),0,32)
pygame.display.set_caption("Hello Pygame Sprite")
screen.fill((0,0,0))

sprite1 = pygame.image.load("Images/chees.png")
sprite1 = pygame.transform.scale(sprite1,(1000,500))
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()

# main loop

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # command to actually quit the game by clicking the X button
            game_over = True
   # screen.blit(sprite1,(0,0)) #choose where the image will go
    screen.blit(sprite1,(screen.get_width()/2 - spriteWidth/2,screen.get_height()/2-spriteHeight/2))
    pygame.display.update()
pygame.quit()