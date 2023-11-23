from user import User
from book import Book
from borrow import Borrow
from user_manage import UserManage

logged_in_user_id = None
is_admin = False
ADMIN_PASSWORD = "admin"
ADMIN_LOGIN = "admin"
ADMIN = "__ID__ADMIN__"
MAX_BOOKS_PER_STUDENT = 3


def is_admin_login(login, password):
    return (login == ADMIN_LOGIN and password == ADMIN_PASSWORD)


def log_in(login, password):
    users = User.get_users()
    for user in users:
        if user["login"] == login and user["password"] == password:
            logged_in_user_id = user["user_id"]
            return True
    return False


def log_out():
    global logged_in_user_id, is_admin
    logged_in_user_id = None
    is_admin = False


# Menu functions --------------------------------------------------


def handle_option(option):
  if option == "1":
      User.add_user()
  elif option == "2":
      User.display_users()
  elif option == "3":
      Book.add_book()
  elif option == "4":
      Book.display_books()
  elif option == "5":
      user_id = input("ID d'utilisateur : ")
      user = User.get_user(user_id)
      if user is not None:
          suspended_users = UserManage.read_suspended_users_from_file()
          if user_id in suspended_users:
              print(
                  "Compte d'utilisateur suspendu. L'emprunt de livres n'est pas autorisé."
              )
          elif len(user["borrowed_books"]) >= MAX_BOOKS_PER_STUDENT:
              print("Limite de livres empruntés atteinte.")
          else:
              Borrow.borrow_book(user_id, input("ID du livre à emprunter : "))
      else:
          print("Utilisateur introuvable.")
  elif option == "6":
      Borrow.display_borrowed_books()
  elif option == "7":
      UserManage.manage_user_accounts()
  elif option == "8":
      Borrow.manage_borrowed_books()
  elif option == "9":
      Borrow.display_late_returning_books()
  elif option == "10":
      user_id = input("ID d'utilisateur : ")
      book_id = input("ID du livre à marquer comme rendu : ")
      if (not user_id or book_id):
          print("Veuillez renseigner tous les champs.")
      else:
          Borrow.return_book(user_id, book_id)
  elif option == "11":
        Book.available_books()
  elif option == "12":
      user_id = input("ID de l'utilisateur : ")
      if user_id:
          Borrow.books_taken_by(user_id)
      else:
        print("ID d'utilisateur introuvable.")
  elif option == "0":
      log_out()
      print("Au revoir !")
  else:
      print("\nOption invalide. Veuillez sélectionner une option valide.\n")


def handle_user_option(option):
  if option == "1":
      Book.display_books()
  elif option == "2":
      book_id_to_borrow = input("ID du livre à emprunter : ")
      if book_id_to_borrow:
          Borrow.borrow_book(logged_in_user_id, book_id_to_borrow)
      else:
          print("Veuillez renseigner l'ID du livre à emprunter.")
  elif option == "3":
      Borrow.display_borrowed_books()
  elif option == "4":
      Borrow.return_book(logged_in_user_id, input("ID du livre à retourner : "))
  elif option == "5":
      Book.available_books()
  elif option == "6":
      Borrow.books_taken_by(logged_in_user_id)
  elif option == "0":
      log_out()
      print("Au revoir !")
  else:
      print("\nOption invalide. Veuillez sélectionner une option valide.\n")
    
# Menu display functions --------------------------------------------


def display_user_options():
  print("\nMenu utilisateur:--------------------------------------------------------\n")
  print("1 - Afficher les livres")
  print("2 - Emprunter un livre")
  print("3 - Afficher les livres empruntés")
  print("4 - Retourner un livre")
  print("5 - Afficher les livres disponibles")
  print("6 - Afficher les livres vous ayant empruntés")
  print("0 - Se déconnecter")

def display_admin_menu():
  print("\nMenu administrateur:------------------------------------------------------\n")
  print("1 - Ajouter un utilisateur")
  print("2 - Afficher les utilisateurs")
  print("3 - Ajouter un livre")
  print("4 - Afficher les livres")
  print("5 - Emprunter un livre")
  print("6 - Afficher les livres empruntés")
  print("7 - Gérer les comptes utilisateurs")
  print("8 - Gérer les emprunts de livres")
  print("9 - Afficher les livres en retard")
  print("10 - Marquer un livre comme rendu")
  print("11 - Afficher les livres disponibles")
  print("12 - Afficher les utilisateurs ayant empruntés un livre")
  print("0 - Se déconnecter")


def display_menu(is_admin):
    if is_admin:
        display_admin_menu()
    else:
        display_user_options()


# Main loop --------------------------------------------------------

while True:
  if logged_in_user_id is None:
      print("Vous n'êtes pas connecté.")
      user_or_admin = input("Voulez-vous vous connecter en tant qu'utilisateur (U) ou administrateur (A) ? ")

      if user_or_admin.lower() == "u":
          user_login = input("Saisissez votre identifiant : ")
          user_password = input("Saisissez votre mot de passe : ")

          if log_in(user_login, user_password) and not is_admin_login(user_login, user_password):
            print("Connecté en tant qu'utilisateur avec succès.")
            for user in User.get_users():
                if user["login"] == user_login:
                    logged_in_user_id = user["user_id"]
                    break

          else:
              print("Identifiant ou mot de passe incorrect ou vous utilisez des identifiants d'administrateur.")

      elif user_or_admin.lower() == "a":
          admin_login = input("Saisissez l'identifiant administrateur : ")
          admin_password = input("Saisissez le mot de passe administrateur : ")
          if is_admin_login(admin_login, admin_password):
              print("Connecté en tant qu'administrateur avec succès.")
              logged_in_user_id = ADMIN
              is_admin = True
          else:
              print("Identifiant ou mot de passe administrateur incorrect.")
      else:
          print("Choix invalide. Veuillez sélectionner une option valide (U ou A).")

  else:
      display_menu(is_admin)
      option = input("\nSélectionnez une option : ")

      if is_admin:
          handle_option(option)
      else:
          handle_user_option(option)

