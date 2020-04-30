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
			screen.blit(self.bulletImg, (x, y))

	# Boundary conditions : don't leave the screen
	def check_bullet(self, bullet_state, bulletX, bulletY, screen, dt):
		#for Bullet
		if bullet_state == 'fired':
			bulletY -= (dt * self.bullet_vel)
			self.fire_bullet(bullet_state, bulletX, bulletY, screen)
		self.bulletY = bulletY

	def shoot(self, p, screen):
		bullet_sound = pygame.mixer.Sound('laser.wav')
		bullet_sound.play()
		self.bullet_state = 'fired'
		self.bulletX = p.playerX
		self.bulletY = p.playerY
		# self.fire_bullet(b.bullet_state, b.bulletX, b.bulletY, screen)
		screen.blit(self.bulletImg, (int(self.bulletX + 10), int(self.bulletY - 15)))
