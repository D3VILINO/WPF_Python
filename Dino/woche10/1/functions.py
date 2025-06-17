from sympy import Eq, parse_expr, pretty, solve #type: ignore[import-untyped]
import re
from tkinter import END, Entry, Label

_operators:set[str] =  {"+", "-", "*", "/", "=", "^"}
_numbers:set[str] = set(str(i) for i in range(0,10))
unique_vars:list[str] = ["", ""]

def make_parsable(function:str) -> str:
  function = function.replace(" ", "")
  unique_vars = list(set(function).difference(_operators).difference(_numbers))
  function = re.sub(r"([\^])", r"**", function)
  for var in unique_vars:
    function = re.sub(f"([0-9])({var})", r"\1*\2", function)
  return function

def add_solution(function:str, label:Label, do_pretty:bool = False) -> None | str:
  function = make_parsable(function)
  solution = my_solve(function)
  solve_to, r_expr = solution.replace(" ", "").split("=")

  label.config(text=solve_to + "=" + r_expr)
  return str(pretty(solve_to + "=" + r_expr))

def my_solve(function:str) -> str:
  res:None|str | tuple[None,str] = validate_function(function)

  if isinstance(res, tuple):
    check = res[0]
    function = res[1]
  else:
    check = res

  if check == None:
    left, right = function.split("=")
    eq:Eq = Eq(parse_expr(left), parse_expr(right))

    solve_to = unique_vars[0]
    solved_res = solve(eq, solve_to)
    text = str(solved_res)[1:-1]
    return solve_to + " = " + text
  else:
    return check

def validate_function(function:str) -> str | tuple[None, str]:
  find:int = function.find("=")
  rfind:int = function.rfind("=")

  # Gleichheitszeichen
  if find == -1:
    return "Sie haben kein Gleichheitszeichen"
  elif rfind != find:
    return "Sie haben zu viele Gleichheitszeichen"
  elif find == 0:
    return "Vor Ihrem Gleichheitszeichen fehlt ein Ausdruck"
  elif rfind == len(function) - 1:
    return "Nach Ihrem Gleichheitszeichen fehlt ein Ausdruck"

  # Variablen Anzahl
  unique:set = set(function)
  unique = unique.difference(_operators).difference(_numbers)
  if len(unique) != 2:
    return "Dieses Programm läuft nur bei genau zwei\nunterschiedlichen Variablen. (Bsp: 2x + y - 5 = 3x)"

  # Valide Ausdrücke / in Valide Ausdrücke umformen
  for var in unique:
    function = re.sub(f"([0-9])({var})", r"\1*\2", function)
  function = re.sub(r"([\^])", r"**", function)

  function_left:str = function.split("=")[0]
  function_right:str = function.split("=")[1]

  try:
   Eq(parse_expr(function_left), parse_expr(function_right))
  except Exception as e:
    return "Ihre Gleichung scheint inkorrekte Stellen zu haben"

  return (None, function)

def test_import(entry:Entry) -> None:
  entry.delete(0, END)
  entry.insert(0, "3x^2 = -7x^2 + 250y")