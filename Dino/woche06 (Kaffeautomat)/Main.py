# class CoffeMachine():
# class CashRegister():
from Recipe import Recipe
from Ingredient import Ingredient
from CoffeMachine import CoffeMachine

i_espresso = Ingredient("espresso", 100)
i_milk = Ingredient("milk", 50)
i_froth = Ingredient("froth", 50)

r_espresso = Recipe("Espresso", (i_espresso), (1))
r_macchiato = Recipe("Espresso Macchiato", (i_espresso, i_froth), (1, 1))
r_cappuccino = Recipe("Cappuccino", (i_espresso, i_milk, i_froth), (1, 1, 2))
r_latte = Recipe("Café Latte", (i_milk, i_froth, i_espresso), (2, 1, 1))

coffeMachine = CoffeMachine("New Model", [r_espresso, r_macchiato, r_cappuccino, r_latte])
coffeMachine.updateRecipePrice()
coffeMachine.print_recipe(2)