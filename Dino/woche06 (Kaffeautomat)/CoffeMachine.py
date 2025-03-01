from Recipe import Recipe
from Ingredient import Ingredient

class CoffeMachine():
  __options:tuple = ("Get a Coffe", "Show Recipe for a Coffe", "Show all Recipies")

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

  def toggleOnOff(self) -> bool:
    """Returns the state after the toggle event"""
    greeting:str = "Welcome Master"
    width:int = len(greeting) + 2
    if self.__state == True:
      self.__state = False
    else:
      self.__state = True
      print("-" * width)
      print(f"{greeting:^{width}}")
      print("-" * width)
      print("\nWhat would you like me to do?")
      self.printOptions()
    return self.__state

  def printOptions(self) -> None:
    for i in range(len(self.__options)):
      print(f"{i + 1}. " + self.__options[i])

  def add_recipe(self, recipe:Recipe) -> None:
    self.__recipes.append(recipe)

  def print_recipe(self, index:int) -> None:
    ingredients:dict[Ingredient, int] = self.__recipes[index].get_ingredients()
    print(f"{index + 1}. " + self.__recipes[index].get_name() + ": ")
    for ingredient, quantity in ingredients.items():
      print(f"{'x':>5}" + str(quantity) + " " + ingredient.get_name())
    print()

  def printAllRecipes_detailed(self) -> None:
    for i in range(len(self.__recipes)):
      self.print_recipe(i)

  def printAllRecipes(self) -> None:
    for i in range(len(self.__recipes)):
      print(f"{i + 1}. " + self.__recipes[i].get_name())
  
  def handleInputs(self) -> None:
    while(True):
      try:
        index:int = int(input("Type here: ")) + 1
        print()
        match index:
          case 1:
            print("What coffe would you like today?")
            self.printAllRecipes()
            index = int(input("Type here: ")) - 1
            print()
            # self.makeCoffe()
          case 2:
            index = int(input(f"Which recipe would you like to see? 1-{len(self.__recipes)}: ")) - 1
            self.print_recipe(index)
          case 3:
            self.printAllRecipes_detailed()
          case _:
            print("Select one of the given options e.g: '1'\n")
            continue
        break
      except ValueError:
        print("Select one of the given options e.g: '1'\n")
      except KeyboardInterrupt:
        exit(0)
    


    