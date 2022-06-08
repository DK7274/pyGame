import pygame
pygame.init()
pygame.font.get_fonts() # import fonts
screen = pygame.display.set_mode((500,500),0,32) #set window size
pygame.display.set_caption("hello button") # set window caption
#set various colours
text_colour =(255,255,255)
button_colour = (156,6,6)
button_over_colour = (255,50,50)
#set button dimensions
button_width = 100
button_height: int = 50
#display button in the middle of the screen
button_rect = [(screen.get_width()-button_width)/2,
               (screen.get_height() - button_height)/2,
               button_width,button_height]
# set button font and button text
button_font = pygame.font.SysFont("Comic Sans MS",20)
button_text = button_font.render("QUIT",True,text_colour)

screen.fill((100,100,100))

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True #quit if window X button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if (button_rect[0] <= x <= button_rect[0] + button_rect[2] and button_rect[1] <= y <= button_rect[1] + button_rect[3]):
                game_over = True #quit game if quit button is clicked
    pygame.draw.rect(screen,button_colour,button_rect)
    # put da button in da centre
    screen.blit(button_text,(button_rect[0]+(button_width - button_text.get_width())/2,button_rect[1] + (button_height/2-button_text.get_height()/2)))

    pygame.display.update()
pygame.quit()