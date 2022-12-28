from pychess.position import Position

from .piece import Piece
from .moves import Moves


class Bishop(Piece):

    def movements(self) -> list[Position]:
        moves = Moves(self)
        return list(moves.diagonal())
