from pychess.piece import King, Rook, Bishop
from pychess.board import Board
from pychess.color import Color
from pychess.position import Position
from pytest import mark


@mark.parametrize('entry, output', [
    (Position(0, 0), [Position(1, 0), Position(1, 1), Position(0, 1)]),
    (Position(7, 0), [Position(6, 0), Position(6, 1), Position(7, 1)]),
    (Position(0, 7), [Position(1, 7), Position(1, 6), Position(0, 6)]),
    (Position(7, 7), [Position(6, 7), Position(6, 6), Position(7, 6)]),
    (Position(3, 0), [Position(2, 0), Position(2, 1), Position(3, 1), Position(4, 1), Position(4, 0)]),
    (Position(3, 7), [Position(2, 7), Position(2, 6), Position(3, 6), Position(4, 6), Position(4, 7)]),
    (Position(0, 3), [Position(0, 2), Position(1, 2), Position(1, 3), Position(1, 4), Position(0, 4)]),
    (Position(7, 3), [Position(7, 2), Position(6, 2), Position(6, 3), Position(6, 4), Position(7, 4)])
])
def test_movements_when_king_in_border(entry: Position, output: list[Position]):
    king = King(Color.WHITE)
    board = Board.empty()
    board.place(king, entry)
    assert set(king.movements()) == set(output)


@mark.parametrize('entry, output', [
    (
            Position(1, 1),
            [
                Position(0, 0), Position(1, 0), Position(2, 0),
                Position(0, 1), Position(2, 1),
                Position(0, 2), Position(1, 2), Position(2, 2)
            ]
    ),
    (
            Position(6, 6),
            [
                Position(5, 5), Position(6, 5), Position(7, 5),
                Position(5, 6), Position(7, 6),
                Position(5, 7), Position(6, 7), Position(7, 7)
            ]
    ),
    (
            Position(5, 3),
            [
                Position(4, 2), Position(5, 2), Position(6, 2),
                Position(4, 3), Position(6, 3),
                Position(4, 4), Position(5, 4), Position(6, 4)
            ]
    )
])
def test_movements_when_king_has_all_available(entry: Position, output: list[Position]):
    king = King(Color.WHITE)
    board = Board.empty()
    board.place(king, entry)
    assert set(king.movements()) == set(output)


def test_movements_when_enemy_pieces_can_intercept_king_move():
    board = Board.empty()

    k = King(Color.BLACK)
    board.place(k, Position(1, 1))

    board.place(Rook(Color.WHITE), Position(0, 5))
    board.place(Rook(Color.WHITE), Position(2, 5))
    board.place(Bishop(Color.WHITE), Position(1, 2))

    print(sorted(k.movements()))
