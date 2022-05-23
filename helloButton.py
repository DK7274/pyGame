import pygame
pygame.init()
pygame.font.get_fonts()
screen = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption("hello button")

text_colour =(255,255,255)
button_colour = (156,6,6)
button_over_colour = (255,50,50)
button_width = 100
button_height: int = 50
screenWidth = screen.get_width()
screenHeight = screen.get_height()

button_rect = [(screenWidth-button_width)/2,
               (screenHeight - button_height)/2,
               button_width,button_height]
button_font = pygame.font.SysFont("Comic Sans MS",20)
button_text = button_font.render("QUIT",True,text_colour)
screen.fill((100,100,100))

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True
    pygame.draw.rect(screen,button_colour,button_rect)
    screen.blit(button_text,(button_rect[0],button_rect[1]))

    pygame.display.update()
pygame.quit()