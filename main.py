from models import Books


def main():

    print('Вас приветствует консольное приложение для управления библиотекой '
          'книг\nЧто вы хотите сделать?')
    print("0 - Добавить книгу, 1 - удалить книгу, 2 - найти книгу, "
          "3 - посмотреть список книг, 4 - изменить статус книги\nВведите код: ")

    command = input()
    select_action(command)


def select_action(command):
    books = Books()
    if command.isdigit():
        command = int(command)
        match command:
            case 0:
                print('Введите название книги для добавления')
                title: str = input().lower()
                print('Введите автора книги')
                author: str = input().lower()
                print('Введите год издания книги (число) ')
                year = int(input())
                try:
                    new_book = books.add_book(title, author, year)
                    if new_book:
                        print(f'Книга "{title}" успешно добавлена.')
                    else:
                        print(f'Книга "{title}" не была добавлена')
                except Exception as e:
                    print(f'Произошла ошибка при добавлении книги: {e}')
            case 1:
                print('Введите id книги для удаления')
                book_id: str or int = input()
                if book_id.isdigit():
                    book_id = int(book_id)
                    try:
                        books.remove_book(book_id)
                    except Exception as e:
                        print(f'Произошла ошибка при удалении книги: {e}')
                else:
                    print('Id книги указан неверно, введите число, например, 34')
            case 2:
                print('Введите один из параметров книги для поиска: '
                      'название, автора, год издания')
                param: str = input().lower()
                book = books.get_book(param)
                if book:
                    print(book)
                else:
                    print(f"Книга с {param} не найдена.")
            case 3:
                print(books.get_books())
            case 4:
                print('Введите id книги для измнения статуса')
                book_id = int(input())
                print('Введите статус - в наличии/выдана/утеряна')
                status: str = input().lower()
                books.change_status(book_id, status)
    else:
        print("Такой команды нет. Попробуйте еще раз")




if __name__ == '__main__':
    main()
