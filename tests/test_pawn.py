from pytest import mark
from pychess.piece import Pawn
from pychess.board import Board
from pychess.position import Position
from pychess.color import Color


@mark.parametrize('entry, output', [
    (Position(0, 1), [Position(0, 2), Position(0, 3)]),
    (Position(1, 1), [Position(1, 2), Position(1, 3)]),
    (Position(2, 1), [Position(2, 2), Position(2, 3)]),
    (Position(3, 1), [Position(3, 2), Position(3, 3)]),
    (Position(4, 1), [Position(4, 2), Position(4, 3)]),
    (Position(5, 1), [Position(5, 2), Position(5, 3)]),
    (Position(6, 1), [Position(6, 2), Position(6, 3)]),
    (Position(7, 1), [Position(7, 2), Position(7, 3)]),
])
def test_black_pawn_move_bottom_first_time(entry: Position, output: list[Position]):
    pawn = Pawn(Color.BLACK)
    board = Board.empty()
    board.place(pawn, entry)
    assert set(pawn.movements()) == set(output)


@mark.parametrize('entry, output', [
    (Position(0, 1), [Position(0, 2)]),
    (Position(1, 1), [Position(1, 2)]),
    (Position(2, 1), [Position(2, 2)]),
    (Position(3, 1), [Position(3, 2)]),
    (Position(4, 1), [Position(4, 2)]),
    (Position(5, 1), [Position(5, 2)]),
    (Position(6, 1), [Position(6, 2)]),
    (Position(7, 1), [Position(7, 2)]),
])
def test_black_pawn_move_bottom(entry: Position, output: list[Position]):
    pawn = Pawn(Color.BLACK)
    board = Board.empty()
    board.place(pawn, entry)
    pawn.first_move = False
    assert set(pawn.movements()) == set(output)


@mark.parametrize('entry, others, output', [
    (Position(0, 1), [Position(1, 2)], [Position(0, 2), Position(1, 2)]),
    (Position(1, 1), [Position(0, 2), Position(2, 2)], [Position(1, 2), Position(0, 2), Position(2, 2)]),
    (Position(2, 1), [Position(3, 2)], [Position(2, 2), Position(3, 2)]),
    (Position(3, 1), [Position(2, 2)], [Position(3, 2), Position(2, 2)]),
    (Position(4, 1), [Position(5, 2), Position(7, 2)], [Position(4, 2), Position(5, 2)]),
    (Position(5, 1), [Position(6, 2)], [Position(5, 2), Position(6, 2)]),
    (Position(6, 1), [Position(5, 0), Position(7, 0)], [Position(6, 2)]),
    (Position(7, 1), [Position(6, 2)], [Position(7, 2), Position(6, 2)]),
])
def test_black_pawn_move_bottom_and_diagonal_enemy(entry: Position, others: list[Position], output: list[Position]):
    pawn = Pawn(Color.BLACK)
    board = Board.empty()
    board.place(pawn, entry)
    pawn.first_move = False

    for other in others:
        board.place(Pawn(Color.WHITE), other)

    assert set(pawn.movements()) == set(output)


@mark.parametrize('entry, others, output', [
    (Position(0, 1), [Position(1, 2)], [Position(0, 2), Position(1, 2), Position(0, 3)]),
    (
            Position(1, 1), [Position(0, 2), Position(2, 2)],
            [Position(1, 2), Position(0, 2), Position(2, 2), Position(1, 3)]
    ),
])
def test_black_pawn_move_bottom_first_and_diagonal_enemy(entry: Position, others: list[Position],
                                                         output: list[Position]):
    pawn = Pawn(Color.BLACK)
    board = Board.empty()
    board.place(pawn, entry)

    for other in others:
        board.place(Pawn(Color.WHITE), other)

    assert set(pawn.movements()) == set(output)


