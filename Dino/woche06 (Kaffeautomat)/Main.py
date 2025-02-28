# class CoffeMachine():
# class CashRegister():
from Recipe import Recipe
from Ingredient import Ingredient
from CoffeMachine import CoffeMachine


i_espresso = Ingredient("espresso", 100)
i_milk = Ingredient("milk", 50)
i_froth = Ingredient("froth", 50)

r_espresso = Recipe("Espresso", {i_espresso: 1})
r_macchiato = Recipe("Espresso Macchiato", {i_espresso: 1, i_froth: 1})
r_cappuccino = Recipe("Cappuccino", {i_espresso: 1, i_milk: 1, i_froth: 2})
r_latte = Recipe("Café Latte", {i_milk: 2, i_froth: 1, i_espresso: 1})

coffeMachine = CoffeMachine("New Model", [r_espresso, r_macchiato, r_cappuccino])
coffeMachine.add_recipe(r_latte)
coffeMachine.print_recipe(2)