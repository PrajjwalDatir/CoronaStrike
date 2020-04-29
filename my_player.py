import pygame
import time
import random
import math

class my_player():
#Player - Protogonist
	def __init__(self):
		self.playerImg = pygame.image.load('spaceship48X48.png')
		self.playerX = 400
		self.playerY = 500
		#self.coor_player = (playerX, playerY)
		self.player_movX = 0
		self.player_movY = 0
		self.player_vel = 0.4

	def player(self, playerX, playerY, screen):
		screen.blit(self.playerImg, (int(playerX), int(playerY)))

	# Boundary conditions : don't leave the screen
	def check_playerX(self, playerX, player_movX):
			#for player
		if playerX < 0:
			self.playerX = 0
			return 0
		elif playerX > 752:
			self.playerX = 752
			return 750
		self.playerX += player_movX

	def check_playerY(self,  playerY):
		if playerY < 0:
			self.playerY = 0		
		elif playerY > 552:
			self.playerY = 552
