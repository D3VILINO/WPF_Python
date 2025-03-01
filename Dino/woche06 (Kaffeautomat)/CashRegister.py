from time import sleep
from utils import indentation

class CashRegister:
  def __init__(self, money200:int=10, money100:int=10, money50:int=10):
    self.__money200:int = money200
    self.__money100:int = money100
    self.__money50:int = money50

  def takeMoney(self, price:int, currentMoney:list[int]|None = None) -> int | bool:
    if currentMoney is None:
      currentMoney = [self.__money200, self.__money100, self.__money50]

    if price <= 0:
      if self.giveExchangeMoney(abs(price), currentMoney) == False:
        return False
      else: 
        return abs(price)
    
    print("To pay: " + f"{(price/100):.2f}" + "€")

    while(True):
      try:
        paid = int(input("Pay: "))
        match paid:
          case 2:
            currentMoney[0] += 1
            return self.takeMoney(price - (paid * 100), currentMoney)
          case 1:
            currentMoney[1] += 1
            return self.takeMoney(price - (paid * 100), currentMoney)
          case 50:
            currentMoney[2] += 1
            return self.takeMoney(price - 50, currentMoney)
          case _:
            print("\nInput 2, 1 or 50")
            continue
      except ValueError:
        print("\nInput 2, 1 or 50")

  def giveExchangeMoney(self, exchange:int, currentMoney:list[int]) -> None | bool:
    exchangeList:dict[str, int] = {"2€": 0, "1€": 0, "0.50€": 0}
    newExchange:int = exchange
    if exchange != 0:  
      while (newExchange > 0):
        if newExchange - 200 >= 0 and currentMoney[0] > 0:
          exchangeList["2€"] += 1
          newExchange -= 200
          currentMoney[0] -= 1
        elif newExchange - 100 >= 0 and currentMoney[1] > 0:
          exchangeList["1€"] += 1
          newExchange -= 100
          currentMoney[1] -= 1
        elif newExchange - 50 >= 0 and currentMoney[2] > 0:
          exchangeList["0.50€"] += 1
          newExchange -= 50
          currentMoney[2] -= 1
        else:
          print("Error: not enough exchange.")
          return False
      
      self.__money200 = currentMoney[0]
      self.__money100 = currentMoney[1]
      self.__money50 = currentMoney[2]
      print("\nYour Exchange: " + f"{(exchange/100):.2f}" + "€ in: ")
      for money, quantity in exchangeList.items():
        if quantity != 0:
          print(f"{"x":>{indentation("x")}}{quantity} {money}")
          sleep(0.5)
      sleep(0.5)
    print()
    return None
  
  def getMoney(self) -> tuple[int, int, int]:
    return (self.__money200, self.__money100, self.__money50)