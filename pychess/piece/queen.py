from .piece import Piece
from pychess.position import Position
from itertools import chain
from typing import Iterable


class Queen(Piece):

    def movements(self) -> Iterable[Position]:
        return chain(self._moves.diagonal(), self._moves.vertical(), self._moves.horizontal())
