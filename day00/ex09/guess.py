import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!", end = '\n\n')
number = random.randrange(1, 100)
retry = 0
while 1:
	value = input("What's your guess between 1 and 99 ?")
	if value == 'exit':
		print("Goodbye!")
		break
	try:
		value = int(value)
	except ValueError:
		print("That's not a number.")
		continue
	if (value == 42):
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	if value > number:
		print("Too high!")
	elif value < number:
		print("Too low!")
	elif value == number:
		if retry == 0:
			print("Congratulations! You got it on your first try!")
		else:
			print("You won in", retry, "attempts!")
		break
	retry += 1