@mark.parametrize('entry, output', [
    (Position(0, 6), [Position(0, 5), Position(0, 4)]),
    (Position(1, 6), [Position(1, 5), Position(1, 4)]),
    (Position(2, 6), [Position(2, 5), Position(2, 4)]),
    (Position(3, 6), [Position(3, 5), Position(3, 4)]),
    (Position(4, 6), [Position(4, 5), Position(4, 4)]),
    (Position(5, 6), [Position(5, 5), Position(5, 4)]),
    (Position(6, 6), [Position(6, 5), Position(6, 4)]),
    (Position(7, 6), [Position(7, 5), Position(7, 4)]),
])
def test_white_pawn_move_top_first_time(entry: Position, output: list[Position]):
    pawn = Pawn(Color.WHITE)
    board = Board.empty()
    board.place(pawn, entry)
    assert set(pawn.movements()) == set(output)


@mark.parametrize('entry, output', [
    (Position(0, 6), [Position(0, 5)]),
    (Position(1, 6), [Position(1, 5)]),
    (Position(2, 6), [Position(2, 5)]),
    (Position(3, 6), [Position(3, 5)]),
    (Position(4, 6), [Position(4, 5)]),
    (Position(5, 6), [Position(5, 5)]),
    (Position(6, 6), [Position(6, 5)]),
    (Position(7, 6), [Position(7, 5)]),
])
def test_white_pawn_move_top(entry: Position, output: list[Position]):
    pawn = Pawn(Color.WHITE)
    board = Board.empty()
    board.place(pawn, entry)
    pawn.first_move = False
    assert set(pawn.movements()) == set(output)


@mark.parametrize('entry, others, output', [
    (Position(0, 6), [Position(1, 5)], [Position(0, 5), Position(1, 5)]),
    (Position(1, 6), [Position(0, 7), Position(0, 5)], [Position(1, 5), Position(0, 5)]),
    (Position(2, 6), [Position(3, 5)], [Position(2, 5), Position(3, 5)]),
    (Position(3, 6), [Position(2, 5)], [Position(3, 5), Position(2, 5)]),
    (Position(4, 6), [Position(5, 5), Position(7, 7)], [Position(4, 5), Position(5, 5)]),
    (Position(5, 6), [Position(6, 5)], [Position(5, 5), Position(6, 5)]),
    (Position(6, 6), [Position(7, 5), Position(5, 5)], [Position(6, 5), Position(7, 5), Position(5, 5)]),
    (Position(7, 6), [Position(6, 5)], [Position(7, 5), Position(6, 5)]),
])
def test_white_pawn_move_top_and_diagonal_enemy(entry: Position, others: list[Position], output: list[Position]):
    pawn = Pawn(Color.WHITE)
    board = Board.empty()
    board.place(pawn, entry)
    pawn.first_move = False

    for other in others:
        board.place(Pawn(Color.BLACK), other)

    assert set(pawn.movements()) == set(output)


@mark.parametrize('entry, others, output', [
    (Position(0, 6), [Position(1, 5)], [Position(0, 5), Position(0, 4), Position(1, 5)]),
    (
            Position(1, 6), [Position(0, 5), Position(2, 5)],
            [Position(1, 5), Position(1, 4), Position(2, 5), Position(0, 5)]
    ),
])
def test_white_pawn_move_top_first_and_diagonal_enemy(entry: Position, others: list[Position], output: list[Position]):
    pawn = Pawn(Color.WHITE)
    board = Board.empty()
    board.place(pawn, entry)

    for other in others:
        board.place(Pawn(Color.BLACK), other)

    assert set(pawn.movements()) == set(output)


def test_black_pawn_move_vertical_and_diagonal_not_include_ally():
    pawn = Pawn(Color.BLACK)
    board = Board.empty()
    board.place(pawn, Position(0, 1))

    board.place(Pawn(Color.BLACK), Position(1, 2))
    board.place(Pawn(Color.BLACK), Position(0, 3))
    result = {Position(0, 2)}

    assert set(pawn.movements()) == result


def test_white_pawn_move_vertical_and_diagonal_not_include_ally():
    pawn = Pawn(Color.WHITE)
    board = Board.empty()
    board.place(pawn, Position(0, 6))

    board.place(Pawn(Color.WHITE), Position(1, 5))
    board.place(Pawn(Color.WHITE), Position(0, 4))
    result = {Position(0, 5)}

    assert set(pawn.movements()) == result
