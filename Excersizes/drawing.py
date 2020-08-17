import pygame 
import time 

# Part-A initialtion 

pygame.init() 

# game constants 
display_width = 800 
display_height = 600 
## colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green  = (0, 255, 0)
blue = (0, 0, 255)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock() 


### game objects 

carImage = pygame.image.load('racecar.png')
def car(x, y): 
	gameDisplay.blit(carImage, (x, y))

def text_objects(text, font, color):
	text_surface = font.render(text, True, color)
	return text_surface, text_surface.get_rect() 

def message_display(text):
	large_font = pygame.font.Font('freesansbold.ttf', 50)
	text_surf, text_rect = text_objects(text, large_font, black)
	text_rect.center = ((display_width//2), (display_height//2))
	gameDisplay.blit(text_surf, text_rect)
	pygame.display.update()
	time.sleep(1)

# Part-c game loop 

def game_loop():
	## Game constants 
	gameExit = False
	car_x = display_width*0.45  
	car_y = display_height*0.8 
	delta_car_x = 0 
	delta_car_y = 0 

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					delta_car_x = -5
				if event.key == pygame.K_RIGHT:
					delta_car_x = 5
				if event.key == pygame.K_UP: 
					delta_car_y = -5 
				if event.key == pygame.K_DOWN:
					delta_car_y = 5 
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					delta_car_x = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					delta_car_y = 0 

		gameDisplay.fill(white)
		car_x += delta_car_x
		car_y += delta_car_y 

		if car_x > display_width - 65:
			car_x = display_width - 65
			gameDisplay.fill(red)
			message_display("you bumbed the wall")
		if car_x <0:
			car_x = 0
			gameDisplay.fill(red)
			message_display("you bumbed the wall")
		if car_y > display_height - 75:
			car_y = display_height  - 75
			gameDisplay.fill(red)
			message_display("you bumbed the wall")
		if car_y < 0:
			car_y = 0
			gameDisplay.fill(red)
			message_display("you bumbed the wall")

		
		car(car_x, y = car_y) 
		pygame.display.update()
		clock.tick(25)

game_loop()
pygame.quit()

