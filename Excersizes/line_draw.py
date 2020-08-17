import pygame 
import time 
import math 
# Part-A initialtion 

pygame.init() 

# game constants 
display_width = 800 
display_height = 600 
## colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE = (0, 0, 255)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock() 


### text_objects 

def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect() 

def node_display(text, location):
    large_font = pygame.font.Font('freesansbold.ttf', 50)
    text_surf, text_rect = text_objects(" "+text+" ", large_font, BLACK)
    pygame.draw.rect(text_surf, BLUE, text_rect, 5)
    gameDisplay.blit(text_surf, location)

def arrow(screen, lcolor, tricolor, start, end, trirad = 10, thickness=5):
    rad = math.pi/180 
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    pygame.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(rotation),
                                        end[1] + trirad * math.cos(rotation)),
                                       (end[0] + trirad * math.sin(rotation - 120*rad),
                                        end[1] + trirad * math.cos(rotation - 120*rad)),
                                       (end[0] + trirad * math.sin(rotation + 120*rad),
                                        end[1] + trirad * math.cos(rotation + 120*rad))))

def main_loop():
    Exit = False
    while not Exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit = True

        gameDisplay.fill(WHITE)
        node_display("Hi", location = (100, 100))
        arrow(gameDisplay, RED, GREEN, (0,0), (80, 80))
        pygame.display.update()
        clock.tick(25)

main_loop()
pygame.quit()

