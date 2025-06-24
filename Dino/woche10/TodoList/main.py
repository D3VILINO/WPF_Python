from visualisation import open_window

try:
  open_window()
except BaseException as e:
  print(f"\033[34mFehler: {type(e).__name__}{(": " + str(e)) if str(e) else ""}\033[0m") # Blau weil ich das ganze Rot so langsam nicht mehr sehen kann
  exit(0)