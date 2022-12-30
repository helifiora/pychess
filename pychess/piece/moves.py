from __future__ import annotations
from itertools import chain
from typing import Iterator, TYPE_CHECKING
from pychess.position import Position

if TYPE_CHECKING:
    from .piece import Board, Piece


class Moves:
    __piece: Piece

    def __init__(self, piece: Piece):
        self.__piece = piece

    @property
    def __board(self) -> Board:
        return self.__piece.board

    def lshape(self) -> Iterator[Position]:
        origin = self.__piece.position
        increments = [
            Position(-2, -1), Position(-2, 1), Position(-1, -2), Position(-1, 2),
            Position(1, -2), Position(1, 2), Position(2, -1), Position(2, 1),
        ]

        return self.__board.iterate_values(origin, increments)

    def horizontal(self, *, take: int | None = None) -> Iterator[Position]:
        origin = self.__piece.position
        left = self.__board.iterate(origin, Position(-1, 0), take=take)
        right = self.__board.iterate(origin, Position(1, 0), take=take)
        return chain(left, right)

    def vertical(self, *, take: int | None = None) -> Iterator[Position]:
        origin = self.__piece.position
        top = self.__board.iterate(origin, Position(0, -1), take=take)
        bottom = self.__board.iterate(origin, Position(0, 1), take=take)
        return chain(top, bottom)

    def diagonal(self, *, take: int | None = None) -> Iterator[Position]:
        origin = self.__piece.position
        left_top = self.__board.iterate(origin, Position(-1, -1), take=take)
        left_bottom = self.__board.iterate(origin, Position(-1, 1), take=take)
        right_top = self.__board.iterate(origin, Position(1, -1), take=take)
        right_bottom = self.__board.iterate(origin, Position(1, 1), take=take)
        return chain(left_top, left_bottom, right_top, right_bottom)
