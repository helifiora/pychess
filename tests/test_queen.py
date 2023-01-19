from pytest import mark
from pychess.board import Board
from pychess.piece import Queen
from pychess.color import Color
from pychess.position import Position


@mark.parametrize('entry, output', [
    (
            Position(0, 3),
            [
                Position(0, 2), Position(0, 1), Position(0, 0),
                Position(0, 4), Position(0, 5), Position(0, 6), Position(0, 7),
                Position(1, 3), Position(2, 3), Position(3, 3), Position(4, 3), Position(5, 3), Position(6, 3),
                Position(7, 3),
                Position(1, 2), Position(2, 1), Position(3, 0),
                Position(1, 4), Position(2, 5), Position(3, 6), Position(4, 7)
            ]
    ),
    (
            Position(3, 0),
            [
                Position(3, 1), Position(3, 2), Position(3, 3), Position(3, 4), Position(3, 5), Position(3, 6),
                Position(3, 7),
                Position(2, 0), Position(1, 0), Position(0, 0),
                Position(4, 0), Position(5, 0), Position(6, 0), Position(7, 0),
                Position(2, 1), Position(1, 2), Position(0, 3),
                Position(4, 1), Position(5, 2), Position(6, 3), Position(7, 4)
            ]
    ),
    (
            Position(3, 7),
            [
                Position(3, 6), Position(3, 5), Position(3, 4), Position(3, 3), Position(3, 2), Position(3, 1),
                Position(3, 0),
                Position(2, 7), Position(1, 7), Position(0, 7),
                Position(4, 7), Position(5, 7), Position(6, 7), Position(7, 7),
                Position(2, 6), Position(1, 5), Position(0, 4),
                Position(4, 6), Position(5, 5), Position(6, 4), Position(7, 3)
            ]
    ),
    (
            Position(7, 3),
            [
                Position(7, 2), Position(7, 1), Position(7, 0),
                Position(7, 4), Position(7, 5), Position(7, 6), Position(7, 7),
                Position(6, 3), Position(5, 3), Position(4, 3), Position(3, 3), Position(2, 3),
                Position(1, 3), Position(0, 3),
                Position(6, 2), Position(5, 1), Position(4, 0),
                Position(6, 4), Position(5, 5), Position(4, 6), Position(3, 7)
            ]
    ),

])
def test_moviments_when_queen_in_middle_corner_position(entry: Position, output: list[Position]):
    board = Board.empty()
    queen = Queen(Color.BLACK)
    board.place(queen, entry)
    assert set(queen.movements()) == set(output)


@mark.parametrize('entry, output', [
    (
            Position(0, 0),
            [
                Position(1, 0), Position(2, 0), Position(3, 0), Position(4, 0), Position(5, 0), Position(6, 0),
                Position(7, 0),
                Position(0, 1), Position(0, 2), Position(0, 3), Position(0, 4), Position(0, 5), Position(0, 6),
                Position(0, 7),
                Position(1, 1), Position(2, 2), Position(3, 3), Position(4, 4), Position(5, 5), Position(6, 6),
                Position(7, 7)
            ]),
    (
            Position(7, 0),
            [
                Position(0, 0), Position(1, 0), Position(2, 0), Position(3, 0), Position(4, 0), Position(5, 0),
                Position(6, 0),
                Position(7, 1), Position(7, 2), Position(7, 3), Position(7, 4), Position(7, 5), Position(7, 6),
                Position(7, 7),
                Position(0, 7), Position(1, 6), Position(2, 5), Position(3, 4), Position(4, 3), Position(5, 2),
                Position(6, 1),
            ]),
    (
            Position(0, 7),
            [
                Position(1, 7), Position(2, 7), Position(3, 7), Position(4, 7), Position(5, 7), Position(6, 7),
                Position(7, 7),
                Position(0, 0), Position(0, 1), Position(0, 2), Position(0, 3), Position(0, 4), Position(0, 5),
                Position(0, 6),
                Position(1, 6), Position(2, 5), Position(3, 4), Position(4, 3), Position(5, 2), Position(6, 1),
                Position(7, 0)
            ]),
    (
            Position(7, 7),
            [
                Position(7, 0), Position(7, 1), Position(7, 2), Position(7, 3), Position(7, 4), Position(7, 5),
                Position(7, 6),
                Position(0, 7), Position(1, 7), Position(2, 7), Position(3, 7), Position(4, 7), Position(5, 7),
                Position(6, 7),
                Position(0, 0), Position(1, 1), Position(2, 2), Position(3, 3), Position(4, 4), Position(5, 5),
                Position(6, 6),
            ]
    ),
])
def test_moviments_when_queen_in_corner_position(entry: Position, output: list[Position]):
    board = Board.empty()
    queen = Queen(Color.BLACK)
    board.place(queen, entry)
    assert set(queen.movements()) == set(output)


@mark.parametrize('entry, output', [
    (
            Position(2, 2),
            [
                Position(2, 1), Position(2, 0),
                Position(1, 2), Position(0, 2),
                Position(2, 3), Position(2, 4), Position(2, 5), Position(2, 6), Position(2, 7),
                Position(3, 2), Position(4, 2), Position(5, 2), Position(6, 2), Position(7, 2),
                Position(1, 1), Position(0, 0),
                Position(3, 3), Position(4, 4), Position(5, 5), Position(6, 6), Position(7, 7),
                Position(3, 1), Position(4, 0),
                Position(1, 3), Position(0, 4)
            ]
    ),
])
def test_moviments_when_queen_in_position_with_all_possibilities(entry: Position, output: list[Position]):
    board = Board.empty()
    queen = Queen(Color.BLACK)
    board.place(queen, entry)
    assert set(queen.movements()) == set(output)


@mark.parametrize('entry, other, output', [
    (
            Position(4, 4),
            [Position(4, 2), Position(2, 4), Position(5, 5), Position(1, 1)],
            [
                Position(4, 2), Position(2, 4), Position(4, 3), Position(3, 4),
                Position(4, 5), Position(4, 6), Position(4, 7),
                Position(5, 4), Position(6, 4), Position(7, 4),
                Position(3, 3), Position(2, 2), Position(1, 1),
                Position(5, 5),
                Position(3, 5), Position(2, 6), Position(1, 7),
                Position(5, 3), Position(6, 2), Position(7, 1)
            ]
    ),
])
def test_moviments_with_queen_and_enemys_pieces_in_board(entry: Position, other: list[Position],
                                                         output: list[Position]):
    board = Board.empty()
    queen = Queen(Color.BLACK)
    board.place(queen, entry)

    for p in other:
        board.place(Queen(Color.WHITE), p)

    assert set(queen.movements()) == set(output)
