"""
@file classes.py
@brief Tic-Tac-Toe game realisation
@author A. 421702
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

    def __setitem__(self, key, value):
        """
        @brief Set item method
        @details Allows to use () operator to set a cell symbol
        """
        row, column = key
        if 0 <= row < self.__field_size and 0 <= column < self.__field_size:
            self.__field[row][column] = value
        else:
            raise IndexError("Invalid coordinates")

    @property
    def symbol(self):

        return self.__symbol

    @property
    def field(self):
        return self.__field.copy()

    @property
    def field_size(self):
        return self.__field_size

    def next_move(self):
        """
        @brief Game next move
        @details Implements players turn change mechanics
        """
        self.__symbol = 'X' if self.symbol == 'O' else 'O'

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
            if self[row, column] == '.':
                self[row, column] = self.symbol
            else:
                print("The cell is occupied")
                self.next_move()
        else:
            print("Invalid coordinates")
            self.next_move()

    def game_winner(self):
        """
        @brief Game winner
        @details A method to implement the mechanics of game winning or a draw
        :return: bool game is won by one of the players
        @see turn
        """
        for i in range(self.__field_size):
            if [self[i, j] for j in range(self.field_size)] == [self.symbol] * self.field_size:
                return True
            if [self[j, i] for j in range(self.field_size)] == [self.symbol] * self.field_size:
                return True
            if [self[j, j] for j in range(self.field_size)] == [self.symbol] * self.field_size:
                return True
            if [self[j, self.field_size - j - 1] for j in range(self.field_size)] == [self.symbol] * self.field_size:
                return True
