# -*- coding:UTF-8 -*-

import sys

import pygame

def test_KEYDOWN():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption('12-4')
	bg_color = (0, 0, 0)
	while  True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					bg_color = (255, 105, 180)
				elif event.key == pygame.K_DOWN:
					bg_color = (65, 105, 225)
				elif event.key == pygame.K_RIGHT:
					bg_color = (152, 251, 152)
				elif event.key == pygame.K_LEFT:
					bg_color = (255, 160, 122)
		
		screen.fill(bg_color)
		pygame.display.flip()

test_KEYDOWN()