import file
BOOKS_FILE_NAME = "books.txt"

class Book:
    def __init__(self, book_id, title, author, editor, isbn, num_copies, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.editor = editor
        self.isbn = isbn
        self.num_copies = num_copies
        self.year = year

    def __str__(self):
        return f"ID: {self.book_id}, title: {self.title}, author: {self.author}, editor: {self.editor}, ISBN: {self.isbn}, num_copies: {self.num_copies}, year: {self.year}"

    def get_book(book_id):
        books = Book.get_books()
        for book in books:
            if book.book_id == book_id:
                return book
        return None

    def add_book():
        book_id = input("ID livre : ")
        title = input("titre : ")
        author = input("auteur : ")
        editor = input("editeur : ")
        isbn = input("ISBN : ")

        while True:
          try:
              num_copies = int(input("nombre de copies : "))
              break
          except ValueError:
              answer = input("Veuillez saisir un nombre entier\n pour quittez tapez q, pour contiuez tapez entrer (any): ")
              if answer == "q":
                 return
        while True:
          try:
              year = int(input("année : "))
              break
          except ValueError:
              answer = input("Veuillez saisir un nombre entier\n pour quittez tapez q, pour contiuez tapez entrer (any): ")
              if answer == "q":
                 return
        if book_id and title and author and editor and isbn and num_copies and year:
            book = Book(book_id, title, author, editor, isbn, num_copies, year)
            book.create_book()
            print("Livre ajouté avec succès.")
        else:
            print("Veuillez renseigner tous les champs.")

    def create_book(self):
        book_data = f"{self.book_id},{self.title},{self.author},{self.editor},{self.isbn},{self.num_copies},{self.year}"
        file.write_to_file(BOOKS_FILE_NAME, book_data)

    @staticmethod
    def get_books():
        try:
            lines = Book.read_from_file(BOOKS_FILE_NAME)
            books = []
            for line in lines:
                book_data = line.strip().split(",")
                book = {"book_id": book_data[0], "title": book_data[1], "author": book_data[2]}
                books.append(book)
            return books
        except FileNotFoundError:
            print(f"Fichier {BOOKS_FILE_NAME} introuvable.")
            return []

    @staticmethod
    def get_book_by_id(book_id):
        books = Book.get_books()
        for book in books:
            if book['book_id'] == book_id:
                return book
        return None

    @staticmethod
    def display_books():
        books = Book.get_books()
        if not books:
            print("Aucun livre disponible.")
        else:
            print("\nListe des livres:")
            for book in books:
                print(
                    f"\tID: {book.get('book_id', '')}, titre: {book.get('title', '')}, auteur: {book.get('author', '')}, editeur: {book.get('editor', '')}, ISBN: {book.get('isbn', '')}, nombre de copies: {book.get('num_copies', '')}, année: {book.get('year', '')}"
                )

    def available_books():
        from borrow import Borrow
        borrowed_books = Borrow.read_all_borrowed_books()
        all_books = Book.get_books()
        available_books = [
            book for book in all_books if book["book_id"] not in borrowed_books
        ]
        print("\nAvailable Books:")
        for book in available_books:
            print(
                f"ID: {book['book_id']}\tTitle: {book['title']}\tAuthor: {book['author']}"
            )

    @staticmethod
    def read_from_file(file_name):
        try:
            with open(file_name, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Fichier {file_name} introuvable.")
            return []
