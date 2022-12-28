from pychess.position import Position

from .moves import Moves
from .piece import Piece, Board


class Knight(Piece):

    def movements(self) -> list[Position]:
        return list(Moves(self).lmove())
