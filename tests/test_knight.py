from pytest import raises, mark
from pychess.board import Board
from pychess.piece import Knight
from pychess.piece.errors import PieceOffTheBoardError
from pychess.color import Color
from pychess.position import Position


def test_movements_raises_offtheboarderror_when_piece_is_not_in_the_board():
    rook = Knight(Color.BLACK)
    with raises(PieceOffTheBoardError):
        rook.movements()


def test_position_raises_offtheboarderror_when_piece_is_not_in_the_board():
    rook = Knight(Color.BLACK)
    with raises(PieceOffTheBoardError):
        assert rook.position


@mark.parametrize('entry, output', [
    (
            Position(0, 3),
            [Position(1, 1), Position(1, 5), Position(2, 2), Position(2, 4)]
    ),
    (
            Position(0, 4),
            [Position(1, 2), Position(1, 6), Position(2, 3), Position(2, 5)]
    ),
    (
            Position(3, 0),
            [Position(1, 1), Position(5, 1), Position(2, 2), Position(4, 2)]
    ),
    (
            Position(4, 0),
            [Position(2, 1), Position(6, 1), Position(3, 2), Position(5, 2)]
    ),
    (
            Position(3, 7),
            [Position(1, 6), Position(5, 6), Position(2, 5), Position(4, 5)]
    ),
    (
            Position(4, 7),
            [Position(2, 6), Position(6, 6), Position(3, 5), Position(5, 5)]
    ),
    (
            Position(7, 3),
            [Position(6, 1), Position(6, 5), Position(5, 2), Position(5, 4)]
    ),
    (
            Position(7, 4),
            [Position(6, 2), Position(6, 6), Position(5, 3), Position(5, 5)]
    ),
])
def test_moviments_when_piece_in_middle_corner_position(entry: Position, output: list[Position]):
    board = Board.empty()
    knight = Knight(Color.BLACK)
    board.place(knight, entry)
    assert set(knight.movements()) == set(output)


@mark.parametrize('entry, output', [
    (Position(0, 0), [Position(1, 2), Position(2, 1)]),
    (Position(7, 0), [Position(5, 1), Position(6, 2)]),
    (Position(0, 7), [Position(2, 6), Position(1, 5)]),
    (Position(7, 7), [Position(6, 5), Position(5, 6)]),
])
def test_moviments_when_piece_in_corner_position(entry: Position, output: list[Position]):
    board = Board.empty()
    knight = Knight(Color.BLACK)
    board.place(knight, entry)
    assert set(knight.movements()) == set(output)


@mark.parametrize('entry, output', [
    (
            Position(2, 2),
            [
                Position(1, 0), Position(3, 0), Position(0, 1), Position(4, 1),
                Position(0, 3), Position(4, 3), Position(1, 4), Position(3, 4)
            ]
    ),
    (
            Position(5, 5),
            [
                Position(4, 3), Position(6, 3), Position(3, 4), Position(7, 4),
                Position(3, 6), Position(7, 6), Position(4, 7), Position(6, 7)
            ]
    ),
    (
            Position(4, 3),
            [
                Position(3, 1), Position(5, 1), Position(2, 2), Position(6, 2),
                Position(2, 4), Position(6, 4), Position(3, 5), Position(5, 5)
            ]
    ),
])
def test_moviments_when_piece_in_position_with_all_possibilities(entry: Position, output: list[Position]):
    board = Board.empty()
    knight = Knight(Color.BLACK)
    board.place(knight, entry)
    assert set(knight.movements()) == set(output)


@mark.parametrize('entry, other, output', [
    (
            Position(2, 2),
            [Position(4, 1), Position(0, 1)],
            [Position(1, 0), Position(3, 0), Position(0, 3), Position(4, 3), Position(1, 4), Position(3, 4)]
    ),
    (
            Position(5, 5),
            [Position(6, 3), Position(7, 4), Position(6, 7), Position(4, 7)],
            [Position(4, 3), Position(3, 4), Position(3, 6), Position(7, 6)]
    ),
    (
            Position(4, 3),
            [Position(6, 4)],
            [
                Position(3, 1), Position(5, 1), Position(2, 2), Position(6, 2),
                Position(2, 4), Position(3, 5), Position(5, 5)
            ]
    ),
])
def test_moviments_with_piece_and_ally_pieces_in_board(entry: Position, other: list[Position], output: list[Position]):
    board = Board.empty()
    knight = Knight(Color.BLACK)
    board.place(knight, entry)

    for p in other:
        board.place(Knight(Color.BLACK), p)

    assert set(knight.movements()) == set(output)
