from pytest import raises
from pychess.position import Position
from pychess.game import Game, AnotherTeamTurnError


def test_raise_error_when_black_piece_play_in_white_team_turn():
    game = Game()

    with raises(AnotherTeamTurnError):
        game.play(Position(0, 0), Position(5, 5))


def test_raise_error_when_white_piece_play_in_black_team_turn():
    game = Game()

    game.play(Position(0, 6), Position(0, 5))
    with raises(AnotherTeamTurnError):
        game.play(Position(0, 7), Position(0, 6))
