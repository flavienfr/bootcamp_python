from book import Book
from recipe import Recipe

tourte = Recipe('Le fufu', 3, 60, ['lol','poivre'], 'dessert')
pomme = Recipe('bleu', 2, 25, ['frite','sel'], 'dessert')
nutela = Recipe('nutela', 4, 10, ['chocolat','huile'], 'dessert')
livre = Book('livre_1')
#to_print = str(tourte)
#print(to_print)
Book.add_recipe(livre, pomme)
Book.add_recipe(livre, nutela)
Book.add_recipe(livre, tourte)

#Book.get_recipes_by_types(livre, 'dessert')
Book.get_recipe_by_name(livre, 'nutela')