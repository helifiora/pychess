from typing import Protocol, Iterable

from pychess.color import Color
from pychess.board import Board
from pychess.position import Position
from pychess.piece import Rook, Knight, King, Bishop, Pawn, Queen, Piece


class PieceGame(Protocol):

    @property
    def color(self) -> Color:
        raise NotImplemented()

    def movements(self) -> Iterable[Position]:
        raise NotImplemented()


class NoPieceInPositionError(Exception):
    ...


class AnotherTeamTurnError(Exception):
    ...


class PieceCanNotMoveError(Exception):
    ...


class Game:
    __board: Board
    __turn: Color
    __captured: set[PieceGame]

    def __init__(self):
        self.__board = self.create_board()
        self.__turn = Color.WHITE
        self.__captured = set()

    @property
    def turn(self) -> Color:
        return self.__turn

    def select_piece_moves(self, position: Position) -> list[Position]:
        piece = self.__board.get_piece(position)
        if piece is None:
            raise NoPieceInPositionError()

        if piece.color != self.__turn:
            raise AnotherTeamTurnError()

        return list(piece.movements())

    def play(self, source: Position, target: Position) -> None:

        piece = self.__select_source_piece(source)
        old_value = self.__select_target_piece(target)

        piece.move(target)

        # TODO: verificar jogadas especiais como a troca entre Roque
        if old_value is not None and not old_value.onboard:
            self.__captured.add(old_value)

        self.__turn = Color.BLACK if self.__turn == Color.WHITE else Color.WHITE

    def __select_source_piece(self, source: Position) -> Piece:
        piece = self.__board.get_piece(source)
        if piece is None:
            raise NoPieceInPositionError()

        if piece.color != self.__turn:
            raise AnotherTeamTurnError()

        if not piece.has_movements:
            raise PieceCanNotMoveError()

        return piece

    def __select_target_piece(self, target: Position) -> Piece | None:
        return self.__board.get_piece(target)

    @staticmethod
    def create_board() -> Board:
        board = Board.empty()

        # PEÇAS PRETAS
        board.place(Rook(Color.BLACK), Position(0, 0))
        board.place(Knight(Color.BLACK), Position(1, 0))
        board.place(Bishop(Color.BLACK), Position(2, 0))
        board.place(Queen(Color.BLACK), Position(3, 0))
        board.place(King(Color.BLACK), Position(4, 0))
        board.place(Bishop(Color.BLACK), Position(5, 0))
        board.place(Knight(Color.BLACK), Position(6, 0))
        board.place(Rook(Color.BLACK), Position(7, 0))

        # PEÇAS BRANCAS
        board.place(Rook(Color.WHITE), Position(0, 7))
        board.place(Knight(Color.WHITE), Position(1, 7))
        board.place(Bishop(Color.WHITE), Position(2, 7))
        board.place(Queen(Color.WHITE), Position(3, 7))
        board.place(King(Color.WHITE), Position(4, 7))
        board.place(Bishop(Color.WHITE), Position(5, 7))
        board.place(Knight(Color.WHITE), Position(6, 7))
        board.place(Rook(Color.WHITE), Position(7, 7))

        # PEÕES
        for x in range(8):
            board.place(Pawn(Color.BLACK), Position(x, 1))
            board.place(Pawn(Color.WHITE), Position(x, 6))

        return board
