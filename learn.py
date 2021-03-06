import pygame
import time
import random
import math


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

My_colours = [Sandy_Brown, Sky_blue, Lawn_Green, Black, White, Red, Green, Blue, Yellow, Aqua, Water, Pink]

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

# number of enemies in level 1


running = True
# pygame.mixer.music.load('background.wav')
# pygame.mixer.music.play(-1)

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 96)

# score functions
score = 0
font = pygame.font.Font('DoubleFeature20.ttf', 24)

#To make 	it full screen - 
#pygame.display.toggle_fullscreen()

#Player - Protogonist
playerImg = pygame.image.load('spaceship48X48.png')
playerX = 400
playerY = 500
coor_player = (playerX, playerY)
player_movX = 0
player_movY = 0
player_vel = 0.5

#Bullet - kill la kill
bulletImg = pygame.image.load('bullet_1.png')
bulletX = 0
bulletY = 0
# bullet_movY = 5
bullet_state = 'ready'
bullet_vel = 1

#level 1 corona-virus
corona_1_Img = []
corona_1X = []
corona_1Y = []
corona_choice = [30, 78, 126, 174]
for i in range(5):
	corona_1_Img.append(pygame.image.load('corona_1.png'))
	again = True
	while again:
		corona_1X.append(random.randint(100, 600))
		corona_1Y.append(random.choice(corona_choice))
		if i == 0:
			break
		for j in range(0, i):
			print("[", corona_1X, ",", corona_1Y)
			distance = math.hypot(corona_1X[i] - corona_1X[j], corona_1Y[i] - corona_1Y[j])
			if distance < 60:
				again = True
				corona_1X.pop()
				corona_1Y.pop()
				break
			else:
				again = False
				break

corona_movX = [1]*5
corona_movY = [48]*5
corona_vel = 0.3

def my_score():
	textX = 10
	textY = 10
	blit_score = font.render("SCORE : " + str(score), True, (255, 255, 255))
	screen.blit(blit_score, (textX, textY))


def game_over_text():

    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (100, 300))


def player(x, y):	
	screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
	global bullet_state # bullet is currently fired. and you can see it	
	if bullet_state == 'fired':
		screen.blit(bulletImg, (x + 10, y - 15))


def corona_1(corona_1X, corona_1Y):	
	for i in range(5):
		screen.blit(corona_1_Img[i], (int(corona_1X[i]), int(corona_1Y[i])))


def isCollision(enemyX, enemyY, bulletX, bulletY):
	distance = math.hypot(enemyX - bulletX, enemyY - bulletY)
	if distance < 30:
		return True
	return False

# FPS
def my_fps(dt):
	textX = 700
	textY = 10 
	blit_fps = font.render("FPS : " + str(dt), True, (255, 255, 255))
	screen.blit(blit_fps, (textX, textY))

	
clock = pygame.time.Clock()
#main game-loop
while running:
	dt = clock.tick(30)
	# Background color
	screen.fill((0,0,0))
	# Background Image
	screen.blit(background, (0, 0))
	player(playerX, playerY)
	corona_1(corona_1X, corona_1Y)
	#sleep(5)
	my_score()
	my_fps(dt)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# if keystroke is pressed check its left or right
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				player_movX = (dt * player_vel)
			elif event.key == pygame.K_LEFT:
				player_movX = -(dt * player_vel)
			# elif event.key == pygame.K_UP:
			# 	player_movY = -(dt * player_vel)
			# elif event.key == pygame.K_DOWN:
			# 	player_movY = (dt * player_vel)
			elif event.key == pygame.K_SPACE:
	  			if bullet_state == 'ready':
	  				bullet_sound = pygame.mixer.Sound('laser.wav')
	  				bullet_sound.play()
	  				bullet_state = 'fired'
	  				bulletX = playerX
	  				bulletY = playerY
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
				player_movX = 0
			elif event.key == pygame.K_LEFT:
				player_movX = 0 
			# elif event.key == pygame.K_UP:
			# 	player_movY = 0
			# elif event.key == pygame.K_DOWN:
			# 	player_movY = 0
			

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
	if bullet_state == 'fired':
		fire_bullet(bulletX, bulletY)
		bulletY -= (dt * bullet_vel)
	if bulletY <= 0:
		bullet_state = 'ready'
	
		# collision
	for i in range(5):
		for j in range(i + 1, 5):
			if isCollision(corona_1X[i], corona_1Y[i], corona_1X[j], corona_1Y[j]):		
				corona_movX[i] = -corona_movX[i]
				corona_movX[j] = -corona_movX[j]

		if isCollision(corona_1X[i], corona_1Y[i], bulletX, bulletY):
			explosion_sound = pygame.mixer.Sound('explosion.wav')
			explosion_sound.play()
			bullet_state = 'ready'
			bulletY = 800
			score += 1
			corona_1X[i] = random.randint(100, 600)
			corona_1Y[i] = random.choice(corona_choice)
			print(score)

		if isCollision(corona_1X[i], corona_1Y[i], playerX, playerY):
			running = False

		#for corona_1
	for i in range(5):
		if corona_1X[i] <= 0:
			corona_1X[i] = 0
			corona_movX[i] = -corona_movX[i]
			corona_1Y[i] += corona_movY[i]	
		elif corona_1X[i] >= 752:
			corona_1X[i] = 752
			corona_movX[i] = -corona_movX[i]
			corona_1Y[i] += corona_movY[i]
		if corona_1Y[i] <= 0:
			corona_1Y[i] = 0		
		elif corona_1Y[i] >= 552:
			corona_1Y[i] = 552
		corona_1X[i] += corona_movX[i] * (dt * corona_vel)
		
	if running == False:
		game_over_text()
	pygame.display.update()
	
time.sleep(0.5)
