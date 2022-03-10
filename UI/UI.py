from Board.board import board
from Game.game import game, InvalidMove

class UI:
    def __init__(self,board,game,player):
        self.board = board
        self.game = game
        self.player=player

    @staticmethod
    def read_size():
        """
        Function to read the size of the board
        :return:
        """
        while True:
            print("Please specify the size of the board")
            try:
                line=int(input("Number of lines: "))
                column=int(input("Number of columns: "))
                break
            except Exception:
                print("Invalid data. Please input numbers.")

        return [line, column]

    def start(self):
        while True:
            try:
                option = int(input("Who do you want to start? 1-You 2-Computer: "))
                break
            except Exception:
                print("Please specify a number")

        if option == 1:
            self.player = -1
        else:
            self.player = 1

        while self.board.empty_cells():
            print(self.board)
            if self.player == 1:
                self.game.moveComputer()
                self.player = -1
            else:
                print("Specify a position: ")
                while True:
                    try:
                        line = int(input("Line: "))
                        column = int(input("Column: "))
                        break
                    except Exception:
                        print("Please specify a number")

                pos = [line-1,column-1]
                try:
                   self.game.movePlayer(pos)
                   self.player = 1
                except InvalidMove:
                   print("Invalid position")

        print(self.board)
        if self.game.game_win() == True:
            print("You win")
        else:
            print("Computer wins!")
