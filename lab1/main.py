from CLASSES import Game


def start_game():
    field_size = int(input("Enter the size of a field: "))
    game = Game(field_size)
    game.show_field()
    amount = 0
    while True:
        print("Enter coordinates for X") if game.symbol == 'X' else print("Enter coordinates for O")
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        game.turn(row, column)
        game.show_field()
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
