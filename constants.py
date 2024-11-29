JSON_IDENT_DEFAULT_VALUE = 4
ENSURE_ASCII_DEFAULT_VALUE = False
PARAM_MIN_LENGTH = 1
PARAM_MAX_LENGTH = 300
STORAGE_FILE_NAME = 'storage_json.json'
EMPTY_FILE = 0
BOOK_STATUSES = ('в наличии', 'выдана')
BOOK_SEARCH_FIELDS = ('title', 'author', 'year')
YEAR_INDEX = 2
NO_BOOKS = 0
ADD_ARGUMENTS_COUNT = 3
SEARCH_ARGUMENTS_COUNT = 3
CHANGE_ARGUMENTS_COUNT = 2
BOOK_DEFAULT_STATUS = 'в наличии'
BOOK_ADDED_SUCCESSFULLY_MESSAGE = 'Книга успешно добавлена!'
BOOK_DELETED_SUCCESSFULLY_MESSAGE = 'Книга успешно удалена!'
BOOK_STATUS_CHANGED_SUCCESSFULLY = ('Статус книги успешно изменён. '
                                    'Новый статус:')
BOOK_TO_DELETE_NOT_FOUND = 'Невозможно удалить книгу с id:'
BOOK_NOT_FOUND_WITH_CURRENT_SEARCH_PARAMS = ('Не удалось найти книги по '
                                             'вашему запросу! Повторите '
                                             'попытку с другими '
                                             'параметрами поиска:')
BOOKS_ON_REQUEST = 'Книги по вашему запросу:'
FULL_CATALOG_OF_BOOKS = 'Текущий каталог книг:'
EMPTY_LIBRARY_MESSAGE = 'На данный момент в библиотеке нет добавленных книг.'
INVALID_BOOK_ID_ERROR_MESSAGE = 'Не удалось удалить книгу. Неверный book_id:'
BOOK_NOT_FOUND = 'Книга не найдена!'
STATUS_WAS_PREVIOUSLY_SET = 'Этот статус был установлен ранее!'
NEW_STATUS_MESSAGE = 'Новый статус:'
INVALID_BOOK_ID_MESSAGE = 'Некорректное значение book_id'
EMPTY_STRING_PARAM_MESSAGE = 'Параметр не может быть пустой строкой!'
NAME_OR_TITLE_TOO_LONG_MESSAGE = ('Имя автора и название книги не могут быть '
                                  'длинее 300 символов!')
YEAR_IS_NOT_INT_MESSAGE = 'Указанное значение года выпуска не является числом'
INVALID_YEAR_MESSAGE = 'Некорректное значение года выпуска.'
YEAR_FIELD_REQUIREMENTS = ('Год выпуска должен быть больше нуля и не больше '
                           'текущего года.')
INVALID_STATUS = 'Некорректный статус. Попробуйте указать один из вариантов:'
PARSER_HELP_TEXT = ('Чтобы увидеть команды для работы с библиотекой, '
                    'введите -h или --help')
ADD_BOOK_ARGUMENT_HELP_TEXT = ('Чтобы добавить книгу в библиотеку, введите '
                               'данные книги по образцу: "название" "автор" '
                               '"год выпуска"')
