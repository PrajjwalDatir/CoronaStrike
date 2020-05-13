# level.py
import sys
import pygame
from my_colours import *

# introScreen.py
class select_level():
	def __init__(self):
		self.level = 0


	def level_loop(self, level):
		self.level = level 


	def game_exit(self):
		return False


	def level_intro(self, screen):
		intro = True
		background1 = pygame.image.load('Bat.png').convert()
		background2 = pygame.image.load('Bat.png').convert()
		background3 = pygame.image.load('Bat.png').convert()
		background4 = pygame.image.load('Bat.png').convert()
		while intro:
			screen.fill((0,0,0))
			screen.blit(background1, (0,50))
			screen.blit(background2, (500,50))
			screen.blit(background3, (0,350))
			screen.blit(background4, (500,350))
			my_mouse = pygame.mouse.get_pos() # in the form [x,y]
			font = pygame.font.Font('DoubleFeature20.ttf', 32)
			blit_level1 = font.render("level 1", True, (255, 255, 255))
			blit_level2 = font.render("level 2", True, (255, 255, 255))
			blit_level3 = font.render("level 3", True, (255, 255, 255))
			blit_level4 = font.render("level 4", True, (255, 255, 255))
			blit_arcade = font.render("Arcade mode", True, (255, 255, 255))
			pygame.mouse.set_visible(False)
			my_mouse = pygame.mouse.get_pos()
			
			if 225 < my_mouse[0] < 500:
				click = pygame.mouse.get_pressed()
				if 50 < my_mouse[1] < 125:
					if click[0] == 1:
						return 1
					pygame.draw.rect(screen, Red, (250,75,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,175,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,275,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,375,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,475,250,75))	
				elif 150 < my_mouse[1] < 225:
					if click[0] == 1:
						return 2
					pygame.draw.rect(screen, Dark_Red, (250,75,250,75))
					pygame.draw.rect(screen, Red, (250,175,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,275,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,375,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,475,250,75))
				
				elif 250 < my_mouse[1] < 325:
					if click[0] == 1:
						return 3
					pygame.draw.rect(screen, Dark_Red, (250,75,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,175,250,75))
					pygame.draw.rect(screen, Red, (250,275,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,375,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,475,250,75))
				elif 350 < my_mouse[1] < 425:
					if click[0] == 1:
						return 4
					pygame.draw.rect(screen, Dark_Red, (250,75,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,175,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,275,250,75))
					pygame.draw.rect(screen, Red, (250,375,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,475,250,75))
				elif 450 < my_mouse[1] < 525:
					if click[0] == 1:
						return 5
					pygame.draw.rect(screen, Dark_Red, (250,75,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,175,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,275,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,375,250,75))
					pygame.draw.rect(screen, Red, (250,475,250,75))
				else:
					pygame.draw.rect(screen, Dark_Red, (250,75,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,175,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,275,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,375,250,75))
					pygame.draw.rect(screen, Dark_Red, (250,475,250,75))
				
			
			else:
				pygame.draw.rect(screen, Dark_Red, (250,75,250,75))
				pygame.draw.rect(screen, Dark_Red, (250,175,250,75))
				pygame.draw.rect(screen, Dark_Red, (250,275,250,75))
				pygame.draw.rect(screen, Dark_Red, (250,375,250,75))
				pygame.draw.rect(screen, Dark_Red, (250,475,250,75))
			
			mouse_img = pygame.image.load('spaceship48X48.png')

			screen.blit(mouse_img, (my_mouse[0], my_mouse[1]))

			screen.blit(blit_level1, (275, 100))
			screen.blit(blit_level2, (275, 200))
			screen.blit(blit_level3, (275, 300))
			screen.blit(blit_level4, (275, 400))			
			screen.blit(blit_arcade, (275, 500))
			
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						intro = False
		return True

