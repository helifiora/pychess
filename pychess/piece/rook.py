from pychess.position import Position
from itertools import chain
from .piece import Piece


class Rook(Piece):

    def movements(self) -> list[Position]:
        horizontal = self._moves.horizontal()
        vertical = self._moves.vertical()
        return list(chain(horizontal, vertical))
