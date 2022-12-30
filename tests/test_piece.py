from pytest import raises, mark
from pychess.piece import *
from pychess.piece.errors import PieceOffTheBoardError, MovimentNotAllowedError
from pychess.board import Board
from pychess.piece.color import Color
from pychess.position import Position


def all_pieces() -> list[Piece]:
    return [
        Bishop(Color.BLACK), Bishop(Color.WHITE),
        King(Color.BLACK), King(Color.WHITE),
        Knight(Color.BLACK), Knight(Color.WHITE),
        Pawn(Color.BLACK), Pawn(Color.WHITE),
        Queen(Color.BLACK), Queen(Color.WHITE),
        Rook(Color.BLACK), Rook(Color.WHITE),
    ]


@mark.parametrize('piece', all_pieces())
def test_movements_raises_offtheboarderror_when_piece_is_not_in_the_board(piece: Piece):
    with raises(PieceOffTheBoardError):
        piece.movements()


@mark.parametrize('piece', all_pieces())
def test_position_raises_offtheboarderror_when_piece_is_not_in_the_board(piece: Piece):
    with raises(PieceOffTheBoardError):
        assert piece.position


@mark.parametrize('piece', all_pieces())
def test_move_raises_offtheboarderror_when_piece_is_not_in_the_board(piece: Piece):
    with raises(PieceOffTheBoardError):
        assert piece.move(Position(1, 1))


@mark.parametrize('piece', all_pieces())
def test_move_raises_movimentnotallowederror_when_position_is_not_in_movements(piece: Piece):
    origin = Position(1, 0)
    target = Position(7, 7)
    board = Board.empty()
    board.place(piece, origin)
    with raises(MovimentNotAllowedError):
        piece.move(target)


@mark.parametrize('piece', all_pieces())
def test_piece_onboard(piece: Piece):
    board = Board.empty()
    board.place(piece, Position(1, 1))
    assert piece.onboard


@mark.parametrize('piece', all_pieces())
def test_piece_offboard(piece: Piece):
    assert not piece.onboard


@mark.parametrize('piece', all_pieces())
def test_position_when_onboard(piece: Piece):
    board = Board.empty()
    board.place(piece, Position(1, 1))
    assert piece.position
