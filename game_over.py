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
		self.over_text = self.over_font.render("G", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.2)
		self.over_text = self.over_font.render("GA", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.2)
		self.over_text = self.over_font.render("GAM", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.2)
		self.over_text = self.over_font.render("GAME", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.2)
		self.over_text = self.over_font.render("GAME O", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.2)
		self.over_text = self.over_font.render("GAME OV", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.2)
		self.over_text = self.over_font.render("GAME OVE", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.2)
		self.over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.2)
	
	def win_game(self, screen):
		self.over_text = self.over_font.render("Y", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.3)
		self.over_text = self.over_font.render("YO", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.3)
		self.over_text = self.over_font.render("YOU", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.3)
		self.over_text = self.over_font.render("YOU W", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.3)
		self.over_text = self.over_font.render("YOU WI", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.2)
		self.over_text = self.over_font.render("YOU WIN", True, (255, 255, 255))
		screen.blit(self.over_text, (100, 300))
		pygame.display.update()
		time.sleep(0.3)
		

