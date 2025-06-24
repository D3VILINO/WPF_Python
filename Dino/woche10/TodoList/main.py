from visualisation import open_window

# Ich wollte eigentlich ein anderes Projekt machen aber auch nach 2 Wochen hat es nicht geklappt...
# Deswegen sehen sie hier eine sehr peinliche Abgabe :)

# Um sicherzugehen, dass Sachen gecatcht werden, selbst wenn ich es woanders vergessen sollte
try:
  open_window()
except BaseException as e:
  print(f"\033[34mFehler: {type(e).__name__}{(": " + str(e)) if str(e) else ""}\033[0m") # Blau weil ich das ganze Rot so langsam nicht mehr sehen kann
  exit(0)