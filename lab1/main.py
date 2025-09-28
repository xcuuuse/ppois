"""
@file main.py
@brief Program file that is executed
"""
from classes import Game


def show_field(game: Game):
    for i in range(game.field_size):
        for j in range(game.field_size):
            print(game[i, j], end=' ')
        print('\n')


def start_game():
    """
    @brief Start game
    @details A function that runs the gaming process
    @see Game0
    @see Game.turn()
    @see Game.show_field()
    @see Game.get_symbol()
    @see Game.game_winner()
    @see Game.next_move()
    """
    field_size = int(input("Enter the size of a field: "))
    game = Game(field_size)
    show_field(game)
    amount = 0
    while True:
        print("Enter coordinates for X") if game.symbol == 'X' else print("Enter coordinates for O")
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        game.turn(row, column)
        show_field(game)
        amount += 1
        if game.game_winner():
            print("player1 won") if game.symbol == 'X' else print("player2 won")
            break
        if not game.game_winner() and amount == field_size * field_size:
            print("The game is tied")
            break
        game.next_move()


while True:
    greeting = str(input("Wanna start a new game? y/n: "))
    if greeting == "y":
        start_game()
        continue
    elif greeting == "n":
        print("Goodbye")
        break
    else:
        print("Incorrect input, try again")
