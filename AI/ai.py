import copy
import random
from math import inf


class ai:
    def __init__(self, board):
        self.board = board
        self.score = 0

    def winning_move(self):
        """
        Determines if the AI can make a move to win the game
        :return: the coordinates of the move or false if the move is not a winning move
        """
        # xy = []
        # new_board = copy.deepcopy(self.board)
        # for x in range(self.board.lines):
        #     for y in range(self.board.columns):
        #         new_board.set_move(x, y, 'O')
        #         if not new_board.empty_cells():
        #             xy.append(x)
        #             xy.append(y)
        # if xy:
        #     return xy
        # else:
        #     return False
        new_board = copy.deepcopy(self.board)
        for x,y in new_board.empty_cells():
            new_board.set_move(x,y,'O')
            if self.ai_wins(new_board):
                return x,y
            new_board.set_value(x,y,' ')
            new_board.undo_last_move()
        return False



    def random_move(self):
        """
        Randomly makes a move on the board
        :return:
        """
        x = -1
        y = -1
        while self.board.valid_move(x, y) is False:
            x = random.choice(range(0, self.board.lines))
            y = random.choice(range(0, self.board.columns))

        self.board.set_move(x, y, 'O')

    def ai_wins(self, state):
        """
        Checks if the AI wins
        Used only for the minimax algorithm
        :param state: the current state of the board
        :return: returns true if the AI wins the game, else it returns false
        """
        if self.game_over(state):
            if state.get_last_player() == 'O':
                return True
            else:
                return False

    def evaluate(self, state):
        """
        Adds one point to the score of the AI if the AI wins the game, else it subtracts one.
        :param state: the current state of the board
        :return: The score of the AI
        """
        if self.ai_wins(state):
            score = +1
        else:
            score = -1
        return score

    def game_over(self, state):
        """
        Checks if the game in a particular state is over
        :param state: the current state of the board
        :return: True if the game is over
        """
        if not state.empty_cells():
            return True

    def minimax(self,state,depth,player):
        """
        Minimax algorithm
        It checks all the possible ways of a game to be played given the current state of the board and returns 1 if the computer wins, or -1 if the player wins
        :param state: the current state of the board
        :param depth: the number of empty cells in the board
        :param player: the current player, 1 for the computer (O) and -1 for player (X)
        :return: 1 if the computer wins, -1 if the player wins
        """
        if depth == 0 or self.game_over(state):
            score=self.evaluate(state)
            return score

        if player == 1:
            best=-inf
            for cell in state.empty_cells():
                state.set_move(cell[0],cell[1],'O')
                best=max(best,self.minimax(state,depth - 1, -1))
                state.set_value(cell[0], cell[1], ' ')
                state.undo_last_move()

            return best

        else:
            best = inf
            for cell in state.empty_cells():
                state.set_move(cell[0], cell[1], 'X')
                best = min(best, self.minimax(state, depth - 1, 1))
                state.set_value(cell[0], cell[1], ' ')
                state.undo_last_move()
            return best



    def find_best_move(self,state,depth):
        """
        Finds the best possible move for the computer using the minimax function
        :param state: the current state of the board
        :param depth: the number of empty cells on the board
        :return: a list containing the best possible move
        """
        bestVal=-inf
        bestMove=[-inf,-inf]

        for cell in state.empty_cells():
            x,y=cell[0],cell[1]
            state.set_move(x,y,"O")
            value=self.minimax(state,depth,-1)
            state.set_value(cell[0], cell[1], ' ')
            state.undo_last_move()

            if value > bestVal:
                bestMove=[x,y]
                bestVal=value
        return bestMove