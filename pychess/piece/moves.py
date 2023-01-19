from __future__ import annotations
from itertools import chain
from typing import Iterable, TYPE_CHECKING, Callable, Iterator
from pychess.position import Position
from .direction import Direction
from functools import partial

if TYPE_CHECKING:
    from .piece import Board, Piece


class Moves:
    __piece: Piece

    def __init__(self, piece: Piece):
        self.__piece = piece

    @property
    def __board(self) -> Board:
        return self.__piece.board

    @staticmethod
    def inc(x: int, y: int) -> Callable[[Position], Position]:
        increment = Position(x, y)

        def wrap(entry: Position) -> Position:
            return entry + increment

        return wrap

    def lshape(self) -> Iterator[Position]:
        origin = self.__piece.position

        return self.__board.viterator(
            origin,
            [
                Position(-2, -1),
                Position(-2, 1),
                Position(-1, -2),
                Position(-1, 2),
                Position(1, -2),
                Position(1, 2),
                Position(2, -1),
                Position(2, 1),
            ],
        )

    def horizontal(
        self,
        *,
        take: int | None = None,
        accept: Callable[[Piece | None, Position], bool] | None = None,
    ) -> Iterable[Position]:
        origin = self.__piece.position
        left = self.__board.iterator(origin, self.inc(-1, 0), take=take, accept=accept)
        right = self.__board.iterator(origin, self.inc(1, 0), take=take, accept=accept)
        return chain(left, right)

    def vertical(
        self,
        *,
        direction: Direction | None = None,
        take: int | None = None,
        accept: Callable[[Piece | None, Position], bool] | None = None,
    ) -> Iterable[Position]:
        origin = self.__piece.position
        iterator = partial(self.__board.iterator, origin, take=take, accept=accept)
        match direction:
            case None:
                top = iterator(self.inc(0, -1))
                bottom = iterator(self.inc(0, 1))
                return chain(top, bottom)
            case Direction.TOP:
                return iterator(self.inc(0, -1))
            case Direction.BOTTOM:
                return iterator(self.inc(0, 1))

    def diagonal(
        self,
        *,
        direction: Direction | None = None,
        take: int | None = None,
        accept: Callable[[Piece | None, Position], bool] | None = None,
    ) -> Iterable[Position]:
        origin = self.__piece.position
        iterator = partial(self.__board.iterator, origin, take=take, accept=accept)
        match direction:
            case None:
                left_top = iterator(self.inc(-1, -1))
                left_bottom = iterator(self.inc(-1, 1))
                right_top = iterator(self.inc(1, -1))
                right_bottom = iterator(self.inc(1, 1))
                return chain(left_top, left_bottom, right_top, right_bottom)
            case Direction.TOP:
                left_top = iterator(self.inc(-1, -1))
                right_top = iterator(self.inc(1, -1))
                return chain(left_top, right_top)
            case Direction.BOTTOM:
                left_bottom = iterator(self.inc(-1, 1))
                right_bottom = iterator(self.inc(1, 1))
                return chain(left_bottom, right_bottom)
