import pygame
import time
import random


#Colours:
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255,255,0)
Aqua = (0, 255, 255)
Water = (48, 86, 191)
Pink = (255, 0, 255)
Lawn_Green = (124, 252, 0)
Sky_blue = (0,191,255)
Sandy_Brown = (244, 164, 96)

#to initialize the pygame module
pygame.init()

#background Image
background = pygame.image.load('evening_1.jpg')

# To start the screen at 600X800 resolution.
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Corona Strike 0.0.1")
icon = pygame.image.load('Code_Maniac.jpg')
pygame.display.set_icon(icon)

running = True

#To make it full screen - 
# pygame.display.toggle_fullscreen()

#Player - Protogonist
playerImg = pygame.image.load('spaceship48X48.png')
playerX = 400
playerY = 500
coor_player = (playerX, playerY)
player_movX = 0
player_movY = 0


def player(x, y):
	coor_player = (x, y)	
	screen.blit(playerImg, coor_player)

#Bullet - kill la kill
bulletImg = pygame.image.load('bullet_1.png')
bulletX = 0
bulletY = 0
# coor_bullet = (bulletX, bulletY)
bullet_movY = 0.1
bullet_state = False

def fire_bullet(x, y):
	# global bullet_state # bullet is currently fired. and you can see it	
	screen.blit(bulletImg, (x + 12, y + 5))

#level 1 corona-virus
corona_1_Img = pygame.image.load('corona_1.png')
corona_1X = random.randint(0, 752)
corona_1Y = random.randint(50, 150)
corona_movX = 0.5
corona_movY = 48

def corona_1(corona_1X, corona_1Y):	
	screen.blit(corona_1_Img, (corona_1X, corona_1Y))


#main game-loop
while running:

	# Background color
	screen.fill(Water)
	# Background Image
	screen.blit(background, (0, 0))
	

	player(playerX, playerY)
	corona_1(corona_1X, corona_1Y)
	#sleep(5)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# if keystroke is pressed check its left or right
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				player_movX = 1
				print("right")
			elif event.key == pygame.K_LEFT:
				player_movX = -1
				print("left")
			elif event.key == pygame.K_UP:
				player_movY = -1
				print("Up")
			elif event.key == pygame.K_DOWN:
				player_movY = 1
				print("Down")
			elif event.key == pygame.K_SPACE:
	  			print("Shoot.")
	  			bullet_state = True
	  			bulletX = playerX
	  			bulletY = playerY
	  			fire_bullet(bulletX, bulletY)
			elif event.key == pygame.K_ESCAPE:
	  			print("Escape key.")
			else:
				pass
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
	  			print("dhuddhud")
			elif event.key == pygame.K_ESCAPE:
				running = False
				print("Existing the Game.")
			elif event.key == pygame.K_RIGHT:
				player_movX = 0
				print("right")
			elif event.key == pygame.K_LEFT:
				player_movX = 0 
				print("left")
			elif event.key == pygame.K_UP:
				player_movY = 0
				print("Up")
			elif event.key == pygame.K_DOWN:
				player_movY = 0
				print("Down")
			else:
				pass
	# Boundary conditions : don't leave the screen player

		#for player
	if playerX <= 0:
		playerX = 0		
	elif playerX >= 752:
		playerX = 752
	if playerY <= 0:
		playerY = 0		
	elif playerY >= 552:
		playerY = 552
	playerX += player_movX
	playerY += player_movY

		#for Bullet
	if bullet_state == True:
		fire_bullet(bulletX, bulletY)
		bulletY -= bullet_movY

		#for corona_1
	if corona_1X <= 0:
		corona_1X = 0
		corona_movX = -corona_movX
		corona_1Y += corona_movY	
	elif corona_1X >= 752:
		corona_1X = 752
		corona_movX = -corona_movX
		corona_1Y += corona_movY
	if corona_1Y <= 0:
		corona_1Y = 0		
	elif corona_1Y >= 552:
		corona_1Y = 552
	corona_1X += corona_movX
	pygame.display.update()