from pychess.position import Position

from .piece import Piece
from .moves import Moves


class Rook(Piece):

    def movements(self) -> list[Position]:
        return list(Moves(self).lmove())
