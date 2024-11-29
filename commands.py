import argparse

import constants as const
from library import Library
from library_interface import LibraryInterface
from services import create_storage_if_not_exists


class LibraryCommands(LibraryInterface):

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            f'{const.PARSER_HELP_TEXT}',
            formatter_class=argparse.RawTextHelpFormatter
        )
        self.library = Library()

    def start(self):
        """Add all arguments to argparser, parse them and process them."""
        create_storage_if_not_exists()
        self.add()
        self.delete()
        self.search()
        self.get()
        self.change()
        args = self.parser.parse_args()
        self.process_commands(vars(args))

    def process_commands(self, args):
        """Filters arguments and prepares them for execution."""
        for arg_name, input_data in args.items():
            if input_data is not None and input_data is not False:
                self.run_command_if_it_received(arg_name, input_data)

    def run_command_if_it_received(self, arg_name, input_data):
        """Run command the command if it is received."""
        switch = {
            'add': self.add_book,
            'delete': self.delete_book,
            'search': self.search_book,
            'get': self.get_books,
            'change': self.change_book_status,
        }
        switch.get(arg_name, self.unknown_command)(input_data)

    def add(self):
        self.parser.add_argument(
            '-a', '--add', nargs=const.ADD_ARGUMENTS_COUNT,
            help=f'{const.ADD_BOOK_ARGUMENT_HELP_TEXT}'
        )

    def delete(self):
        self.parser.add_argument('-d', '--delete', type=int)

    def search(self):
        self.parser.add_argument(
            '-s', '--search',
            nargs=const.SEARCH_ARGUMENTS_COUNT, type=str
        )

    def get(self):
        self.parser.add_argument('-g', '--get', action='store_true')

    def change(self):
        self.parser.add_argument(
            '-ch', '--change', type=str,
            nargs=const.CHANGE_ARGUMENTS_COUNT,
        )

    def unknown_command(self, input_data):
        print('Unknown command')

    def add_book(self, input_data):
        self.library.add_book(input_data)

    def delete_book(self, input_data):
        self.library.delete_book(input_data)

    def search_book(self, input_data):
        self.library.search_book(input_data)

    def get_books(self, input_data):
        self.library.get_books()

    def change_book_status(self, input_data):
        self.library.change_book_status(input_data)
