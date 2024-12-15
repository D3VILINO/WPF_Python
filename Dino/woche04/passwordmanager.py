import os.path

# die txt wird dort erstellt und nach der Existenz geprüft, je nach aktuellem Pfad im Terminal. Habe dafür innerhalb der Zeit keine Lösung gefunden.
def main():
  try:
    database = get_database() # Database like "nameOfDatabase.txt"
    while True:
      try:
        print_menu(database)
        handle_menu(database)
      except (ValueError, TypeError):
        print("Please enter a valid selection (except)\n")
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
        if check_database():
          print("Your database already exists")
          continue
        else:
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
      print("Please enter a valid selection (except)\n")

def create_database() -> str:
  database = input("Please enter the name of the database you want to create: ")
  if not database.__contains__(".txt"): # keine gute, aber wenigstens irgendeine Überprüfung
      database += ".txt"
      file = open(database, "w")
      file.write("Index;Name;Password;URL;Note\n")
      file.close()
  return database

def check_database(database: str) -> bool:
  return os.path.exists(database)

def print_menu(database: str) -> None:
  print("=" * 41,
        f"Passwordmanager ({database})".center(41),
        "=" * 41,
        "    1) Show existing passwords",
        "    2) Add new password",
        "    3) Delete an existing password",
        "    4) Update password",
        "    5) Exit",
        sep="\n")

def handle_menu(database: str) -> None:
  selection = int(0)
  while True:
    selection = int(input("What do you like to do? "))
    if selection == 1:
      print_passwords(database)
    elif selection == 2:
      add_password(database)
    elif selection == 3:
      delete_password(database)
    elif selection == 4:
      update_password(database)
    elif selection == 5:
      print("Maybe next time. Seeya!")
      exit(0)
    else:
      print("Please enter a valid selection\n")
      continue
    break

# Eine lange URL zerschießt die Formatierung. ist also quasi wie bei MariaDB xd
def print_passwords(database: str, width:int = 120) -> None:
  header = ("Index", "Name", "Password", "URL", "Note")
  print(" " + "=" * (width + 4 - (width % 2)))
  for item in header:
    print(f"|{item:^{width // 5}}", end="")
  print("|")
  print(" " + "=" * (width + 4 - (width % 2)))

  file = open(database, "r")
  lines = file.readlines()
  for line in lines[1:]:
    data = line.strip().split(";")
    for d in data:
      print(f"|{d:^{width // 5}}", end="")
    print("|")
    print(" " + "-" * (width + 4 - (width % 2)))
  file.close()
  print("\n")

# Man könnte noch "validieren": wurde "Name" und "Password" gesetzt.
def add_password(database: str) -> None:
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

  content = content[:-1]

  file = open(database, "w")
  file.write(content + "\n")
  file.close()

def delete_password(database: str) -> None:
  to_delete = input("Enter index of the password which is to be deteled: ")
  if not 0 < int(to_delete) < number_of_lines(database):
    print("Please look at possible indices.")

  file = open(database, "r")
  lines = file.readlines()
  file.close()

  file = open(database, "w")
  successfull_delete = False
  for line in lines: 
    data = line.strip().split(";")
    if not successfull_delete:
      if data[0] == to_delete:
        successfull_delete = True
        continue
    else:
      data[0] = str(int(data[0]) - 1)
    file.write(";".join(data) + "\n")
  file.close()

def update_password(database: str) -> None:
  to_update = input("Enter index of the password which is to be updated: ")
  if not 0 < int(to_update) < number_of_lines(database):
    print("Please look at possible indices.")

  file = open(database, "r")
  lines = file.readlines()
  file.close()

  file = open(database, "w")
  for line in lines: 
    data = line.strip().split(";")
    if data[0] == to_update:
      print("What do you want to change?",
            "    1) Name",
            "    2) Password",
            "    3) URL",
            "    4) Note",
            "    5) Nothing",
            sep="\n")
      selection = int(input("Choose selection: "))
      if 0 < selection < 5:
        new_value = input("Enter new value: ")
        data[selection] = new_value
    file.write(";".join(data) + "\n")
  file.close()

def number_of_lines(database) -> int:
  """Including the header"""
  file = open(database, "r")
  akk = 0
  for _ in file:
    akk += 1
  file.close()
  return akk

main()
