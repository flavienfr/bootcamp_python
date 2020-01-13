cookbook = {'sandwich': {'ingredients': ["ham", "bread", "cheese", "tomatoes"], 'meal': 'lunch', 'prep_time': 10},
			'cake': {'ingredients': ["flour", "sugar", "eggs"], 'meal': 'dessert', 'prep_time': 60},
			'salad': {'ingredients': ["avocado", "arugula", "tomatoes", "spinach"], 'meal': 'lunch', 'prep_time': 15}
			}

def print_ckbk():
	print(cookbook)

def print_recipe():
	name = input("name :")
	try:
		print("Recipe for ", name, ":", sep = '')
		print("Ingredients list:", cookbook[name]['ingredients'])
		print("To be eaten for ", cookbook[name]['meal'], ".", sep = '')
		print("Takes", cookbook[name]['prep_time'], "minutes of cooking.")

	except:
		print("No recipe named", name)

def add_recipe():
	name = input('name :')
	lst = input('ingredients ([\'1\',\'2\']):')
	meal = input('meal :')
	time = input('prep_time :')
	cookbook[name] = {}
	cookbook[name]['ingredients'] = lst
	cookbook[name]['meal'] = meal
	cookbook[name]['prep_time'] = time

def	dell_recipe():
	name = input("name :")
	try:
		del cookbook[name]
	except:
		print("No recipe named", name)

def option():
	print("Please select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

while 1:
	option()
	choice = input()
	print('')
	if choice == '1':
		add_recipe()
	elif choice == '2':
		dell_recipe()
	elif choice == '3':
		print_recipe()
	elif choice == '4':
		print_ckbk()
	elif choice == '5':
		break
	else:
		print("This option does not exist, please type the corresponding number.")
		print("To exit, enter 5.")
	print('')
