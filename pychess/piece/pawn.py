from typing import Iterable
from itertools import chain
from .piece import Piece
from .direction import Direction
from pychess.position import Position
from pychess.piece.color import Color


class Pawn(Piece):
    first_move: bool

    def __init__(self, /, color: Color):
        super().__init__(color)
        self.first_move = True

    def move(self, position: Position) -> None:
        super().move(position)
        if self.first_move:
            self.first_move = False

    def movements(self) -> Iterable[Position]:
        take = 2 if self.first_move else 1
        direction = Direction.BOTTOM if self.color == Color.BLACK else Direction.TOP

        vertical = self._moves.vertical(direction=direction, take=take)
        diagonal = self._moves.diagonal(direction=direction, take=1, accept=self.__accept)

        return chain(vertical, diagonal)

    def __accept(self, target: Piece | None, _: Position) -> bool:
        return target is not None and target.color != self.color
