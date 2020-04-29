# test011.py
import pygame
import time
import random
import math
from my_colours import *
from game_over import *
from my_player import *
from my_enemy import *
from my_score import *
from my_mechanics import *
from my_bullet import *
# from my_movement import *

#to initialize the pygame module
pygame.init()

# To start the screen at 600X800 resolution.
screen = pygame.display.set_mode((800, 600))

#background Image
background = pygame.image.load('evening_1.jpg').convert()

#Title and Icon
pygame.display.set_caption("Corona Strike 0.0.1")
icon = pygame.image.load('Code_Maniac.jpg')
pygame.display.set_icon(icon)

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

#main game-loop
running = True
p = my_player()
c = my_corona_1()
g = game_over()
b = my_bullet()
s = info_game()
m = mechanics()
# key = movement()
clock = pygame.time.Clock()
while running:
	dt = clock.tick_busy_loop(30)
	# Background color
	screen.fill((0,0,0))
	# Background Image
	screen.blit(background, (0, 0))
	p.player(p.playerX, p.playerY, screen)
	c.corona_1(c.corona_1X, c.corona_1Y, screen)
	s.my_score(screen)
	s.my_fps(dt, screen)
	# running = key.move(p, b, dt)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# if keystroke is pressed check its left or right
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				p.player_movX = (dt * p.player_vel)
				print("right")
			elif event.key == pygame.K_LEFT:
				print("left")
				p.player_movX = -(dt * p.player_vel)
			elif event.key == pygame.K_SPACE:
	  			if b.bullet_state == 'ready':
	  				b.bullet_sound = pygame.mixer.Sound('laser.wav')
	  				b.bullet_sound.play()
	  				b.bullet_state = 'fired'
	  				b.bulletX = p.playerX
	  				b.bulletY = p.playerY
	  				b.fire_bullet(b.bullet_state, b.bulletX, b.bulletY, screen)
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

			# collision
	for i in range(5):		
		for j in range(i + 1, 5):
			if c.corona_1Y[i] == c.corona_1Y[j]:
				if abs(c.corona_1X[i] - c.corona_1X[j]) < 48:
				# if m.isCollision(c.corona_1X[i], 
				# 				c.corona_1Y[i], 
				# 				c.corona_1X[j], 
				# 				c.corona_1Y[j]
				# 				): 
					c.corona_movX[i] = -c.corona_movX[i]
					c.corona_movX[j] = -c.corona_movX[j]
					if c.corona_1_Img[j] == c.corona_1_Img_right:
						c.corona_1X[j] -= 4
						c.corona_1X[i] += 4
						c.corona_1_Img[j] = c.corona_1_Img_left
						c.corona_1_Img[i] = c.corona_1_Img_right
					else:
						c.corona_1X[j] += 4
						c.corona_1X[i] -= 4
						c.corona_1_Img[j] = c.corona_1_Img_right 
						c.corona_1_Img[i] = c.corona_1_Img_left

		if m.isCollision(c.corona_1X[i], c.corona_1Y[i], b.bulletX, b.bulletY):
			explosion_sound = pygame.mixer.Sound('explosion.wav')
			explosion_sound.play()
			b.bullet_state = 'ready'
			b.bulletY = 800
			s.score += 1
			again = True
			while again:
				c.corona_1X[i] = random.randint(100, 600)
				c.corona_1Y[i] = random.choice(c.corona_choice)
				for j in range(0, 5):
					if i == j:
						continue
					if (c.corona_1Y[i] == c.corona_1Y[j]) and abs((c.corona_1X[i] - c.corona_1X[j]) < 48):
						again = True
						break
					else:
						again = False
						break
		
			#c.corona_1X[i] = random.randint(100, 600)
			#c.corona_1Y[i] = random.choice(c.corona_choice)
			print(s.score)

		if m.isCollision(c.corona_1X[i], c.corona_1Y[i], p.playerX, p.playerY):
			running = False
	c.check_corona_1(dt)
	
	b.check_bullet(b.bullet_state, b.bulletX, b.bulletY, screen, dt)
	p.check_playerX(p.playerX, p.player_movX)
	p.check_playerY(p.playerY)
	
	if b.bulletY <= 0:
		b.bullet_state = 'ready'
		
	if running == False:
		g.game_over_text(screen)
	pygame.display.update()
	