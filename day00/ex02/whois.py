import sys

def who_is(nb):
	if nb == 0:
		print("I'm Zero.")
	elif nb % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

if len(sys.argv) == 2:
	try:	
		who_is(int(sys.argv[1]))
	except ValueError:
		print("ERROR")
