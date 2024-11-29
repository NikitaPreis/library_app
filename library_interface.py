from abc import ABC, abstractmethod


class LibraryInterface(ABC):

    @abstractmethod
    def add_book(self, *args, **kwargs):
        pass

    @abstractmethod
    def search_book(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_books(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_book(self, *args, **kwargs):
        pass

    @abstractmethod
    def change_book_status(self, *args, **kwargs):
        pass
