class Game:
    def __init__(self, field_size: int):
        self.field_size = field_size
        self.field = [['.' for _ in range(field_size)] for _ in range(field_size)]
        self.symbol = 'X'

    def show_field(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                print(self.field[i][j], end=' ')
            print('\n')

    def next_move(self):
        self.symbol = 'X' if self.symbol == 'O' else 'O'

    def turn(self, row: int, column: int):
        if 0 <= row < self.field_size and 0 <= column < self.field_size:
            if self.field[row][column] == '.':
                self.field[row][column] = self.symbol
            else:
                print("The cell is occupied")
                Game.next_move(self)
        else:
            print("Invalid coordinates")
            Game.next_move(self)

    def game_winner(self):
        for i in range(self.field_size):
            if self.field[i] == [self.symbol] * self.field_size:
                return True
            if [self.field[j][i] for j in range(self.field_size)] == [self.symbol] * self.field_size:
                return True
        if [self.field[i][i] for i in range(self.field_size)] == [self.symbol] * self.field_size:
            return True
        if [self.field[i][self.field_size-i-1] for i in range(self.field_size)] == [self.symbol] * self.field_size:
            return True
        return False
