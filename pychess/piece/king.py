from itertools import chain
from pychess.position import Position
from .piece import Piece
from .moves import Moves


class King(Piece):

    def movements(self) -> list[Position]:
        moves = Moves(self)
        return list(chain(
            moves.horizontal(take=1),
            moves.vertical(take=1),
            moves.diagonal(take=1)
        ))
