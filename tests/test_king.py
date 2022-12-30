from pychess.piece import King
from pychess.board import Board
from pychess.piece.color import Color
from pychess.position import Position


def test_create():
    board = Board.empty()

    k = King(Color.BLACK)
    board.place(k, Position(1, 1))

    print(k.movements())
