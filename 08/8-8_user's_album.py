# -*- coding:UTF-8 -*-

def make_album(artist, album_name, number=''):
	"""返回一个字典，其中包含有关专辑的信息"""
	album = {'artist': artist, 'album_name': album_name}
	if number:
		album['number'] = number
	return album

while True:
	print("\nPlease tell me the album info:")
	print("Enter \'q\' to exit.")
	artist = input("The artist: ")
	if artist == 'q':
		break

	album_name = input("The album: ")
	if album_name == 'q':
		break

	number = input("Total number: ")
	if number == 'q':
		break

	album = make_album(artist, album_name, number)
	print("\nYour album info: " + str(album) + "!")