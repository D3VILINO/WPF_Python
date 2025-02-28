from Ingredient import Ingredient

class Recipe:
  def __init__(self, name:str, ingredients:dict[Ingredient, int]) -> None:
    self.__name:str = name
    self.__ingredients:dict[Ingredient, int] = ingredients
    self.__price:int = self.calculate_price()

  def calculate_price(self) -> int:
    price:int = 50
    for ingredient, quantity in self.__ingredients.items():
      price += ingredient.get_price() * quantity
    print(price)
    return price

  def get_name(self) -> str:
    return self.__name

  def get_price(self) -> int:
    return self.__price

  def get_ingredients(self) -> dict[Ingredient, int]:
    return self.__ingredients
