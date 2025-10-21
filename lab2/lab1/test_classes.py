"""
@file test_classes.py
@brief Classes tests
"""

from classes import Game


def test_field_size():
    game = Game(3)
    assert game.field_size == 3


def test_field():
    game = Game(3)
    assert game.field == [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]


def test_symbol():
    game = Game(5)
    assert game.symbol == 'X'


def test_get_item():
    game = Game(3)
    assert game[1, 2] == '.'


def test_set_item():
    game = Game(4)
    game[1, 2] = 'O'
    assert game[1, 2] == 'O'


def test_next_move():
    game = Game(4)
    game.next_move()
    assert game.symbol == 'O'


def test_turn():
    game = Game(5)
    game.turn(1, 1)
    game.next_move()
    game.turn(0, 0)
    assert game[1, 1] == 'X'
    assert game[0, 0] == 'O'


def test_occupied():
    game = Game(5)
    game.turn(1, 1)
    game.turn(1, 1)
    assert game.symbol == 'O'


def test_invalid_coordinates():
    game = Game(4)
    game.turn(5, 1)
    game.next_move()
    assert game.symbol == 'X'


def test_winner_row():
    game = Game(3)
    for j in range(game.field_size):
        game[1, j] = 'X'
    assert game.game_winner()


def test_winner_row_o():
    game = Game(4)
    game.next_move()
    for j in range(game.field_size):
        game[0, j] = 'O'
    assert game.game_winner()


def test_winner_column():
    game = Game(3)
    for i in range(game.field_size):
        game[i, 1] = 'X'
    assert game.game_winner()


def test_winner_column_o():
    game = Game(3)
    game.next_move()
    for i in range(game.field_size):
        game[0, i] = 'O'
    assert game.game_winner()


def test_winner_main():
    game = Game(5)
    for i in range(game.field_size):
        game[i, i] = 'X'
    assert game.game_winner()


def test_winner_main_o():
    game = Game(5)
    game.next_move()
    for i in range(game.field_size):
        game[i, i] = 'O'
    assert game.game_winner()


def test_winner_side():
    game = Game(5)
    for i in range(game.field_size):
        game[i, game.field_size - i - 1] = 'X'
    assert game.game_winner()


def test_winner_side_o():
    game = Game(5)
    game.next_move()
    for i in range(game.field_size):
        game[i, game.field_size - i - 1] = 'O'
    assert game.game_winner()


def test_first_winner():
    game = Game(1)
    game.turn(0, 0)
    assert game.game_winner()


def test_empty_winner():
    game = Game(3)
    assert not game.game_winner()


def test_not_winner():
    game = Game(3)
    game.turn(0, 2)
    game.next_move()
    assert not game.game_winner()


def test_negative():
    game = Game(4)
    game.turn(0, -3)
    assert IndexError


def test_big():
    game = Game(4)
    game.turn(5, 0)
    assert IndexError



