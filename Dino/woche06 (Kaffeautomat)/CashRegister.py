from time import sleep
from utils import indentation

class CashRegister:
  def __init__(self, money200:int=10, money100:int=10, money50:int=10):
    self.__money200:int = money200
    self.__money100:int = money100
    self.__money50:int = money50

  def takeMoney(self, price:int) -> int:
    if price <= 0:
      return abs(price)
    print("To pay: " + f"{(price/100):.2f}" + "€")
    while(True):
      try:
        paid = int(input("Pay: "))
        match paid:
          case 2 | 1:
            price = self.takeMoney(price - (paid * 100))
          case 50:
            price = self.takeMoney(price - 50)
          case _:
            print("\nInput 2, 1 or 50")
            continue
        return price
      except ValueError:
        print("\nInput 2, 1 or 50")

  def giveExchangeMoney(self, exchange:int) -> None:
    exchangeList:dict[str, int] = {"2€": 0, "1€": 0, "0.50€": 0}
    newExchange:int = exchange
    while (newExchange > 0):
      if newExchange - 200 >= 0:
        exchangeList["2€"] += 1
        newExchange -= 200
      elif newExchange - 100 >= 0:
        exchangeList["1€"] += 1
        newExchange -= 100
      else:
        exchangeList["0.50€"] += 1
        newExchange -= 50

    if exchange != 0:  
      print("\nYour Exchange: " + f"{(exchange/100):.2f}" + "€ in: ")
      for money, quantity in exchangeList.items():
        if quantity != 0:
          print(f"{"x":>{indentation("x")}}{quantity} {money}")
          sleep(0.5)
      sleep(0.5)
    print()