from CLASSES import Game


def test_field():
    game = Game(3)
    assert game.field == [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    assert game.symbol == 'X'


def test_next_move():
    game = Game(3)
    game.next_move()
    assert game.symbol == 'O'


def test_turn():
    game = Game(3)
    game.turn(0, 0)
    assert game.field[0][0] == 'X'


def test_occupied():
    game = Game(3)
    game.turn(0, 0)
    game.next_move()
    game.turn(0, 0)
    assert game.symbol == 'X'


def test_invalid():
    game = Game(3)
    game.turn(4, 4)
    game.next_move()
    assert game.symbol == 'X'


def test_winner_row():
    game = Game(3)
    game.field[0] = ['X', 'X', 'X']
    assert game.game_winner()


def test_winner_diagonals():
    game = Game(3)
    game.turn(0, 2)
    game.next_move()
    for i in range(game.field_size):
        game.field[i][i] = 'O'
    assert game.game_winner()
    new_game = Game(3)
    for i in range(new_game.field_size):
        new_game.field[i][new_game.field_size - i - 1] = 'X'
    assert new_game.game_winner()


def test_winner_column():
    game = Game(3)
    for i in range(game.field_size):
        game.field[i][1] = 'X'
    assert game.game_winner()


def test_draw():
    game = Game(3)
    game.field = [['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'X', 'O']]
    assert not game.game_winner()
    new_game = Game(3)
    new_game.field = [['O', 'O', 'X'], ['X', 'X', 'O'], ['O', 'O', 'X']]
    assert not new_game.game_winner()
