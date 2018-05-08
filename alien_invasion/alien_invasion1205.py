# -*- coding:UTF-8 -*-

import pygame

from pygame.sprite import Group
from settings1205 import Settings
from ship1205 import Ship
import game_functions1205 as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建一艘飞船
	ship = Ship(ai_settings, screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()

	# 开始游戏的主循环 
	while True:

		# 监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, ship, bullets)
		# 更新飞船位置
		ship.update()
		# 更新所有未消失的子弹的位置
		gf.update_bullets(bullets)
		# 每次循环时都重绘屏幕
		# 让最近绘制的屏幕可见
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()