from pychess.piece import King, Rook, Bishop
from pychess.board import Board
from pychess.piece.color import Color
from pychess.position import Position


def test_create():
    board = Board.empty()

    k = King(Color.BLACK)
    board.place(k, Position(1, 1))

    board.place(Rook(Color.WHITE), Position(0, 5))
    board.place(Rook(Color.WHITE), Position(2, 5))
    board.place(Bishop(Color.WHITE), Position(1, 2))

    print(sorted(k.movements()))
