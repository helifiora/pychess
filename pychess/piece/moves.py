from __future__ import annotations
from itertools import chain
from typing import Iterable, TYPE_CHECKING, Callable
from pychess.position import Position
from .direction import Direction

if TYPE_CHECKING:
    from .piece import Board, Piece


class Moves:
    __piece: Piece

    def __init__(self, piece: Piece):
        self.__piece = piece

    @property
    def __board(self) -> Board:
        return self.__piece.board

    def lshape(self) -> Iterable[Position]:
        origin = self.__piece.position
        increments = [
            Position(-2, -1), Position(-2, 1), Position(-1, -2), Position(-1, 2),
            Position(1, -2), Position(1, 2), Position(2, -1), Position(2, 1),
        ]

        return self.__board.iterate_values(origin, increments)

    def horizontal(self, *, take: int | None = None) -> Iterable[Position]:
        origin = self.__piece.position
        left = self.__board.iterate(origin, Position(-1, 0), take=take)
        right = self.__board.iterate(origin, Position(1, 0), take=take)
        return chain(left, right)

    def vertical(
            self, *,
            direction: Direction | None = None,
            take: int | None = None,
            accept: Callable[[Piece | None], bool] | None = None
    ) -> Iterable[Position]:
        origin = self.__piece.position
        match direction:
            case None:
                top = self.__board.iterate(origin, Position(0, -1), take=take, accept=accept)
                bottom = self.__board.iterate(origin, Position(0, 1), take=take, accept=accept)
                return chain(top, bottom)
            case Direction.TOP:
                return self.__board.iterate(origin, Position(0, -1), take=take, accept=accept)
            case Direction.BOTTOM:
                return self.__board.iterate(origin, Position(0, 1), take=take, accept=accept)

    def diagonal(
            self, *,
            direction: Direction | None = None,
            take: int | None = None,
            accept: Callable[[Piece | None], bool] | None = None
    ) -> Iterable[Position]:
        origin = self.__piece.position
        match direction:
            case None:
                left_top = self.__board.iterate(origin, Position(-1, -1), take=take, accept=accept)
                left_bottom = self.__board.iterate(origin, Position(-1, 1), take=take, accept=accept)
                right_top = self.__board.iterate(origin, Position(1, -1), take=take, accept=accept)
                right_bottom = self.__board.iterate(origin, Position(1, 1), take=take, accept=accept)
                return chain(left_top, left_bottom, right_top, right_bottom)
            case Direction.TOP:
                left_top = self.__board.iterate(origin, Position(-1, -1), take=take, accept=accept)
                right_top = self.__board.iterate(origin, Position(1, -1), take=take, accept=accept)
                return chain(left_top, right_top)
            case Direction.BOTTOM:
                left_bottom = self.__board.iterate(origin, Position(-1, 1), take=take, accept=accept)
                right_bottom = self.__board.iterate(origin, Position(1, 1), take=take, accept=accept)
                return chain(left_bottom, right_bottom)
