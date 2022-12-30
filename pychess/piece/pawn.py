from .piece import Piece
from .moves import Moves
from pychess.position import Position
from pychess.color import Color


class Pawn(Piece):
    first_move: bool

    def __init__(self, /, color: Color):
        super().__init__(color)
        self.first_move = True

    def movements(self) -> list[Position]:
        moves = Moves(self)
        return []
