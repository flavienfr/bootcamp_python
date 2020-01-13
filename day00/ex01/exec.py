import sys

arg = len(sys.argv) - 1
while arg > 0:
	j = 1
	lenght = len(sys.argv[arg])
	while j <= lenght:
		char = sys.argv[arg][lenght - j]
		if char.isupper():
			print(char.lower(), end = '')
		elif char.islower():
			print(char.upper(), end = '')
		else:
			print(char, end = '')
		j += 1
	arg -= 1
	if arg > 0:
		print(' ', end = '')
print()
