from typing import Type

from psycopg import Cursor


def get_food_by_name(cursor: Cursor, name: str) -> None:
    pass


def created_food(cursor: Cursor, name: str, price: float) -> None:
    pass


def get_food_by_id(cursor: Cursor, food_id: int) -> Type[None]:
    pass


def updated_food(cursor: Cursor, id: int, name: str, price: float) -> Type[None]:
    pass


def delete_food(cursor: Cursor, food_id: int) -> None:
    return None
