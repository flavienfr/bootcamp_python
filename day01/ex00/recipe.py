class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ''):
		try:
			if isinstance(name, str):
				self.name = name
			else:
				print('Bad name format')
				exit()
			if cooking_lvl in range (1, 6):
				self.cooking_lvl = cooking_lvl
			else:
				print('Bad cooking_lvl number')
				exit()
			if cooking_time > 0:
				self.cooking_time = cooking_time
			else:
				print('Bad cooking_time')
				exit()
			if all(isinstance(s, str) for s in ingredients):
				self.ingredients = ingredients
			else:
				print('Bad ingredients format')
				exit()
			if isinstance(description, str):
				self.description = description
			else:
				print('Bad description')
				exit()
			if any(recipe_type in s for s in ['starter','lunch','dessert']):
				self.recipe_type = recipe_type
			else:
				print('Bad recipe_type')
				exit()
		except ValueError:
			print('Bad argument')
			exit()
	def __str__(self):
		return "name: {}\ncooking_lvl: {}, cooking_time: {}, ingredients: {}, description: {}, recipe_type: {}\n".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)

