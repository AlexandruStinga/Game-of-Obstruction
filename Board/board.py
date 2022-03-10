import texttable


class board:
    def __init__(self, lines, columns):
        self.board = []
        self.lines = lines
        self.columns = columns
        for line in range(lines):
            self.board.append([])
            for column in range(columns):
                self.board[line].append(' ')
        self.history = []
        self.history_index = 0

    def empty_cells(self):
        """
        Puts all the empty cells on the board in a list
        :return: the list containing the coordinates of the empty cells in the board
        """
        cells=[]
        for i in range(self.lines):
            for j in range(self.columns):
                if self.board[i][j] == ' ':
                    cells.append([i,j])
        return cells

    def valid_move(self, x, y):
        """
        Determines if a move is a valid one
        :param x: the x coordinate (row)
        :param y: the y coordinate (column)
        :return: True if the move is valid
                 False if the move is not valid
        """
        if [x, y] in self.empty_cells():
            return True
        else:
            return False

    def set_move(self, x, y, player):
        """
        Makes the move corresponding to the given coordinates on the board.
        :param x: the x coordinate (row)
        :param y: the y coordinate (column)
        :param player: the current player (X for player, O for computer)
        """
        if self.valid_move(x, y):
            self.history.append([player])
            if 1 <= x < self.lines:
                if self.board[x-1][y] == ' ':
                    self.board[x - 1][y] = '-'
                    self.history[self.history_index].append([x - 1, y])
            if 0 <= x < self.lines - 1:
                if self.board[x + 1][y] == ' ':
                    self.board[x + 1][y] = '-'
                    self.history[self.history_index].append([x + 1, y])

            if 1 <= y < self.columns:
                if self.board[x][y - 1] == ' ':
                    self.board[x][y - 1] = '-'
                    self.history[self.history_index].append([x, y-1])
            if 0 <= y < self.columns - 1:
                if self.board[x][y + 1] == ' ':
                    self.board[x][y + 1] = '-'
                    self.history[self.history_index].append([x, y+1])

            if 1 <= x < self.lines and 0 <= y < self.columns - 1:
                if self.board[x - 1][y + 1] == ' ':
                    self.board[x - 1][y + 1] = '-'
                    self.history[self.history_index].append([x - 1, y + 1])
            if 1 <= x < self.lines and 1 <= y < self.columns:
                if self.board[x - 1][y - 1] == ' ':
                    self.board[x - 1][y - 1] = '-'
                    self.history[self.history_index].append([x - 1, y - 1])

            if 0 <= x < self.lines - 1 and 1 <= y < self.columns:
                if self.board[x + 1][y - 1] == ' ':
                    self.board[x + 1][y - 1] = '-'
                    self.history[self.history_index].append([x + 1, y - 1])
            if 0 <= x < self.lines - 1 and 0 <= y < self.columns - 1:
                if self.board[x + 1][y + 1] == ' ':
                    self.board[x + 1][y + 1] = '-'
                    self.history[self.history_index].append([x + 1, y + 1])

            self.history_index+=1
            self.board[x][y] = player

    def set_value(self, x, y, value):
        """
        Function for setting a given value on the board
        :param x: x coordinate (row)
        :param y: y coordinate (column)
        :param value: the value to set on the board
        """
        self.board[x][y] = value
        if value != ' ':
            self.history.append(value)

    def get_last_player(self):
        """
        Function to determine the last player to have made a move
        :return: returns the last player to have made a move
        """
        return self.history[-1][0]

    # def board_equals_minus(self, x, y):
    #     """
    #
    #     :param x:
    #     :param y:
    #     :return:
    #     """
    #     if self.board[x][y] == '-':
    #         return True
    #     else:
    #         return False

    def undo_last_move(self):
        """
        Replaces all '-' from a move, to spaces
        :return:
        """
        for i in range(1,len(self.history[-1])):
            self.board[self.history[-1][i][0]][self.history[-1][i][1]] = ' '
        self.history.pop()
        self.history_index-=1


    def __getitem__(self,index):
        return self.board[index]

    def __str__(self):
        """
        Prints the board in a nicer way using texttable
        :return: the printing method from texttable
        """
        t = texttable.Texttable()
        header = [' ']
        for h in range(self.columns):
            header.append(str(h + 1))
        t.header(header)

        for row in range(self.lines):
            data = []
            for val in self.board[row]:
                data.append(str(val))

            t.add_row([row + 1] + data)
        return t.draw()
