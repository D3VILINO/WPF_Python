# class CoffeMachine():
# class CashRegister():

class Ingredient:
  def __init__(self, name, price):
    self.__name = name
    self.__price = price

  def get_name(self):
    return self.__name

  def get_price(self):
    return self.__price

class Recipe:
  def __init__(self, name, ingredients:tuple, quantity:int):
    self.__name = name
    self.__ingredients = ingredients
    self.__quantity = quantity
    self.__price = 0

  def calculate_price(self):
    price = 50
    if (type(self.get_ingredients()) == tuple):
      for i in range(len(self.get_ingredients())):
        price += self.__ingredients[i].get_price() * self.__quantity[i]
    else:
      price += self.get_ingredients().get_price()
    self.__price = price
    return price

  def get_quantity(self):
    return self.__quantity

  def get_name(self):
    return self.__name

  def get_price(self):
    return self.__price

  def get_ingredients(self):
    return self.__ingredients



i_espresso = Ingredient("espresso", 100)
i_milk = Ingredient("milk", 50)
i_froth = Ingredient("froth", 50)

r_espresso = Recipe("Espresso", (i_espresso), (1))
r_macchiato = Recipe("Espresso Macchiato", (i_espresso, i_froth), (1, 1))
r_cappuccino = Recipe("Cappuccino", (i_espresso, i_milk, i_froth), (1, 1, 2))
r_cappuccino.calculate_price()
print(r_cappuccino.get_price())