import datetime as dt

import constants as const


def validate_book_id(book_id: int) -> int | bool:
    try:
        book_id = int(book_id)
    except ValueError:
        print(f'{const.INVALID_BOOK_ID_MESSAGE}: {book_id}')
        return False
    return book_id


def validate_field_length(filed_name: str, param: str)  -> str | bool:
    if len(param) < const.PARAM_MIN_LENGTH:
        print(f'{const.EMPTY_STRING_PARAM_MESSAGE}: {filed_name}')
        return False
    if len(param) > const.PARAM_MAX_LENGTH:
        print(f'{const.NAME_OR_TITLE_TOO_LONG_MESSAGE}: {filed_name}')
        return False
    return param


def validate_book_title(title: str) -> str | bool:
    return validate_field_length(filed_name='Название', param=title)


def validate_book_author(author: str) -> str | bool:
    return validate_field_length(filed_name='Имя автора', param=author)


def validate_book_year(year: int | str) -> int | bool:
    try:
        year = int(year)
    except ValueError:
        print(f'{const.YEAR_IS_NOT_INT_MESSAGE}: {year}.')
        return False
    current_year = dt.datetime.now().year
    if 0 <= year <= current_year:
        return year
    print(f'''{const.INVALID_YEAR_MESSAGE}: {year}.
          {const.YEAR_FIELD_REQUIREMENTS}''')
    return False


def validate_writable_fields_of_book(
        title: str, author: str, year: str | int
) -> tuple[str | bool, str | bool, int | bool] | bool:
    data = title, author, year
    for value in data:
        if not (isinstance(value, str) or isinstance(value, int)):
            return False
    validated_data = (validate_book_title(title),
                      validate_book_author(author),
                      validate_book_year(year))
    for value in validated_data:
        if not value:
            return False
    return validated_data


def validate_book_status(new_book_status: str) -> str | bool:
    if new_book_status not in const.BOOK_STATUSES:
        print(f'{const.INVALID_STATUS} {const.BOOK_STATUSES}')
        return False
    return new_book_status


def validate_change_book_status(book_id: int,
                                new_book_status: str) -> bool:
    if not (validate_book_id(book_id)
            and validate_book_status(new_book_status)):
        return False
    return True
