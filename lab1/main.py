"""
@file main.py
@brief Program file that is executed
"""
from CLASSES import Game


def start_game():
    """
    @brief Start game
    @details A function that runs the gaming process
    @see Game
    @see Game.turn()
    @see Game.show_field()
    @see Game.get_symbol()
    @see Game.game_winner()
    @see Game.next_move()
    """
    field_size = int(input("Enter the size of a field: "))
    game = Game(field_size)
    game.show_field()
    amount = 0
    while True:
        print("Enter coordinates for X") if game.get_symbol() == 'X' else print("Enter coordinates for O")
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        game.turn(row, column)
        game.show_field()
        amount += 1
        if game.game_winner():
            print("player1 won") if game.get_symbol() == 'X' else print("player2 won")
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
