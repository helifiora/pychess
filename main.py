import time
from pychess.board import Board
from pychess.piece import King, Rook
from pychess.color import Color
from pychess.position import Position
from pychess.game import Game

b = Board.empty()
b.place(King(Color.BLACK), Position(4, 0))
b.place(Rook(Color.BLACK), Position(4, 1))

b.place(Rook(Color.WHITE), Position(4, 6))

game = Game(board=b, turn=Color.BLACK)
game.play(Position(4, 1), Position(4, 7))
