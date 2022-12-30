from typing import Self, Iterator, Callable
from pychess.piece import Piece
from pychess.position import Position

Table = list[list[Piece | None]]
PiecePosition = dict[Piece, Position]

AcceptFn = Callable[[Piece | None], bool]
StopFn = Callable[[Piece | None], bool]


class Board:
    __table: Table
    __piece_position: PiecePosition

    def __init__(self, table: Table, pieces: PiecePosition):
        self.__table = table
        self.__piece_position = pieces

    @classmethod
    def empty(cls) -> Self:
        table = [
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

    def place(self, piece: Piece, position: Position) -> None:
        if (existing_piece := self.get_piece(position)) is not None:
            self.__piece_position.pop(existing_piece)
            existing_piece.board = None

        if (piece_old_position := self.get_piece_position(piece)) is not None:
            self.__table[piece_old_position.y][piece_old_position.x] = None

        self.__table[position.y][position.x] = piece
        self.__piece_position[piece] = position

        if piece.board != self:
            piece.board = self

    def iterate_values(
            self,
            /, origin: Position, positions: list[Position],
            *, accept: AcceptFn | None = None
    ) -> Iterator[Position | None]:
        origin_piece = self.get_piece(origin)

        def map_fn(increment: Position) -> Position:
            return origin + increment

        def filter_fn(position: Position) -> bool:
            if not position.inside_board:
                return False

            target = self.get_piece(position)
            return self.__can_accept(origin_piece, target, accept)

        mapped = map(map_fn, positions)
        return filter(filter_fn, mapped)

    def iterate(
            self,
            /, origin: Position, increment: Position,
            *, accept: AcceptFn | None = None, stop: StopFn | None = None, take: int | None = None
    ) -> Iterator[Position | None]:

        cells = 1
        origin_piece = self.get_piece(origin)
        current = origin + increment

        while current.inside_board and self.__can_take(cells, take):
            target = self.get_piece(current)

            if self.__can_accept(origin_piece, target, accept):
                yield current.clone()

            if self.__can_stop(target, stop):
                break

            cells += 1
            current += increment

    @staticmethod
    def __can_accept(origin: Piece | None, target: Piece | None, accept: AcceptFn) -> bool:
        if accept is not None:
            return accept(target)

        if target is None:
            return True

        if origin is None:
            return True

        return origin.color != target.color

    @staticmethod
    def __can_take(count: int, limit: int | None) -> bool:
        return limit is None or count <= limit

    @staticmethod
    def __can_stop(target: Position | None, stop: StopFn | None) -> bool:
        if stop is not None:
            return stop(target)

        return target is not None
