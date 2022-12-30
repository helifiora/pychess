from pychess.position import Position
from typing import Iterable

from .piece import Piece


class Bishop(Piece):

    def movements(self) -> Iterable[Position]:
        return self._moves.diagonal()
