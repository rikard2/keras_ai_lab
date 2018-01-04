import numpy as np

class LuffarSchack:
    def __init__(self):
        self.board_size = 3
        self.in_a_row = 3
        self.new_game()

    def create_board(self, type = np.int8):
        return np.zeros( self.board_size ** 2, type ).reshape( self.board_size, self.board_size )
    def new_game(self):
        # Board of actions:
        #   0 = no move
        #   1 = Player 1
        #   2 = Player 2
        self.board = self.create_board()

    def state(self):
        return self.board

    def action(self, player, x, y):
        self.board[ y, x ] = player

    def cell(self, x, y):
        return self.board[ y, x ]

    def horizontal(self, x, y):
        return self.board [ y, x : self.in_a_row + x ]

    def vertical(self, x, y):
        return self.board [ y : self.in_a_row + y, x ]

    def diag(self, x, y):
        a = np.zeros(0, np.int8)

        for z in range(self.in_a_row):
            ax = x + z
            ay = y + z
            if ax < self.board_size and ay < self.board_size:
                a = np.append(a, self.board[ay, ax])

        return a

    def test(self):
        self.action(2, 0, 3)
        self.action(2, 1, 2)
        self.action(2, 2, 1)

    def downdiag(self, x, y):
        a = np.zeros(0, np.int8)

        for z in range(self.in_a_row):
            ax = x - z
            ay = y + z
            if ax >= 0 and ay < self.board_size:
                a = np.append(a, self.board[ay, ax])

        return a

    def empty(self):
        a = np.zeros(0, np.int8)
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.cell(x, y) == 0:
                    a = np.append(a, y * self.board_size + x)
        return np.sort(a)

    def possible_moves(self):
        a = self.create_board()
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.cell(x, y) == 0:
                    a[ y, x ]  = 1
        return a

    def reward_board(self, reward, x, y):
        a = self.create_board()
        a[ y, x ] = reward
        return a

    def create_target(self, board, reward):
        a = board.astype(np.float32)
        for x in range(a.shape[0]):
            for y in range(a.shape[1]):
                if a[x, y] > 0:
                    a[x, y] = reward
        return a

    def move(self, player, number):
        rest = number % self.board_size
        x = 0
        y = 0

        if number >= self.board_size:
            y = (number - rest) / self.board_size
            x = rest
        else:
            y = 0
            x = rest
        x = int(x)
        y = int(y)
        self.action(player, x, y)

        return self.reward_board(1, x, y)

    def winner(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                horizontal = self.horizontal(x, y)
                vertical = self.vertical(x, y)
                diag = self.diag(x, y)
                downdiag = self.downdiag(x, y)

                if horizontal.shape[0] == self.in_a_row:
                    if np.array_equal( horizontal, np.full(self.in_a_row, 1) ):
                        # Player one !
                        print('horizontal', horizontal)
                        return 1
                    if np.array_equal( horizontal, np.full(self.in_a_row, 2) ):
                        # Player two !
                        print('horizontal', horizontal)
                        return 2

                if vertical.shape[0] == self.in_a_row:
                    if np.array_equal( vertical, np.full(self.in_a_row, 1) ):
                        # Player one !
                        print('vertical', vertical)
                        return 1
                    if np.array_equal( vertical, np.full(self.in_a_row, 2) ):
                        # Player two !
                        print('vertical', vertical)
                        return 2

                if diag.shape[0] == self.in_a_row:
                    if np.array_equal( diag, np.full(self.in_a_row, 1) ):
                        # Player one !
                        print('diag', vertical)
                        return 1
                    if np.array_equal( diag, np.full(self.in_a_row, 2) ):
                        # Player two !
                        print('diag', diag)
                        return 2

                if downdiag.shape[0] == self.in_a_row:
                    if np.array_equal( downdiag, np.full(self.in_a_row, 1) ):
                        # Player one !
                        print('downdiag', vertical)
                        return 1
                    if np.array_equal( downdiag, np.full(self.in_a_row, 2) ):
                        # Player two !
                        print('downdiag', downdiag)
                        return 2
        return 0

if __name__ == '__main__':
    l = LuffarSchack()
