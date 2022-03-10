from AI.ai import ai
from copy import deepcopy
class InvalidMove(Exception):
    pass

class game:
    def __init__(self,board,ai):
        self.board=board
        self.ai=ai

    def movePlayer(self,pos):
        """
        Determines if pos is a valid move and then sets that move on the board
        :param pos: the position of the move
        :raises: InvalidMove if the move is not valid
        """
        if self.board.valid_move(pos[0],pos[1]):
            self.board.set_move(pos[0],pos[1],'X')
        else:
            raise InvalidMove


    def moveComputer(self):
        """
        Calls the minimax function so that the computer makes a move
        :param player: current player
        """
        # depth=len(self.board.empty_cells())
        # if depth == 0:
            #     return

        minmax = deepcopy(self.board)
        depth = len(minmax.empty_cells())

        if depth > 16:
              self.ai.random_move()
        else:
            move=self.ai.find_best_move(minmax,depth)
            x,y=move[0],move[1]
            self.board.set_move(x,y,'O')

        # if self.ai.winning_move() != False:
        #     x,y=self.ai.winning_move()
        #     self.board.set_move(x,y,'O')
        # else:
        #     self.ai.random_move()


    def game_win(self):
        """
        Determines who wins the game
        :return:
        """
        if self.board.get_last_player() == 'X':
            return True
        else:
            return False

        # if counter == 1:
        #     return True
        # else:
        #     return False