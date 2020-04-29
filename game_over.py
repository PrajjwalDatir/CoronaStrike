#game_over.py
# Game Over
import pygame
import time
import random
import math

class game_over():
	def __init__(self):
		self.over_font = pygame.font.Font('freesansbold.ttf', 96)

	def game_over_text(self, screen):
	    self.over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
	    screen.blit(self.over_text, (100, 300))
