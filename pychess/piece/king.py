from itertools import chain
from pychess.position import Position
from .piece import Piece
from .color import Color
from typing import Iterable, Callable
from functools import reduce


class King(Piece):

    def movements(self) -> Iterable[Position]:
        enemy_movements = self.__enemy_movements()
        horizontal = self._moves.horizontal(take=1, accept=self.__accept(enemy_movements))
        vertical = self._moves.vertical(take=1, accept=self.__accept(enemy_movements))
        diagonal = self._moves.diagonal(take=1, accept=self.__accept(enemy_movements))
        return chain(horizontal, vertical, diagonal)

    def __enemy_movements(self) -> set[Position]:
        enemy_color = Color.WHITE if self.color == Color.BLACK else Color.BLACK
        enemies = self.board.get_pieces(enemy_color)
        return reduce(self.__join, enemies, set())

    def __accept(self, enemies_possible_movements: set[Position]) -> Callable[[Piece | None], bool]:
        def accept(piece: Piece | None, position: Position) -> bool:
            if position in enemies_possible_movements:
                return False

            return piece is None or piece.color != self.color

        return accept

    @staticmethod
    def __join(positions: set[Position], piece: Piece) -> set[Position]:
        return positions.union(piece.movements())
