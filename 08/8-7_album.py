# -*- coding:UTF-8 -*-

def make_album(artist, album_name, number=''):
	"""返回一个字典，其中包含有关专辑的信息"""
	album = {'artist': artist, 'album_name': album_name}
	if number:
		album['number'] = number
	return album

album = make_album('YGW', 'G3')
print(album)

album = make_album('chaozai', 'haunyaunkunshou', number=15)
print(album)

album = make_album('AC/DC', 'High way to hell', 16)
print(album)