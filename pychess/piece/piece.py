from __future__ import annotations
from abc import abstractmethod, ABC
from typing import Protocol, Callable, Iterable
from pychess.piece.color import Color
from pychess.position import Position
from .moves import Moves
from .errors import PieceOffTheBoardError, MovimentNotAllowedError


class Board(Protocol):

    @abstractmethod
    def place(self, piece: Piece, position: Position) -> None:
        ...

    @abstractmethod
    def get_piece(self, position: Position) -> Piece | None:
        ...

    @abstractmethod
    def get_piece_position(self, piece: Piece) -> Position | None:
        ...

    @abstractmethod
    def iterate_values(
            self,
            /, origin: Position, positions: list[Position],
            *, accept: Callable[[Piece | None], bool] | None = None
    ) -> Iterable[Position | None]:
        ...

    @abstractmethod
    def iterate(
            self,
            /, origin: Position, increment: Position,
            *, accept: Callable[[Piece | None], bool] | None = None, stop: Callable[[Piece | None], bool] | None = None,
            take: int | None = None
    ) -> Iterable[Position | None]:
        ...


class Piece(ABC):
    __board: Board | None
    __color: Color
    _moves: Moves

    def __init__(self, /, color: Color):
        self.__color = color
        self.__board = None
        self._moves = Moves(self)

    @property
    def board(self) -> Board:
        return self.__board

    @board.setter
    def board(self, value: Board | None) -> None:
        self.__board = value

    @property
    def color(self) -> Color:
        return self.__color

    @property
    def position(self) -> Position:
        """
        :raise: PieceOffTheBoardError
        :return:
        """
        if self.__board is None:
            raise PieceOffTheBoardError(self)

        return self.__board.get_piece_position(self)

    @property
    def onboard(self) -> bool:
        return self.__board is not None

    def move(self, position: Position) -> None:
        if position not in set(self.movements()):
            raise MovimentNotAllowedError(self, position)

        self.board.place(self, position)

    @abstractmethod
    def movements(self) -> Iterable[Position]:
        ...
