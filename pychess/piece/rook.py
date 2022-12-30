from pychess.position import Position
from itertools import chain
from .piece import Piece
from typing import Iterable


class Rook(Piece):

    def movements(self) -> Iterable[Position]:
        horizontal = self._moves.horizontal()
        vertical = self._moves.vertical()
        return chain(horizontal, vertical)
