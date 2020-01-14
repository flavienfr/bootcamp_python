from recipe import Recipe
import datetime

class Book:
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.datetime.now()
		self.creation_date = datetime.datetime.now()
		self.recipes_list = { "starter":[], 
							 "lunch":[],
							 "dessert":[]}

	def get_recipe_by_name(self, name):
		for key, value in self.recipes_list.items():
			for FindName in value:
				if FindName.name == name:
					print (FindName)
					return FindName

	def get_recipes_by_types(self, recipe_type):
		for key, value in self.recipes_list.items():
			if recipe_type == key:
				for i in range(0, len(self.recipes_list[recipe_type])):
					print(self.recipes_list[recipe_type][i])

	def add_recipe(self, recipe):
		if type(recipe) is Recipe:
			self.recipes_list[recipe.recipe_type].append(recipe)
			self.last_update = datetime.datetime.now()
		else:
			print('Not a Recipe object')
