from typing import Callable, Protocol, Iterable, Iterator

from pychess.color import Color
from pychess.board import Board
from pychess.position import Position
from pychess.piece import Rook, Knight, King, Bishop, Pawn, Queen, Piece


class NoPieceInPositionError(Exception):
    ...


class AnotherTeamTurnError(Exception):
    ...


class PieceCanNotMoveError(Exception):
    ...


class PieceMoveCauseCheckError(Exception):
    ...


class Game:
    __board: Board
    __turn: Color
    __captured: set[Piece]
    __check: Color | None
    __checkmate: Color | None

    def __init__(self, *, board: Board | None = None, turn: Color | None = None):
        self.__board = board or self.create_board()
        self.__turn = turn or Color.WHITE
        self.__captured = set()
        self.__check = None
        self.__checkmate = None

    @property
    def turn(self) -> Color:
        return self.__turn

    @property
    def check(self) -> Color | None:
        return self.__check

    @property
    def captured(self) -> set[Piece]:
        return self.__captured

    def play(self, source: Position, target: Position) -> None:
        origin_piece = self.__select_source_piece(source)
        target_piece = self.__select_target_piece(target)

        if Game.is_move_apply_check(self.__board, self.__turn, source, target):
            raise PieceMoveCauseCheckError()

        origin_piece.move(target)

        self.__capture_piece(target_piece)
        self.__change_turn()

        if not self.is_check(self.__board, self.__turn):
            return

        if self.is_checkmate(self.__board, self.__turn):
            self.__checkmate = self.__turn
        else:
            self.__check = self.__turn

    def select_piece_moves(self, position: Position) -> list[Position]:
        piece = self.__board.get_piece(position)
        if piece is None:
            raise NoPieceInPositionError()

        if piece.color != self.__turn:
            raise AnotherTeamTurnError()

        def wrapper(new_position: Position) -> bool:
            return not Game.is_move_apply_check(
                self.__board, self.__turn, position, new_position
            )

        return list(filter(wrapper, piece.movements()))

    def __capture_piece(self, piece: Piece | None) -> None:
        if piece is None or piece.onboard:
            return

        self.__captured.add(piece)

    def __change_turn(self) -> None:
        self.__turn = self.__turn.inverse()

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
    def is_check(board: Board, color: Color) -> bool:
        opponent_pieces = board.get_pieces(color.inverse())
        king_position = board.get_king(color).position

        def is_king_in_movements(piece: Piece) -> bool:
            return king_position in piece.movements()

        return any(map(is_king_in_movements, opponent_pieces))

    @staticmethod
    def is_checkmate(board: Board, color: Color) -> bool:
        def not_apply_check(origin: Position) -> Callable[[Position], bool]:
            def wrapper(target: Position) -> bool:
                return not Game.is_move_apply_check(board, color, origin, target)

            return wrapper

        moves_that_undo_check = (
            map(not_apply_check(piece.position), piece.movements())
            for piece in board.get_pieces(color)
        )

        return not any(moves_that_undo_check)

    @staticmethod
    def is_move_apply_check(
        board: Board, color: Color, origin: Position, target: Position
    ) -> bool:
        board_copy = board.clone()
        piece_copy = board_copy.get_piece(origin)
        if piece_copy is None:
            return False

        if not piece_copy.can_move_to(target):
            return False

        board_copy.place(piece_copy, target)
        return Game.is_check(board_copy, color)

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
