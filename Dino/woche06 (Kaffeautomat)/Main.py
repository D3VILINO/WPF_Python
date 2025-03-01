# class CashRegister():
from Recipe import Recipe
from Ingredient import Ingredient
from CoffeMachine import CoffeMachine

i_espresso:Ingredient = Ingredient("Espresso", 100)
i_milk:Ingredient = Ingredient("Hot Milk", 50)
i_foam:Ingredient = Ingredient("Milk Foam", 50)

r_espresso:Recipe = Recipe("Espresso", {i_espresso: 1})
r_macchiato:Recipe = Recipe("Espresso Macchiato", {i_espresso: 1, i_foam: 1})
r_cappuccino:Recipe = Recipe("Cappuccino", {i_espresso: 1, i_milk: 1, i_foam: 2})
r_latte:Recipe = Recipe("Café Latte", {i_milk: 2, i_foam: 1, i_espresso: 1})

coffeMachine:CoffeMachine = CoffeMachine("New Model", [r_espresso, r_macchiato, r_cappuccino])
coffeMachine.add_recipe(r_latte)
# coffeMachine.print_recipe(2)
# coffeMachine.printAllRecipes_detailed()
coffeMachine.printAllRecipes()
coffeMachine.toggleOnOff()
coffeMachine.handleInputs()