import file

USERS_FILE_NAME = "users.txt"

class User:
    def __init__(self, id, name, nickname, email, login, password):
        self.id = id
        self.name = name
        self.nickname = nickname
        self.email = email
        self.login = login
        self.password = password

    def __str__(self):
        return f"User(id={self.id}, name='{self.name}', nickname='{self.nickname}', email='{self.email}', login='{self.login}', password='{self.password}')"

    def create_user(user_id, name, nickname, mail, login, password):
        user_data = f"{user_id},{name},{nickname},{mail},{login},{password}"
        file.write_to_file(USERS_FILE_NAME, user_data)
        print("Utilisateur ajouté avec succès.")

    def add_user():
      user_id = input("ID utilisateur : ")
      name = input("nom : ")
      nickname = input("prenom : ")
      mail = input("email : ")
      login = input("login : ")
      password = input("mot de passe : ")
      User.create_user(user_id, name, nickname, mail, login, password)
      print("Utilisateur ajouté avec succès.")
  
    def get_users():
      users = []
      lines = file.read_from_file(USERS_FILE_NAME)
      for line in lines:
          user_data = line.strip().split(",")
          user = {
              "user_id": user_data[0],
              "name": user_data[1],
              "nickname": user_data[2],
              "mail": user_data[3],
              "login": user_data[4],
              "password": user_data[5],
              "borrowed_books": [],
          }
          users.append(user)
      return users

    def get_user(user_id):
        users = User.get_users()
        for user in users:
            if user["user_id"] == user_id:
                return user
        return None

    def display_users():
        users = User.get_users()
        if not users:
            print("\nAucun utilisateur trouvé.\n")
        else:
            print("\nUtilisateurs:\n")
            for user in users:
                print(
                    f"ID: {user['user_id']}, nom: {user['name']}, prenom: {user['nickname']}, email: {user['mail']}, login: {user['login']}, mot de passe: {user['password']}"
                )
