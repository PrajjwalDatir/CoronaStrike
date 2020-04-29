# my_enemy.py
import pygame
import time
import random
import math

class my_corona_1():
#level 1 corona-virus
	def __init__(self):
		self.corona_1_Img_right = pygame.image.load('corona_2.png')
		self.corona_1_Img_left = pygame.image.load('corona_1.png')
		self.corona_1_Img = []
		self.corona_1X = []
		self.corona_1Y = []
		self.corona_choice = [30, 78, 126, 174]
		self.corona_movX = [1]*5
		self.corona_movY = [48]*5
		self.corona_vel = 0.3
		
		def spawn_corona(self, i):
			# for i in range(5):
			self.corona_1_Img.append(self.corona_1_Img_right)
			again = True
			while again:
				self.corona_1X.append(random.randint(100, 600))
				self.corona_1Y.append(random.choice(self.corona_choice))
				if i == 0:
					break
				for j in range(0, 5):
					print("[", self.corona_1X, ",", self.corona_1Y)
					if (self.corona_1Y[i] == self.corona_1Y[j]) and (abs(self.corona_1X[i] - self.corona_1X[j]) < 96):
						again = True
						self.corona_1X.pop()
						self.corona_1Y.pop()
						break
					else:
						again = False
						break
		for i in range(5):
			spawn_corona(self, i)

	def corona_1(self, corona_1X, corona_1Y, screen):	
		for i in range(5):
			screen.blit(self.corona_1_Img[i], (int(corona_1X[i]), int(corona_1Y[i])))

	# Boundary conditions : don't leave the screen
	def check_corona_1(self, dt):
				#for corona_1
		for i in range(5):
			if self.corona_1X[i] <= 0:
				self.corona_1X[i] = 0
				self.corona_1_Img[i] = self.corona_1_Img_right
				self.corona_movX[i] = -self.corona_movX[i]
				self.corona_1Y[i] += self.corona_movY[i]	
			elif self.corona_1X[i] >= 752:
				self.corona_1X[i] = 752
				self.corona_1_Img[i] = self.corona_1_Img_left
				self.corona_movX[i] = -self.corona_movX[i]
				self.corona_1Y[i] += self.corona_movY[i]
			if self.corona_1Y[i] <= 0:
				self.corona_1Y[i] = 0		
			elif self.corona_1Y[i] >= 552:
				self.corona_1Y[i] = 552
			self.corona_1X[i] += self.corona_movX[i] * (dt * self.corona_vel)
