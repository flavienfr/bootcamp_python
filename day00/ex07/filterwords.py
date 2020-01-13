import string
import sys

def print_error():
	print("ERROR")
def remove_word(txt, nb):
	new_lst = []
	for c in string.punctuation:
		txt = txt.replace(c, '')
	lst = txt.split(' ')
	for s in lst:
		if len(s) > nb:
			new_lst.append(s)
	print(new_lst)

if len(sys.argv) == 3 and not sys.argv[1].isdigit():
	try:
		remove_word(sys.argv[1], int(sys.argv[2]))
	except:
		print_error()
else:
	print_error()

