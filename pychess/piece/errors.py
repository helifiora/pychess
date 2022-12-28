from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .piece import Piece


class PieceOffTheBoardError(Exception):
    __piece: Piece

    def __init__(self, piece: Piece) -> None:
        super().__init__()
        self.__piece = piece
