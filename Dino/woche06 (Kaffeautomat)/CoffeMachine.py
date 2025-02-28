from Recipe import Recipe

class CoffeMachine():
  def __init__(self, model:str, recipes:list[Recipe]): 
    self.__state:bool = False
    self.__model:str = model
    self.__recipes:list[Recipe] = recipes

  def get_recipes(self) -> list:
    return self.__recipes

  def get_model(self) -> str:
    return self.__model

  def get_state(self) -> bool:
    return self.__state

  def add_recipe(self, recipe:Recipe) -> None:
    self.__recipes.append(recipe)

  def print_recipe(self, index:int) -> None:
    ingredients = self.__recipes[index].get_ingredients()
    for ingredient, quantity in ingredients.items():
      print("x" + str(quantity) + " " + ingredient.get_name())