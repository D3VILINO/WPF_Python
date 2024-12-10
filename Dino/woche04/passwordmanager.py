import os.path

def main():
  database = get_database() # Database like "nameOfDatabase.txt"
  while True:
    print_menu(database)
    handle_menu(database)

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
        if not database.__contains__(".txt"): # not perfect but at least something
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
  if not database.__contains__(".txt"): # not perfect but at least something
      database += ".txt"
      open(database, "w").close()
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
  selection = int(input("What do you want to do? "))

def handle_menu(database):
  selection = 0
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
    except (ValueError, TypeError):
      print("Please enter a valid selection\n")

def print_passwords(database):
  file = open(database, "r")
  for line in file:
    print(line.rstrip())
  print("\n")

def add_password(database):
  # Index,Name,Password,URL,Note
  file = open(database, "r")
  number_of_passwords = len(file)
  print(number_of_passwords)

def delete_password(database):
  pass

def update_password(database):
  pass

main()
