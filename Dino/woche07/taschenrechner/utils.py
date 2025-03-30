def check_for_dots(s:str) -> str:
  count = 0
  for i in range(len(s) - 1, -1, -1):
    if s[i] == "." and s[i-1].isnumeric():
      count += 1
    if i != 0 and s[i-1].isnumeric():
      continue
    break

  if count != 0:
    return s
  return s + "."

def change_plus_minus(s: str) -> str:
  for i in range(len(s) - 1, -1, -1): 
    if s[i] in ("/", "*"): 
      return s[:i+1] + "-" + s[i+1:]
    elif s[i] == "+":
      return s[:i] + "-" + s[i+1:]
    elif s[i] == "-":  
      return s[:i] + "+" + s[i+1:]

  if s.startswith("-"):  
    return s[1:]
  return "-" + s

def toggle_sqrt(s:str) -> str:
  if s[-1] == ")":
    for i in range(len(s) - 2, -1, -1):
      if s[i] == "(":
        return s[:i-4] + s[i+1:-1]

  for i in range(len(s) - 1, -1, -1):
    if (not s[i].isnumeric()) and s[i] != ".":
      return s[:i+1] + "sqrt(" + s[i+1:] + ")"
  
  return f"sqrt({s})"

def into_percent(s:str) -> str:
  for i in range(len(s) - 1, -1, -1): 
    if not (s[i].isnumeric() or s[i] == "."):  
      num = s[i+1:] 
      if num:
        return s[:i+1] + str(float(num) / 100)
      return s  
  return str(float(s) / 100)

def divide_by(s:str) -> str:
  if s == "":
    return "1/"
  return "*1/"