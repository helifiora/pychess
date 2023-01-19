from __future__ import annotations
from abc import abstractmethod, ABC
from typing import Iterator, Protocol, Callable, Iterable
from pychess.color import Color
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
    def get_pieces(self, color: Color) -> list[Piece]:
        ...

    @abstractmethod
    def get_piece_position(self, piece: Piece) -> Position | None:
        ...

    @abstractmethod
    def viterator(
        self,
        /,
        origin: Position,
        positions: list[Position],
        *,
        accept: Callable[[Piece | None, Position], bool] | None = None,
    ) -> Iterator[Position]:
        ...

    @abstractmethod
    def iterator(
        self,
        /,
        origin: Position,
        increment: Callable[[Position], Position],
        *,
        take: int | None = None,
        accept: Callable[[Piece | None, Position], bool] | None = None,
    ) -> Iterator[Position]:
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
        """
        Get the current board of the piece
        :raises PieceOffTheBoardError
        :return: Board
        """
        if self.__board is None:
            raise PieceOffTheBoardError(self)

        return self.__board

    @board.setter
    def board(self, value: Board | None) -> None:
        """
        Define the board to the piece
        :param value: a Board or None
        """
        self.__board = value

    @property
    def color(self) -> Color:
        """
        Get the color of the piece
        :return: Color
        """
        return self.__color

    @property
    def position(self) -> Position:
        """
        :raise: PieceOffTheBoardError
        :return:
        """
        if self.__board is None:
            raise PieceOffTheBoardError(self)

        position = self.__board.get_piece_position(self)
        if position is None:
            raise PieceOffTheBoardError(self)

        return position

    @property
    def onboard(self) -> bool:
        """
        Inform if piece is on a board
        :return: bool
        """
        return self.__board is not None

    def move(self, position: Position) -> None:
        """
        Move the piece to an available position
        :param position: new position to the piece
        :raises MovimentNotAllowedError, PieceOffTheBoardError
        """
        if position not in set(self.movements()):
            raise MovimentNotAllowedError(self, position)

        self.board.place(self, position)

    @abstractmethod
    def movements(self) -> Iterable[Position]:
        """
        Return all availbale positions that the piece has
        :return: iterator with available positions
        """
        ...
