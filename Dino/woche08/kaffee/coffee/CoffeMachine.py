from coffee.CashMachine import CashMachine
from time import sleep
from coffee.Recipe import Recipe
from coffee.Ingredient import Ingredient
from coffee.CashRegister import CashRegister
from coffee.utils import indentation

class CoffeMachine():
  def __init__(self, model:str, recipes:list[Recipe]):
    self.__state:bool = False
    self.__model:str = model
    self.__recipes:list[Recipe] = recipes
    self.__cashRegister:CashRegister = CashRegister()

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
    return self.__state

  def printOptions(self) -> None:
    options:tuple = ("Get a Coffe", "Show Recipe for a Coffe", "Show all Recipies", "Turn Machine off")
    for i in range(1, len(options) + 1):
      print(f"{i:>{indentation(i)}}. " + options[i - 1])

  def add_recipe(self, recipe:Recipe) -> None:
    self.__recipes.append(recipe)

  def print_recipe(self, index:int) -> None:
    ingredients:dict[Ingredient, int] = self.__recipes[index].get_ingredients()
    print(self.__recipes[index].get_name() + ": ")
    for ingredient, quantity in ingredients.items():
      print(f"{'x':>{indentation("x")}}" + str(quantity) + " " + ingredient.get_name())
    print()

  def printAllRecipes_detailed(self) -> None:
    for i in range(len(self.__recipes)):
      self.print_recipe(i)

  def printAllRecipes(self) -> None:
    for i in range(1, len(self.__recipes) + 1):
      print(f"{i:>{indentation(i)}}. " + self.__recipes[i - 1].get_name())

  def handleInputs(self) -> None:
    while(True):
      try:
        print("What would you like me to do?")
        self.printOptions()
        index:int = int(input("Type here: "))
        print()
        match index:
          case 1:
            print("What coffe would you like today?")
            self.printAllRecipes()
            index = int(input("Type here: ")) - 1
            print()
            if self.__cashRegister.takeMoney(self.__recipes[index].get_price()) != False:
              self.makeCoffe(index)
              akk = self.__cashRegister.getMoney()
              for i in akk:
                print(i)
          case 2:
            index = int(input(f"Which recipe would you like to see? 1-{len(self.__recipes)}: ")) - 1
            print()
            self.print_recipe(index)
          case 3:
            self.printAllRecipes_detailed()
          case 4:
            self.toggleOnOff()
            break
          case _:
            print("Select one of the given options e.g: '1'\n")
      except (ValueError, IndexError):
        print("Select one of the given options e.g: '1'\n")

  def makeCoffe(self, index:int) -> None:
    print("Starting Process... Adding: ")
    ingredients:dict[Ingredient, int] = self.__recipes[index].get_ingredients()
    for ingredient, quantity in ingredients.items():
      for i in range(quantity):
        name:str = ingredient.get_name()
        print(f"{name:>{indentation(name)}}")
        sleep(1)
    print("\nPlease enjoy your fresh " + self.__recipes[index].get_name() + "\n")
    sleep(2)