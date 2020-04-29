#my_bullet.py
import pygame
import time
import random
import math


class my_bullet():
	def __init__(self):
		#Bullet - kill la kill
		self.bulletImg = pygame.image.load('bullet_1.png')
		self.bulletX = 0
		self.bulletY = 0
		# bullet_movY = 5
		self.bullet_state = 'ready'
		self.bullet_vel = 1

	def fire_bullet(self, bullet_state, x, y, screen):
		# bullet is currently fired. and you can see it	
		if bullet_state == 'fired':
			screen.blit(self.bulletImg, (int(x + 10), int(y - 15)))

	# Boundary conditions : don't leave the screen
	def check_bullet(self, bullet_state, bulletX, bulletY, screen, dt):
		#for Bullet
		if bullet_state == 'fired':
			bulletY -= (dt * self.bullet_vel)
			self.fire_bullet(bullet_state, bulletX, bulletY, screen)
		self.bulletY = bulletY
