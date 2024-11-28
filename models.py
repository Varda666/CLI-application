import json
from json import load, dump


class Books:
    """Класс для работы с книгами в формате JSON"""

    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = []
        self.load()

    def load(self):
        """Загрузить файл с книгами"""

        try:
            with open(self.filename, encoding='utf-8') as fp:
                self.books = json.load(fp)
                return self.books
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {self.filename}. Инициализация пустого списка книг.")
            self.books = []

    def save(self):
        """Сохраняет файл с книгами"""

        with open(self.filename, 'w', encoding='utf-8') as fp:
            json.dump(self.books, fp, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Добавляет книгу"""

        if year < 0:
            raise ValueError("Год публикации не может быть отрицательным.")
        if not title or not author or not year:
            raise ValueError("Название и автор книги не могут быть пустыми.")
        for book in self.books[:]:
            if title == book['title']:
                print(f'Книга "{title}" уже есть в списке')
        book_id = len(self.books) + 1
        new_book = {'book_id': book_id, 'title': title, 'author': author, 'year': year, 'status': 'в наличии'}
        self.books.append(new_book)
        self.save()
        return new_book

    def __str__(self):
        return '\n'.join(
            f"ID книги: {book['book_id']}, Название книги: {book['title']}, Автор: {book['author']}, Год издания: {book['year']}, Статус: {book['status']},"
            for book in self.books
        )

    def remove_book(self, book_id):
        """Удаляет книгу"""

        books_ids = []
        for book in self.books[:]:
            books_ids.append(book['book_id'])
            if book_id == book['book_id']:
                self.books.remove(book)
                self.save()
                print(f'Книга с ID {book_id} успешно удалена.')
        if book_id not in books_ids:
            print(f'Книги с ID {book_id} нет в списке')

    def get_books(self):
        """Получить все книги"""
        return self.books

    def get_book(self, param):
        """Получить книгу по названию, автору, году"""

        for book in self.books[:]:
            if param == book['title']:
                return book
            elif param == book['author']:
                return book
            elif param == book['year']:
                return book

    def change_status(self, book_id: int, status):
        """Меняет статус книги (в наличии/выдана/утеряна)"""

        books_ids = []
        for book in self.books[:]:
            books_ids.append(book['book_id'])
            if book_id == book['book_id']:
                book['status'] = status
                self.save()
        if book_id not in books_ids:
            print(f'Книги с ID {book_id} нет в списке')








    # def __init__(self, title: str = None, author: str = None, year: str or int = None, data: dict = None, status: str = None) -> None:
    #
    #     self.id = id
    #     self.title = title
    #     self.author = author
    #     self.year = year
    #     self.status = status
    #
    #     if data:
    #         self.id = data.get('id')
    #         self.title = data.get('title')
    #         self.author = data.get('author')
    #         self.year = data.get('year')
    #         self.status = data.get('status')
    #
    # def check(self) -> set:
    #     error: set[str or None] = set()
    #     error.add(Book.check_year(self))
    #     error.add(check_status(self.status))
    #     error.discard(None)
    #     return error
    #
    # def check_year(self) -> str or None:
    #     if not isinstance(self.year, int) or self.year < 1000 or self.year > 10000:
    #         return "Некорректный год издания книги"
    #     return None
    #
    # def receiving_issuing(self, status: str) -> bool:
    #     check: str or None = check_status(status)
    #     if check:
    #         return False
    #     self.status = status
    #     return True
    #
    # def book_dict(self) -> dict:
    #     return {'id': self.id, 'title': self.title, 'author': self.author, 'year': self.year, 'status': self.status}
    #
    # def demonstration(self) -> str:
    #     return f'Книга №{self.id}. {self.author} "{self.title}" {self.year} года издания - {self.status}'