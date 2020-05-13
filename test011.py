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
from my_movement import *
from introScreen import *
import sys
from level import *
from my_boss import *
# import pygame.sprite as sprite

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

# pygame.mixer.music.load('background.wav')
# pygame.mixer.music.play(-1)

starting = start_game()
run = starting.game_intro(screen)
if run == False:
	sys.exit()

# need level selecting page
my_level = select_level()
mode = my_level.level_intro(screen)
print("your mode is ", mode)
#main game-loop

running = True

p = my_player()
c = my_corona_1(mode)
for i in range(5):
	c.spawn_corona(i)

g = game_over()
b = my_bullet()
s = info_game()
m = mechanics()
key = movement()
clock = pygame.time.Clock()
#rb = red_boss()

hit = 0
while running:
	dt = clock.tick_busy_loop(30)
	# Background color
	screen.fill((0,0,0))
	# Background Image
	screen.blit(background, (0,0))
	p.player(p.playerX, p.playerY, screen)
	c.corona_1(c.corona_1X, c.corona_1Y, screen)
	# rb.boss_draw(screen)
	s.my_score(screen)
	s.my_fps(dt, screen)

	running = key.move(p, b, dt, screen)

	# checking game finish
	dead = 0

	for i in range(5):		
		if not c.alive[i]:
				dead += 1
				continue
		for j in range(i + 1, 5):
			if not c.alive[j]:
				continue
			elif c.corona_1Y[i] == c.corona_1Y[j]:
				if abs(c.corona_1X[i] - c.corona_1X[j]) < 48:
				# if m.isCollision(c.corona_1X[i], 
				# 				c.corona_1Y[i], 
				# 				c.corona_1X[j], 
				# 				c.corona_1Y[j]
				# 				): 
					c.corona_movX[i] = -c.corona_movX[i]
					c.corona_movX[j] = -c.corona_movX[j]
					if c.corona_movX[i] > 0:
						c.corona_1X[j] -= (48 - abs(c.corona_1X[i] - c.corona_1X[j]))/2
						c.corona_1X[i] += (48 - abs(c.corona_1X[i] - c.corona_1X[j]))/2
						c.corona_1_Img[j] = c.corona_1_Img_left
						c.corona_1_Img[i] = c.corona_1_Img_right
					else:
						c.corona_1X[j] += (48 - abs(c.corona_1X[i] - c.corona_1X[j]))/2
						c.corona_1X[i] -= (48 - abs(c.corona_1X[i] - c.corona_1X[j]))/2
						c.corona_1_Img[j] = c.corona_1_Img_right 
						c.corona_1_Img[i] = c.corona_1_Img_left
						
		if m.isCollision(c.corona_1X[i], c.corona_1Y[i], b.bulletX, b.bulletY):
			explosion_sound = pygame.mixer.Sound('explosion.wav')
			explosion_sound.play()
			b.bullet_state = 'ready'
			b.bulletY = 800
			if mode == 5:
				c.spawn_corona(i)
			else:
				c.health[i] -= 1
				if c.health[i] == 0: 
					c.alive[i] = False
					s.score += 1
			if c.corona_movX[i] < 0:
				c.corona_1_Img[i] = c.corona_1_Img_left
			print(s.score)
		if m.isCollision(c.corona_1X[i], c.corona_1Y[i], p.playerX, p.playerY):
			running = False
				
	if dead == 5:
		running = False
	c.check_corona_1(dt)

	# boss collision
	#distance_boss = math.hypot(rb.bossX - b.bulletX, rb.bossY - b.bulletY)
	#if rb.health == 3:
	#	if distance_boss < 120:
	#		hit = 1
	# elif rb.health == 2:
	# 	if distance_boss < 90:
	# 		hit = 1
	# elif rb.health == 1:
	# 	if distance_boss < 75:
	# 		hit = 1
	# if hit == 1:
	# 	b.bullet_state = 'ready'
	# 	b.bulletY = 800
	# 	rb.health -= 1
	# 	explosion_sound = pygame.mixer.Sound('explosion.wav')
	# 	explosion_sound.play()
	# 	hit = 0

	# if rb.health <= 0:
	# 	explosion_sound = pygame.mixer.Sound('explosion.wav')
	# 	explosion_sound.play()
	# 	running = False
	
	b.check_bullet(b.bullet_state, b.bulletX, b.bulletY, screen, dt)
	p.check_playerX(p.playerX, p.player_movX)
	p.check_playerY(p.playerY)
	
	if b.bulletY <= 0:
		b.bullet_state = 'ready'

	if running == False:
		g.game_over_text(screen)
		pygame.display.update()
		#time.sleep(2)

	pygame.display.update()
