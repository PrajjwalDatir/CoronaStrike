# my_score.py
# score functions
import pygame
import time
import random
import math

class info_game():
	def __init__(self):
		self.score = 0
		self.font = pygame.font.Font('DoubleFeature20.ttf', 24)
		self.textX1 = 10
		self.textY1 = 10
		self.textX2 = 700
		self.textY2 = 10 
		
	def my_score(self, screen):
		blit_score = self.font.render("SCORE : " + str(self.score), True, (255, 255, 255))
		screen.blit(blit_score, (self.textX1, self.textY1))


	# FPS
	def my_fps(self, dt, screen):
		blit_fps = self.font.render("FPS : " + str(dt), True, (255, 255, 255))
		screen.blit(blit_fps, (self.textX2, self.textY2))

