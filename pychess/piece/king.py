from itertools import chain
from pychess.position import Position
from .piece import Piece
from typing import Iterable


class King(Piece):

    def movements(self) -> Iterable[Position]:
        horizontal = self._moves.horizontal(take=1)
        vertical = self._moves.vertical(take=1)
        diagonal = self._moves.diagonal(take=1)
        return chain(horizontal, vertical, diagonal)
