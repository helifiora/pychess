from __future__ import annotations

from typing import Self, Iterator, Callable
from pychess.piece import Piece, King
from pychess.position import Position
from pychess.color import Color
from copy import deepcopy

Table = list[list[Piece | None]]
PiecePosition = dict[Piece, Position]

AcceptFn = Callable[[Piece | None, Position], bool]
StopFn = Callable[[Piece | None], bool]


class Board:
    __table: Table
    __piece_position: PiecePosition

    def __init__(self, table: Table, pieces: PiecePosition):
        self.__table = table
        self.__piece_position = pieces

    @classmethod
    def empty(cls) -> Self:
        table: Table = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

        return cls(table, dict())

    def get_piece(self, position: Position) -> Piece | None:
        return self.__table[position.y][position.x]

    def get_piece_position(self, piece: Piece) -> Position | None:
        return self.__piece_position.get(piece, None)

    def get_king(self, color: Color) -> Piece:
        king = [
            piece
            for piece in self.__piece_position.keys()
            if piece.color == color and isinstance(piece, King)
        ]

        if len(king) != 1:
            raise Exception(f"Erro, {len(king)}")

        return king[0]

    def get_pieces(self, color: Color) -> list[Piece]:
        return [piece for piece in self.__piece_position.keys() if piece.color == color]

    def place(self, piece: Piece, position: Position) -> None:
        if (existing_piece := self.get_piece(position)) is not None:
            self.__piece_position.pop(existing_piece)
            existing_piece.board = None

        if (piece_old_position := self.get_piece_position(piece)) is not None:
            self.__table[piece_old_position.y][piece_old_position.x] = None

        self.__table[position.y][position.x] = piece
        self.__piece_position[piece] = position

        if not piece.onboard or piece.board != self:
            piece.board = self

    def viterator(
        self,
        /,
        origin: Position,
        positions: list[Position],
        *,
        accept: AcceptFn | None = None,
    ) -> Iterator[Position]:
        origin_piece = self.get_piece(origin)

        def map_fn(increment: Position) -> Position:
            return origin + increment

        def filter_fn(current: Position) -> bool:
            if not current.inside_board:
                return False

            current_position = self.get_piece(current)
            if accept is not None:
                return accept(current_position, current)

            if origin_piece is None or current_position is None:
                return True

            return origin_piece.color != current_position.color

        mapped = map(map_fn, positions)
        return filter(filter_fn, mapped)

    def iterator(
        self,
        /,
        origin: Position,
        increment: Callable[[Position], Position],
        *,
        take: int | None = None,
        accept: AcceptFn | None = None,
    ) -> Iterator[Position]:
        return BoardIterator(self, origin, increment, take, accept)

    def clone(self) -> Board:
        return deepcopy(self)


class BoardIterator:
    __board: Board
    __current: Position
    __origin: Position
    __increment_fn: Callable[[Position], Position]
    __take: int | None = None
    __accept_fn: AcceptFn | None
    __iterations: int
    __is_stopped: bool

    def __init__(
        self,
        board: Board,
        origin: Position,
        increment_fn: Callable[[Position], Position],
        take: int | None = None,
        accept_fn: AcceptFn | None = None,
    ) -> None:
        self.__board = board
        self.__current = origin.clone()
        self.__origin = origin
        self.__increment_fn = increment_fn
        self.__take = take
        self.__accept_fn = accept_fn
        self.__iterations = 1
        self.__is_stopped = False

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Position:
        if self.__is_stopped or not self.__can_take:
            raise StopIteration

        self.__increment()

        if not self.__current.inside_board or not self.__can_accept:
            raise StopIteration

        if self.__can_stop:
            self.__is_stopped = True

        return self.__current.clone()

    @property
    def __current_piece(self) -> Piece | None:
        return self.__board.get_piece(self.__current)

    @property
    def __origin_piece(self) -> Piece | None:
        return self.__board.get_piece(self.__origin)

    @property
    def __can_take(self) -> bool:
        return self.__take is None or self.__iterations <= self.__take

    @property
    def __can_accept(self) -> bool:
        if self.__accept_fn is not None:
            return self.__accept_fn(self.__current_piece, self.__current)

        if self.__current_piece is None or self.__origin_piece is None:
            return True

        return self.__current_piece.color != self.__origin_piece.color

    @property
    def __can_stop(self) -> bool:
        return self.__current_piece is not None

    def __increment(self) -> None:
        self.__current = self.__increment_fn(self.__current)
        self.__iterations += 1
