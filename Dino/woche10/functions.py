from sympy import Eq, parse_expr, root, solve as n_solve #type: ignore
import re
from tkinter import Label

def solve(function:str, output:Label) -> None:
  res:None|str | tuple[None,str] = validate_function(function)

  if isinstance(res, tuple):
    check = res[0]
    function = res[1]
  else:
    check = res

  if check == None:
    operators:set[str] =  {"+", "-", "*", "/", "=", "^"}
    numbers:set[str] = set(str(i) for i in range(0,10))
    unique:set|tuple = set(function)
    unique = unique.difference(operators).difference(numbers) if isinstance(unique, set) else unique
    unique = tuple(unique)

    left, right = function.split("=")
    eq = Eq(parse_expr(left), parse_expr(right))

    solve_to = unique[0]
    output.config(text=str(solve_to) + "=" + (str(n_solve(eq, solve_to)))[1:-1])
  else:
    output.config(text=check)

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
  operators:set[str] =  {"+", "-", "*", "/", "=", "^"}
  numbers:set[str] = set(str(i) for i in range(0,10))
  unique:set = set(function)
  unique = unique.difference(operators).difference(numbers)
  if len(unique) != 2:
    return "Dieses Programm läuft nur bei genau zwei\nunterschiedlichen Variablen. (Bsp: 2x + y - 5 = 3x)"

  # Valide Ausdrücke
  for var in unique:
    function = re.sub(f"([0-9])({var})", r"\1*\2", function)

  function_left:str = function.split("=")[0]
  function_right:str = function.split("=")[1]

  try:
   Eq(parse_expr(function_left), parse_expr(function_right))
  except Exception as e:
    return "Ihre Gleichung scheint inkorrekte Stellen zu haben"

  return (None, function)

