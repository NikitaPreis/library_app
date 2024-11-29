from dataclasses import asdict, dataclass
from uuid import uuid4

import constants as const
from services import dumps_data_to_json_with_base_formatting


@dataclass
class Book:
    title: str
    author: str
    year: int
    status: str = const.BOOK_DEFAULT_STATUS
    book_id: int = int(uuid4())

    def get_book_dict(self) -> dict:
        return asdict(self)

    def dumps_book_to_json(self):
        return dumps_data_to_json_with_base_formatting(self.get_book_dict())
