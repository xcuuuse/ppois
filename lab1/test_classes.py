"""
@file test_classes.py
@brief Tests for Game class
"""

from CLASSES import Game


def test_field():
    game = Game(3)
    assert game.get_field() == [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    assert game.get_symbol() == 'X'


def test_next_move():
    game = Game(3)
    game.next_move()
    assert game.get_symbol() == 'O'


def test_turn():
    game = Game(3)
    game.turn(0, 0)
    assert game.get_field()[0][0] == 'X'


def test_occupied():
    game = Game(3)
    game.turn(0, 0)
    game.next_move()
    game.turn(0, 0)
    assert game.get_symbol() == 'X'


def test_invalid():
    game = Game(3)
    game.turn(4, 4)
    game.next_move()
    assert game.get_symbol() == 'X'


def test_winner_row():
    game = Game(3)
    for i in range(game.get_field_size()):
        game.set_field(1, i, 'X')
    assert game.game_winner()


def test_winner_column():
    game = Game(3)
    for i in range(game.get_field_size()):
        game.set_field(i, 0, 'X')
    assert game.game_winner()


def test_winner_diagonals():
    game = Game(3)
    for i in range(game.get_field_size()):
        game.set_field(i, i, 'X')
    assert game.game_winner()
    new_game = Game(3)
    for i in range(new_game.get_field_size()):
        new_game.set_field(i, new_game.get_field_size() - i - 1, 'X')
    assert game.game_winner()


def test_draw():
    first = ['X', 'O', 'O']
    second = ['O', 'X', 'X']
    third = ['X', 'X', 'O']
    game = Game(3)
    for i in range(3):
        game.set_field(0, i, first[i])
        game.set_field(1, i, second[i])
        game.set_field(2, i, third[i])
    assert not game.game_winner()



