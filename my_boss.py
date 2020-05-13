#my_boss.py
import pygame
from my_player import *


class red_boss():
	def __init__(self):
		self.bossIMG = pygame.image.load('Corona_boss1_75x75.png')
		self.bossIMG2 = pygame.image.load('Corona_boss1_90x90.png')
		self.bossIMG3 = pygame.image.load('Corona_boss1_120x120.png')
		self.bossX = 400
		self.bossY = 130
		self.boss_movX = 0
		self.boss_movY = 0
		self.boss_vel = 0.4
		self.health = 3

	def boss_draw(self, screen):
		if self.health == 1:
			screen.blit(self.bossIMG, (int(self.bossX), int(self.bossY)))
		elif self.health == 2:
			screen.blit(self.bossIMG2, (int(self.bossX), int(self.bossY)))
		elif self.health == 3:
			screen.blit(self.bossIMG3, (int(self.bossX), int(self.bossY)))


	def check_bossX(self, bossX, boss_movX):
			#for boss
		if bossX < 0:
			self.bossX = 0
			return 0
		elif bossX > 752:
			self.bossX = 752
			return 750
		self.bossX += boss_movX

	def check_bossY(self,  bossY):
		if bossY < 0:
			self.bossY = 0		
		elif bossY > 552:
			self.bossY = 552
	
#	def home_missile(self, p, screen):
#		self.

