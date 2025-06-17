from sympy import Eq, parse_expr, solve, lambdify, simplify #type: ignore[import-untyped]
import re
from tkinter import END, Entry, Label

unique_vars:list[str] = ["", ""]
f1:str = ""
solution:list = []

def submitted_entry(entry_function:str, output_label:Label) -> None:
  global f1, solution, unique_vars

  f1 = make_parsable(entry_function)
  valid, info = validate_function()

  if valid:
    solution = my_solve(unique_vars[0])
    print(solution)
    text:str = unique_vars[0] + " = " + solution[0] + "\n"
    if len(solution) > 1:
      text = ""
      subscripted_char = ("\u2080", "\u2081", "\u2082", "\u2083", "\u2084", "\u2085", "\u2086", "\u2087", "\u2088", "\u2089")
      for i in range(0, len(solution)):
        text += unique_vars[0] + subscripted_char[i+1] + " = " + solution[i] + "\n"
    output_label.configure(text=text)
  else:
    output_label.configure(text=info)

def my_solve(solve_for:str) -> list:
  global f1
  f1_left, f1_right = map(parse_expr, f1.split("="))
  eq:Eq = Eq(f1_left, f1_right)
  solution:list[str] = str(solve(eq, solve_for))[1:-1].split(",")
  for i in range(len(solution)):
    solution[i] = solution[i].strip()
  return solution

def validate_function() -> tuple[bool, str]:
  global f1, unique_vars

  # Gleichheitszeichen
  find:int = f1.find("=")
  if find == -1:
    return False, "Sie haben kein Gleichheitszeichen"
  elif find == 0:
    return False, "Vor Ihrem Gleichheitszeichen fehlt ein Ausdruck"
  elif find == len(f1) - 1:
    return False, "Nach Ihrem Gleichheitszeichen fehlt ein Ausdruck"
  elif f1.count("=") > 1:
    return False,"Sie haben zu viele Gleichheitszeichen"

  # Variablen Anzahl
  if len(unique_vars) != 2:
    return False, "Dieses Programm läuft nur bei genau zwei\nunterschiedlichen Variablen. (Bsp: 2x + y - 5 = 3x)"

  # Valide Ausdrücke
  f1_left, f1_right= map(parse_expr, f1.split("="))
  try:
   Eq(f1_left, f1_right)
  except Exception as e:
    return False, "Ihre Gleichung scheint inkorrekte Stellen zu haben"

  # Fehlerfrei
  return True, "Validierung erfolgreich"

def make_parsable(func:str) -> str:
  global unique_vars
  operators:set[str] =  {"+", "-", "*", "/", "=", "^"}
  numbers:set[str] = {str(i) for i in range(0,10)}

  func = func.replace(" ", "")
  unique_vars = sorted(list(set(func).difference(operators).difference(numbers)))

  func = re.sub(r"([\^])", r"**", func)
  for var in unique_vars:
    func = re.sub(f"([0-9])({var})", r"\1*\2", func)

  return func

def test_import(entry:Entry) -> None:
  entry.delete(0, END)
  entry.insert(0, "3x^2 = -7x^2 + 250y")