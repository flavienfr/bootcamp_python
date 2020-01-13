import sys

def error_ex():
	print("Usage: python operations.py")
	print("Example:")
	print("    python operations.py 10 3")


def opp(nb1, nb2):
	print("Sum		:", nb1 + nb2)
	print("Difference	:", nb1 - nb2)
	print("Product		:", nb1 * nb2)
	try:
		print("Quotient	:", nb1 / nb2)
	except:
		print("Quotient	: ERROR (div by zero)")	
	try:
		print("Remainder	:", nb1 % nb2)
	except:
		print("Remainder	: ERROR (modulo by zero)")	

lenght = len(sys.argv)
if lenght < 3:
	error_ex()
elif lenght > 3:
	print("InputError: too many arguments", end = '\n\n')
	error_ex()
else:
	try:
		opp(int(sys.argv[1]), int(sys.argv[2]))
	except ValueError:
		print("InputError: only numbers", end = "\n\n")
		error_ex()

