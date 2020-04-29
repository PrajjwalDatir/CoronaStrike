# move.py
import pygame
import time
import random
import math

class movement():

	def move(self, p, b, dt):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
		# if keystroke is pressed check its left or right
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					p.player_movX = (dt * p.player_vel)
				elif event.key == pygame.K_LEFT:
					p.player_movX = -(dt * p.player_vel)
				# elif event.key == pygame.K_UP:
				# 	player_movY = -(dt * player_vel)
				# elif event.key == pygame.K_DOWN:
				# 	player_movY = (dt * player_vel)
				elif event.key == pygame.K_SPACE:
		  			if b.bullet_state == 'ready':
		  				b.bullet_sound = pygame.mixer.Sound('laser.wav')
		  				b.bullet_sound.play()
		  				b.bullet_state = 'fired'
		  				b.bulletX = p.playerX
		  				b.bulletY = p.playerY
		  				fire_bullet(bulletX, bulletY)
				elif event.key == pygame.K_ESCAPE:
		  			print("Escape key.")
				else:
					pass
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					pass
				elif event.key == pygame.K_ESCAPE:
					running = False
					print("Existing the Game.")
				elif event.key == pygame.K_RIGHT:
					p.player_movX = 0
				elif event.key == pygame.K_LEFT:
					p.player_movX = 0 
				# elif event.key == pygame.K_UP:
				# 	player_movY = 0
				# elif event.key == pygame.K_DOWN:
				# 	player_movY = 0
		return True