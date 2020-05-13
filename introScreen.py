import pygame
from my_colours import *

# introScreen.py
class start_game():
	def __init__(self):
		self.intro = True


	def game_loop(self):
		self.intro = False


	def game_exit(self):
		return False


	def game_intro(self, screen):
		# self.intro = True
		background = pygame.image.load('banner2.jpg').convert()
		while self.intro:
			screen.fill((0,0,0))
			#background Image
			screen.blit(background, (0,0))
			my_mouse = pygame.mouse.get_pos() # in the form [x,y]
			font = pygame.font.Font('DoubleFeature20.ttf', 32)
			blit_score = font.render("start the game :)", True, (0, 0, 0))
			blit_score2 = font.render("Quit :(", True, (0, 0, 0))
			pygame.mouse.set_visible(False)
			# pygame.mouse.set_cursor((16, 16), (7, 7), (0, 0, 1, 0, 3, 128, 7, 192, 14, 224, 28, 112, 56, 56, 112, 
			# 						28, 56, 56, 28, 112, 14, 224, 7, 192, 3, 128, 1, 0, 0, 0, 0, 0), 
			# 						(1, 0, 3, 128, 7, 192, 15, 224, 31, 240, 62, 248, 124, 124, 248, 62, 124, 124, 
			# 						62, 248, 31, 240, 15, 224, 7, 192, 3, 128, 1, 0, 0, 0))
			# print(my_mouse)
			if 160 < my_mouse[0] < 550:
				click = pygame.mouse.get_pressed()
				if 160 < my_mouse[1] < 315:
					if click[0] == 1:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								return False
							if event.type == pygame.MOUSEBUTTONUP:
								print("start the game")
								self.game_loop()
					pygame.draw.rect(screen, Green, (200,200,350,125))
					pygame.draw.rect(screen, Dark_Red, (200,400,350,125))
				elif 360 < my_mouse[1] < 515:
					if click[0] == 1:
						print("Quit the Game")
						return self.game_exit()
					pygame.draw.rect(screen, Red, (200,400,350,125))
					pygame.draw.rect(screen, Dark_Green, (200,200,350,125))
				else:
					pygame.draw.rect(screen, Dark_Green, (200,200,350,125))
					pygame.draw.rect(screen, Dark_Red, (200,400,350,125))
			else:
				pygame.draw.rect(screen, Dark_Green, (200,200,350,125))
				pygame.draw.rect(screen, Dark_Red, (200,400,350,125))
			
			screen.blit(blit_score, (225, 250))
			screen.blit(blit_score2, (275, 450))
			mouse_img = pygame.image.load('spaceship48X48.png')
			screen.blit(mouse_img, (my_mouse[0], my_mouse[1]))
			
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.intro = False
		return True

