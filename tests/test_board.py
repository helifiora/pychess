from pychess.board import Board
from pychess.position import Position


def test_board_empty():
    board = Board.empty()

    positions = [board.get_piece(Position(x, y)) for x in range(0, 8) for y in range(0, 8)]
    assert not any(filter(lambda p: p is not None, positions))
