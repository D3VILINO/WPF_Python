class Recipe:
  def __init__(self, name, ingredients:tuple, quantity:int):
    self.__name = name
    self.__ingredients = ingredients
    self.__quantity = quantity
    self.__price = 0

  def calculate_price(self):
    price = 50
    if (type(self.__ingredients) == tuple):
      for i in range(len(self.__ingredients)):
        price += self.__ingredients[i].get_price() * self.__quantity[i]
    else:
      price += self.__ingredients.get_price() * self.__quantity
    self.__price = price
    return price

  def get_quantities(self):
    return self.__quantity

  def get_name(self):
    return self.__name

  def get_price(self):
    return self.__price

  def get_ingredients(self):
    return self.__ingredients
