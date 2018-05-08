# -*- coding:UTF-8 -*-

class Settings():
	"""存储《飞船移动》的所有设置的类"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		# self.bg_color = (230, 230, 230)
		self.bg_color = (0, 0, 0)

		# 飞船的设置
		self.ship_speed_factor = 5