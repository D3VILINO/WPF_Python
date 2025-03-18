class Ingredient:
  def __init__(self, name:str, price:int) -> None:
    self.__name:str = name
    self.__price:int = price

  def get_name(self) -> str:
    return self.__name

  def get_price(self) -> int:
    return self.__price