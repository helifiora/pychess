from pychess.position import Position

from .piece import Piece


class Knight(Piece):

    def movements(self) -> list[Position]:
        return list(self._moves.lshape())
