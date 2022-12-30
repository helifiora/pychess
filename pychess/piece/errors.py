from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .piece import Piece
    from pychess.position import Position


class PieceOffTheBoardError(Exception):
    piece: Piece

    def __init__(self, piece: Piece):
        super().__init__()
        self.piece = piece


class MovimentNotAllowedError(Exception):
    piece: Piece
    position: Position

    def __init__(self, piece: Piece, position: Position):
        super().__init__()
        self.piece = piece
        self.position = position
