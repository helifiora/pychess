from typing import Self
from pychess.piece import Piece
from pychess.position import Position

Table = list[list[Piece | None]]
PiecePosition = dict[Piece, Position]


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
