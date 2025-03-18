from Recipe import Recipe
from Ingredient import Ingredient
from CoffeMachine import CoffeMachine

<<<<<<< HEAD
i_espresso = Ingredient("espresso", 100)
i_milk = Ingredient("milk", 50)
i_froth = Ingredient("froth", 50)
=======
i_espresso:Ingredient = Ingredient("Espresso", 100)
i_milk:Ingredient = Ingredient("Hot Milk", 50)
i_foam:Ingredient = Ingredient("Milk Foam", 50)

r_espresso:Recipe = Recipe("Espresso", {i_espresso: 1})
r_macchiato:Recipe = Recipe("Espresso Macchiato", {i_espresso: 1, i_foam: 1})
r_cappuccino:Recipe = Recipe("Cappuccino", {i_espresso: 1, i_milk: 1, i_foam: 2})
r_latte:Recipe = Recipe("Café Latte", {i_milk: 2, i_foam: 1, i_espresso: 1})
>>>>>>> 0f9c81ab68e476f16cdcc67bab861903eb963303

coffeMachine:CoffeMachine = CoffeMachine("New Model", [r_espresso, r_macchiato, r_cappuccino, r_latte])
# coffeMachine.add_recipe(r_latte)

while True:
  try:
    if(coffeMachine.get_state() == False):
      start = input("Machine is offline. Would you like to start the machine? y/n: ").lower()
      if start == "n":
        print("Goodbye")
        exit(0)
      elif start == "y":
        coffeMachine.toggleOnOff()
      else:
        continue
    coffeMachine.handleInputs()
  except KeyboardInterrupt:
    exit(0)