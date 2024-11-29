import constants as const
from book import Book
from library_interface import LibraryInterface
from services import (dumps_data_to_json_with_base_formatting,
                      get_books_filtered_by_search_params,
                      get_books_from_storage, put_books_to_storage)
from validators import (validate_book_id, validate_change_book_status,
                        validate_writable_fields_of_book)


class Library(LibraryInterface):

    def add_book(self, input_data):
        """Add a book to storage."""
        validated_data = validate_writable_fields_of_book(*input_data)
        if not validated_data:
            return None
        title, author, year = validated_data
        book = Book(title=title, author=author, year=year).get_book_dict()
        books = get_books_from_storage(return_dict=True)
        books[book['book_id']] = book
        put_books_to_storage(books)
        print(const.BOOK_ADDED_SUCCESSFULLY_MESSAGE)

    def search_book(self, input_data):
        """Select books in the storage according to the specified params."""
        try:
            year = int(input_data[const.YEAR_INDEX])
        except ValueError:
            year = '-'
        input_data[const.YEAR_INDEX] = year
        search_params = [param if param != '-' else None
                         for param in input_data]
        books = get_books_from_storage()
        books_to_response = dumps_data_to_json_with_base_formatting(
            get_books_filtered_by_search_params(
                books, search_params
            )
        )
        if len(books) == const.NO_BOOKS:
            print(f'{const.BOOK_NOT_FOUND_WITH_CURRENT_SEARCH_PARAMS} '
                  f'{search_params}')
            return None
        print(f'{const.BOOKS_ON_REQUEST}\n')
        print(f'{books_to_response}')

    def get_books(self):
        """Get all books from storage."""
        books = get_books_from_storage(return_json=True)
        if len(books) == const.NO_BOOKS:
            print(f'{const.EMPTY_LIBRARY_MESSAGE}')
            return False
        print(f'{const.FULL_CATALOG_OF_BOOKS}\n')
        print(books)

    def delete_book(self, book_id):
        """Delete a book from storage."""
        book_id = str(book_id)
        if not validate_book_id(book_id):
            return None
        books = get_books_from_storage(return_dict=True)
        deleted_book = books.pop(book_id, False)
        if not deleted_book:
            print(f'{const.INVALID_BOOK_ID_ERROR_MESSAGE} {book_id}')
            return None
        put_books_to_storage(books)
        print(f'{const.BOOK_DELETED_SUCCESSFULLY_MESSAGE}')
        print(f'Удаленная книга:\n{deleted_book}')

    def change_book_status(self, input_data):
        """Change a book status."""
        book_id, new_book_status = input_data
        new_book_status = new_book_status.rstrip().lower()
        if not validate_change_book_status(book_id, new_book_status):
            return None
        books = get_books_from_storage(return_dict=True)
        book = books.get(book_id, None)
        if book is None:
            print(f'{const.BOOK_NOT_FOUND}')
            return None
        old_status = book.get('status')
        if new_book_status == old_status:
            print(f'{const.STATUS_WAS_PREVIOUSLY_SET}: "{new_book_status}"')
            return None
        books[book_id]['status'] = new_book_status
        put_books_to_storage(books)
        print(f'{const.BOOK_STATUS_CHANGED_SUCCESSFULLY}')
        print(f'{const.NEW_STATUS_MESSAGE}: "{new_book_status}"')
