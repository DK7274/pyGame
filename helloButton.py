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

button_rect = [(screen.get_width()-button_width)/2,
               (screen.get_height() - button_height)/2,
               button_width,button_height]
button_font = pygame.font.SysFont("Comic Sans MS",20)
button_text = button_font.render("QUIT",True,text_colour)
screen.fill((100,100,100))

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            
    pygame.draw.rect(screen,button_colour,button_rect)
    # put da button in da centre
    screen.blit(button_text,(button_rect[0]+(button_width - button_text.get_width())/2,button_rect[1] + (button_height/2-button_text.get_height()/2)))

    pygame.display.update()
pygame.quit()