from time import sleep
from tkinter import *
from typing import TypedDict
from coffee.Recipe import Recipe
from coffee.CoffeMachine import CoffeMachine
from coffee.Ingredient import Ingredient

# finished
class Types_Of_Objects(TypedDict):
  ingredients: list[Ingredient]
  recipes: list[Recipe]
  coffeemachine: CoffeMachine

# finished
def initialize_objects() -> Types_Of_Objects:
  i_espresso:Ingredient = Ingredient("Espresso", 100)
  i_milk:Ingredient = Ingredient("Hot Milk", 50)
  i_foam:Ingredient = Ingredient("Milk Foam", 50)
  list_ingredients:list[Ingredient] = [i_espresso, i_milk, i_foam]

  r_espresso:Recipe = Recipe("Espresso", {i_espresso: 1})
  r_macchiato:Recipe = Recipe("Espresso Macchiato", {i_espresso: 1, i_foam: 1})
  r_cappuccino:Recipe = Recipe("Cappuccino", {i_espresso: 1, i_milk: 1, i_foam: 2})
  r_latte:Recipe = Recipe("Café Latte", {i_milk: 2, i_foam: 1, i_espresso: 1})
  list_recipies:list[Recipe] = [r_espresso, r_macchiato, r_cappuccino, r_latte]

  coffe_machine:CoffeMachine = CoffeMachine("New Model", [r_espresso, r_macchiato, r_cappuccino, r_latte])

  return {"ingredients":list_ingredients, "recipes":list_recipies, "coffeemachine":coffe_machine}

# finished
def clear_frame(frame:Frame) -> None:
  for widget in frame.winfo_children():
    widget.destroy()

# finished
def create_header(frame:Frame) -> Label:
  frame_header:Frame = Frame(frame)
  frame_header.pack()

  header:Label = Label(frame_header, padx=5, text="="*41, font=("Helvetica", 20))
  header.pack(fill=BOTH, expand=TRUE, anchor=N)

  header = Label(frame_header, padx=5, text="Kaffeeautomat", font=("Helvetica", 20))
  header.pack(fill=BOTH, expand=TRUE, anchor=N)
  header_label = header

  header = Label(frame_header, padx=5, text="="*41, font=("Helvetica", 20))
  header.pack(fill=BOTH, expand=TRUE, anchor=N)
  return header_label

# finished
def create_power(frame:Frame) -> None:
  clear_frame(frame)

  Label(frame, text="Machine is offline.", font=("Helvetica", 16)).pack(pady=5)
  Button(frame, text="Turn ON", command=lambda: create_options(frame)).pack()
  Button(frame, text="Turn OFF", command=lambda: exit()).pack()

# finished
def create_options(frame:Frame) -> None:
  clear_frame(frame)

  Label(frame, text="What would you like to do?", font=("Helvetica", 16)).pack(pady=5)
  Button(frame, text="Make Coffee", command=lambda: create_coffee(frame)).pack()
  Button(frame, text="Show specific Recipe", command=lambda:create_show_specific_recipe(frame)).pack()
  Button(frame, text="Show all Recipies", command=lambda: create_show_recipes(frame)).pack()
  Button(frame, text="Sleep Mode", command=lambda: create_power(frame)).pack()

# finished
def create_coffee(frame:Frame) -> None:
  clear_frame(frame)
  global object_dict

  recipes_list = object_dict["recipes"]
  for i in range(len(recipes_list)):
    Button(frame, text=str(i + 1) + ". " + recipes_list[i].get_name(), command=lambda index = i:create_make_coffee(frame, index)).pack(anchor="w")

  Button(frame, text="Go Back", command=lambda:create_options(frame)).pack()

# finished but without dynamic
def create_make_coffee(frame:Frame, index:int) -> None:
  clear_frame(frame)
  global object_dict

  recipe:Recipe = object_dict["recipes"][index]
  ingredients = recipe.get_ingredients()

  Label(frame, text=f"In Progress: {recipe.get_name()}... Adding:", font=("Helvetica", 16)).pack()
  label_progress = Label(frame, text="")
  label_progress.pack()
  for ingredient, quantity in ingredients.items():
    for i in range(quantity):
      label_progress.config(text= label_progress.cget("text") + ingredient.get_name() + "\n")
  Label(frame, text="Your coffee is ready", font=("Helvetica", 16)).pack()
  random_Frame:Frame = Frame(frame)
  random_Frame.pack()
  for i in range(3):
    Label(random_Frame, text=".").grid(row=0, column=i)
  frame.after(2000, create_options, frame)

# finished
def create_show_recipes(frame:Frame) -> None:
  clear_frame(frame)

  Label(frame, text="Show All Recipes", font=("Helvetica", 16)).pack()
  show_recipe(frame, "all")
  Button(frame, text="Go Back", command=lambda:create_options(frame)).pack()

# finished
def create_show_specific_recipe(frame:Frame) -> None:
  clear_frame(frame)

  global object_dict
  recipes_list = object_dict["recipes"]
  for i in range(len(recipes_list)):
    Button(frame, text=str(i + 1) + ". " + recipes_list[i].get_name(), command=lambda index = i:show(index)).pack(anchor="w")

  Button(frame, text="Go Back", command=lambda:create_options(frame)).pack()

  def show(index):
    clear_frame(frame)
    show_recipe(frame, index)
    Button(frame, text="Go Back", command=lambda:create_show_specific_recipe(frame)).pack()
    Button(frame, text="Go to Main", command=lambda:create_options(frame)).pack()

# finished
def show_recipe(frame, type:str|int = "all") -> None:
  global object_dict
  recipes_list = object_dict["recipes"]
  if type == "all":
    for recipe in recipes_list:
      Label(frame, text=recipe.get_name()).pack(anchor="w")
      ingredents:dict[Ingredient,int] = recipe.get_ingredients()
      for ingredient, amount in ingredents.items():
        Label(frame, text=f"    {amount}x {ingredient.get_name()}").pack(anchor="w")
  else:
    recipe:Recipe = recipes_list[type]
    Label(frame, text=recipe.get_name()).pack(anchor="w")

    ingredents:dict[Ingredient,int] = recipe.get_ingredients()
    for ingredient, amount in ingredents.items():
      Label(frame, text=f"    {amount}x {ingredient.get_name()}").pack(anchor="w")

object_dict = initialize_objects()
