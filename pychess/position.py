from copy import copy
from typing import Self

from pychess.entry import ENTRY_COLUMN_VALUE, ENTRY_ROW_VALUE


class Position:
    __slots__ = ['x', 'y']

    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __lt__(self, other: 'Position') -> bool:
        if not isinstance(other, Position):
            return False

        if self.y < other.y:
            return True

        if self.y > other.y:
            return False

        if self.x < other.x:
            return True

    @classmethod
    def from_entry(cls, entry_row: str, entry_column: str) -> Self:
        """
        :param entry_row: '1', '2', '3', '4', '5', '6', '7', '8'
        :param entry_column: 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
        :return: Position
        """

        try:
            column = ENTRY_COLUMN_VALUE[entry_column]
            row = ENTRY_ROW_VALUE[entry_row]
            return cls(column, row)
        except Exception:
            raise ValueError('Erro ao criar position')

    def clone(self) -> Self:
        return copy(self)

    @property
    def inside_board(self) -> bool:
        return 0 <= self.x <= 7 and 0 <= self.y <= 7

    def __eq__(self, other: any) -> bool:
        return isinstance(other, Position) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __add__(self, other: 'Position') -> Self:
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Position') -> Self:
        return Position(self.x - other.x, self.y - other.y)

    def __iadd__(self, other: 'Position') -> Self:
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other: 'Position') -> Self:
        self.x -= other.x
        self.y -= other.y
        return self

    def __repr__(self) -> str:
        return f'Position[x: {self.x}, y: {self.y}]'
