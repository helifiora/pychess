from pychess.board import Board
from pychess.piece import Knight
from pychess.color import Color
from pychess.position import Position

b = Board.empty()

b.place(Knight(Color.WHITE), Position(5, 5))
b.place(Knight(Color.WHITE), Position(5, 1))


origin = Position(5, 5)


def increment(entry: Position) -> Position:
    return entry + Position(1, 0)


for position in b.iterator(origin, increment, take=1):
    print(position)
