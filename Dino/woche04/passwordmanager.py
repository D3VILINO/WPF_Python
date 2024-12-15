import os.path

def main():
  try:
    database = get_database() # Database like "nameOfDatabase.txt"
    while True:
      print_menu(database)
      handle_menu(database)
  except KeyboardInterrupt:
    exit(0)

def get_database() -> str:
  while True:
    try:
      print("=" * 41, "Passwordmanager".center(41),
            "=" * 41,
            "    1) Create new password Database",
            "    2) Start with existig Database",
            "    3) Cancel",
            sep="\n")
      selection = int(input("What do you want to do? "))

      if selection == 1:
        database = create_database()
      elif selection == 2:
        database = input("Please enter the name of the database you want to open: ")
        if not database.__contains__(".txt"): # keine gute, aber wenigstens irgendeine Überprüfung
          database += ".txt"
        if not check_database(database):
          print("Your datebase does not exist.")
          continue
      elif selection == 3:
        print("Maybe next time. Seeya!")
        exit(0)
      else:
        print("Please enter a valid selection\n")
        continue
      return database
    except (ValueError, TypeError):
      print("Please enter a valid selection\n")

def create_database() -> str:
  database = input("Please enter the name of the database you want to create: ")
  if not database.__contains__(".txt"): # keine gute, aber wenigstens irgendeine Überprüfung
      database += ".txt"
      file = open(database, "w")
      file.write("Index;Name;Password;URL;Note\n")
      file.close()
  return database

def check_database(database) -> bool:
  return os.path.exists(database)

def print_menu(database) -> None:
  print("=" * 41,
        f"Passwordmanager ({database})".center(41),
        "=" * 41,
        "    1) Show existing passwords",
        "    2) Add new password",
        "    3) Delete an existing password",
        "    4) Update password",
        "    5) Exit",
        sep="\n")

def handle_menu(database):
  selection = int(0)
  while True:
    try:
      selection = int(input("What do you like to do? "))
      if selection == 1:
        print_passwords(database)
      elif selection == 2:
        add_password(database)
      elif selection == 3:
        pass
        # delete_password(database)
      elif selection == 4:
        pass
        # update_password(database)
      elif selection == 5:
        print("Maybe next time. Seeya!")
        exit(0)
      else:
        print("Please enter a valid selection\n")
        continue
      break
    except (ValueError, TypeError):
      print("Please enter a valid selection (except)\n")

def print_passwords(database):
  file = open(database, "r")
  for line in file:
    print(line.rstrip())
  file.close()
  print("\n")

# TODO: Validation, ob Name und Password gesetzt sind und ob der Index bereits vergeben ist.
def add_password(database):
  # Index;Name;Password;URL;Note
  data_row = {"Index": None, "Name": None, "Password": None, "URL": "None", "Note": "None"}
  data_row.update({"Index": str(number_of_lines(database))})
  data_row.update({"Name": input("Name for password: ")})
  data_row.update({"Password": input("Password: ")}) # man könnte noch eine wiederholte Eingabe erfragen, aber das ist mehr Aufwand und muss nicht gewollt sein --> eine "Einstellung", ob man das will?
  if "y" == input("Part of a Website? y/n: ").lower():
    data_row.update({"URL": input("URL: ")})
  if "y" == input("Add note to password? y/n: ").lower():
    data_row.update({"Note": input("Note: ")})

  # geht das alles nicht vielleicht etwas schöner?
  file = open(database, "a")
  for value in data_row.values():
    file.write(value + ";")
  file.close()
  
  file = open(database, "r")
  content = file.read()
  file.close()

  if content.endswith(";"):
      content = content[:-1]

  file = open(database, "w")
  file.write(content + "\n")
  file.close()

def delete_password(database):
  pass

def update_password(database):
  pass

def number_of_lines(database) -> int:
  """Including the header"""
  file = open(database, "r")
  akk = 0
  for _ in file:
    akk += 1
  file.close()
  return akk

main()
