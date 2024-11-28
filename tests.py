import unittest
from models import Books


class TestBooks(unittest.TestCase):
    def setUp(self):
        """Создаем экземпляр библиотеки для тестов"""
        self.books = Books()

    def test_add_valid_book(self):
        """Тестируем добавление корректной книги"""
        book = self.books.add_book("1984", "George Orwell", 1949)
        self.assertEqual(book['title'], "1984")
        self.assertEqual(book['author'], "George Orwell")
        self.assertEqual(book['year'], 1949)

    def test_remove_book(self):
        """Тестируем добавление дубликата книги"""
        self.books.remove_book(7)
        self.assertEqual(len(self.books.books), 6)

    def test_get_book(self):
        """Тестируем добавление дубликата книги"""
        book = self.books.get_book(1)
        self.assertEqual(book['title'], "колобок")

    def test_change_status(self):
        """Тестируем добавление дубликата книги"""
        book = self.books.change_status(1, 'в наличии')
        self.assertEqual(book['status'], "в наличии")


if __name__ == '__main__':
    unittest.main()