class CoffeMachine():
  def __init__(self, model, recipes):
    self.__state = False
    self.__model = model
    self.__recipes = recipes

  def updateRecipePrice(self):
    for recipe in self.__recipes:
      recipe.calculate_price()
      print(recipe.get_price())

  def get_recipes(self):
    return self.__recipes

  def get_model(self):
    return self.__model

  def get_state(self):
    return self.__state

  def add_recipe(self, recipe):
    self.recipes.append(recipe)

  def print_recipe(self, recipePlace:int):
    ingredients = self.__recipes[recipePlace].get_ingredients()
    quantities = self.__recipes[recipePlace].get_quantities()
    for i in range(len(ingredients)):
      print("x" + str(quantities[i]) + " " + ingredients[i].get_name())