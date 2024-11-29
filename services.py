import json

import constants as const


def create_storage_if_not_exists(
        storage_file_name: str = const.STORAGE_FILE_NAME
) -> None:
    with open(file=storage_file_name, mode='a'):
        pass


def get_books_from_storage(
        storage_file_name: str = const.STORAGE_FILE_NAME,
        return_json: bool = False, return_dict: bool = False
) -> dict[int, str | int] | list[dict[str, str | int]]:
    """Get all books from storage and return them in chosen format."""
    with open(file=storage_file_name, mode='r', encoding='utf-8') as storage:
        try:
            books = json.loads(storage.read())
            if return_json:
                try:
                    books = list(books.values())
                except:
                    books = []
                return dumps_data_to_json_with_base_formatting(books)
        except json.JSONDecodeError:
            if return_json:
                books = []
            else:
                books = {}
        if return_dict:
            return books
        if books:
            return books.values()
        return books


def put_books_to_storage(
        books: dict[int, str | int] | list[dict[str, str | int]],
        storage_file_name: str = const.STORAGE_FILE_NAME
) -> None:
    """Add all books to storage by overwriting the file."""
    with open(file=storage_file_name, mode='w', encoding='utf-8') as storage:
        storage.write(dumps_data_to_json_with_base_formatting(books))


def dumps_data_to_json_with_base_formatting(data: list | dict):
    """Dumps data to json."""
    return (json.dumps(
         data, indent=const.JSON_IDENT_DEFAULT_VALUE,
         ensure_ascii=const.ENSURE_ASCII_DEFAULT_VALUE)
    )


def get_books_filtered_by_search_params(
    books: dict[str, int | str], search_params: list[str | int | None]
) -> list[str]:
    books_for_response = []
    for book in books:
        is_append: bool = is_append_book_to_response(book, search_params)
        if is_append:
            books_for_response.append(book)
    return books_for_response


def is_append_book_to_response(
        book: dict[str, str | int], search_params: list[str | int | None]
) -> bool:
    """Determine whether to add a book to the response."""
    is_append: bool = True
    title, author, year = search_params
    search_params_dict = {
        'title': title,
        'author': author,
        'year': year
    }
    for search_field_name, search_param in search_params_dict.items():
        if search_param is None:
            continue
        if search_param == book[search_field_name]:
            is_append = True
        else:
            is_append = False
            break
    return is_append
