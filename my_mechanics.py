# my_mechanics.py
import pygame
import time
import random
import math

class mechanics():
	# is collision
	def isCollision(self, enemyX, enemyY, bulletX, bulletY):
		distance = math.hypot(enemyX - bulletX, enemyY - bulletY)
		if distance < 48:
			return True
		return False