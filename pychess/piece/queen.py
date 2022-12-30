from .piece import Piece
from .moves import Moves
from pychess.position import Position
from itertools import chain


class Queen(Piece):

    def movements(self) -> list[Position]:
        return list(chain(self._moves.diagonal(), self._moves.vertical(), self._moves.horizontal()))
