"""
@file CLASSES.py
@brief Tic-Tac-Toe game realisation
@author Yevik A. 421702
"""


class Game:
    """!
    @brief Tic-Tac-Toe game class
    @details Controls the field, players turns and defines the winner
    """
    def __init__(self, field_size: int):
        """
        @brief Constructor
        :param field_size: The size of a game field
        """
        self.__field_size = field_size
        self.__field = [['.' for _ in range(field_size)] for _ in range(field_size)]
        self.__symbol = 'X'

    def __getitem__(self, pos):
        row, column = pos
        if 0 <= row < self.__field_size and 0 <= column < self.__field_size:
            return self.__field[row][column]
        else:
            raise IndexError("Invalid coordinates")

    def get_symbol(self):
        """
        @brief Symbol getter
        @details A method to get the current game symbol
        :return: str game symbol
        """
        return self.__symbol

    def get_field(self):
        """
        @brief Field getter
        @details A method to get the field
        :return: List[list] game field
        """
        return self.__field.copy()

    def get_field_size(self):
        """
        @brief Field size getter
        @details A method to get the size
        :return: int field size
        """
        return self.__field_size

    def set_field(self, row, column, symbol):
        """
        @brief Field cell setter
        :param row: row
        :param column: column
        :param symbol: symbol
        """
        self.__field[row][column] = symbol

    def show_field(self):
        """
        @brief Show field
        @details A method to show the game field
        """
        for i in range(self.__field_size):
            for j in range(self.__field_size):
                print(self.__field[i][j], end=' ')
            print('\n')

    def next_move(self):
        """
        @brief Game next move
        @details Implements players turn change mechanics
        """
        self.__symbol = 'X' if self.__symbol == 'O' else 'O'

    def turn(self, row: int, column: int):
        """
        @brief Game turn
        @details A method to implement the mechanics of cell occupation
        :param row: row
        :param column: column
        @see next_move
        @see game_winner
        """
        if 0 <= row < self.__field_size and 0 <= column < self.__field_size:
            if self.__field[row][column] == '.':
                self.__field[row][column] = self.__symbol
            else:
                print("The cell is occupied")
                Game.next_move(self)
        else:
            print("Invalid coordinates")
            Game.next_move(self)

    def game_winner(self):
        """
        @brief Game winner
        @details A method to implement the mechanics of game winning or a draw
        :return: bool game is won by one of the players
        @see turn
        """
        for i in range(self.__field_size):
            if self.__field[i] == [self.__symbol] * self.__field_size:
                return True
            if [self.__field[j][i] for j in range(self.__field_size)] == [self.__symbol] * self.__field_size:
                return True
        if [self.__field[i][i] for i in range(self.__field_size)] == [self.__symbol] * self.__field_size:
            return True
        size = self.__field_size
        if [self.__field[i][size-i-1]for i in range(size)] == [self.__symbol]*self.__field_size:
            return True
        return False
