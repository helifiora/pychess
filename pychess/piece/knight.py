from pychess.position import Position
from typing import Iterable

from .piece import Piece


class Knight(Piece):

    def movements(self) -> Iterable[Position]:
        return self._moves.lshape()
