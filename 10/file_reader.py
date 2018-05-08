# file_path = '/Users/admin/Documents/Python_Crash_Course/10/text_files/pi_digits.txt'
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in linesC:
	print(line.rstrip())