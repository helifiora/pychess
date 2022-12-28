from itertools import chain
from typing import Iterable
from pychess.position import Position

from .piece import Board, Piece


class Moves:
    __piece: Piece
    __board: Board

    def __init__(self, piece: Piece):
        self.__board = piece.board
        self.__piece = piece

    def lmove(self) -> Iterable[Position]:
        origin = self.__piece.position.clone()

        increments = [
            Position(-2, -1), Position(-2, 1),
            Position(-1, -2), Position(-1, 2),
            Position(1, -2), Position(1, 2),
            Position(2, -1), Position(2, 1),
        ]

        def map_to_positions(increment: Position) -> Position:
            return origin + increment

        def filter_valid_positions(position: Position) -> bool:
            if not position.is_inside_board:
                return False

            target = self.__board.get_piece(position)
            return target is None or target.color != self.__piece.color

        mapping = map(map_to_positions, increments)
        return filter(filter_valid_positions, mapping)

    def horizontal(self) -> Iterable[Position]:
        left = self.__iterable(Position(-1, 0))
        right = self.__iterable(Position(1, 0))
        return chain(left, right)

    def vertical(self) -> Iterable[Position]:
        top = self.__iterable(Position(0, -1))
        bottom = self.__iterable(Position(0, 1))
        return chain(top, bottom)

    def diagonal(self) -> Iterable[Position]:
        left_top = self.__iterable(Position(-1, -1))
        left_bottom = self.__iterable(Position(-1, 1))
        right_top = self.__iterable(Position(1, -1))
        right_bottom = self.__iterable(Position(1, 1))
        return chain(left_top, left_bottom, right_top, right_bottom)

    def __iterable(self, increment: Position) -> Iterable[Position]:

        position = self.__piece.position.clone() + increment
        while position.is_inside_board:

            target = self.__board.get_piece(position)
            if target is None or target.color != self.__piece.color:
                yield position.clone()

            if target is not None:
                break

            position += increment
