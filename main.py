from UI.UI import UI
from Board.board import board
from Game.game import game
from AI.ai import ai
if __name__ == '__main__':
    player=-1
    size=UI.read_size()
    board=board(size[0],size[1])
    ai=ai(board)
    game=game(board,ai)
    ui = UI(board,game,player)
    ui.start()