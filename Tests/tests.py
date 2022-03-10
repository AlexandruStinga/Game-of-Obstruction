import unittest
from AI.ai import ai
from Board.board import board
from Game.game import game,InvalidMove

class TestAI(unittest.TestCase):

    def test_winning_move(self):
        Board=board(3,3)
        AI=ai(Board)
        self.assertEqual(AI.winning_move(),(1,1))

    def test_find_best_move(self):
        Board=board(3,3)
        AI=ai(Board)
        self.assertEqual(AI.find_best_move(Board,9),[1,1])

        board2=board(4,4)
        AI2=ai(board2)
        self.assertEqual(AI2.find_best_move(board2,25),[0,0])

class TestGame(unittest.TestCase):

    def test_move_player(self):
        Board=board(3,3)
        AI=ai(Board)
        Game=game(Board,AI)
        Game.movePlayer([0,0])
        self.assertEqual(Board[0][0],'X')
        self.assertRaises(InvalidMove,Game.movePlayer,[0,0])

    def test_move_computer(self):
        Board = board(3, 3)
        AI = ai(Board)
        Game = game(Board, AI)
        Game.moveComputer()
        self.assertEqual(Board[1][1],'O')

    def test_game_win(self):
        Board = board(3, 3)
        AI = ai(Board)
        Game = game(Board, AI)
        Game.moveComputer()
        self.assertEqual(Board[1][1], 'O')
        self.assertEqual(Game.game_win(),False)

        Board_x = board(3, 3)
        AI_x = ai(Board_x)
        Game_x = game(Board_x, AI_x)
        Game_x.movePlayer([0, 0])
        self.assertEqual(Game_x.game_win(), True)

class TestBoard(unittest.TestCase):

    def test_empty_cells(self):
        Board=board(3,3)
        cells=Board.empty_cells()
        self.assertEqual(len(cells),9)

        Board = board(6, 6)
        cells = Board.empty_cells()
        self.assertEqual(len(cells), 36)

    def test_valid_move(self):
        Board = board(3, 3)
        cells = Board.empty_cells()
        self.assertEqual(len(cells), 9)
        self.assertEqual(Board.valid_move(0,0),True)

        AI = ai(Board)
        Game = game(Board, AI)
        Game.movePlayer([0,0])
        self.assertEqual(Board.valid_move(0,0),False)

    def test_set_move(self):
        Board=board(3,3)
        Board.set_move(0,0,'X')
        self.assertEqual(Board[0][0], 'X')
        self.assertEqual(Board[0][1], '-')
        self.assertEqual(Board[1][0], '-')
        self.assertEqual(Board[1][1], '-')

    def test_set_value(self):
        Board=board(3,3)
        Board.set_move(0, 0, 'X')
        self.assertEqual(Board[0][0], 'X')
        self.assertEqual(Board[0][1], '-')
        Board.set_value(0,1,' ')
        self.assertEqual(Board[0][1], ' ')

    def test_get_last_player(self):
        Board = board(4, 4)
        Board.set_move(0, 0, 'X')
        self.assertEqual(Board.get_last_player(),'X')

        Board.set_move(3,3,'O')
        self.assertEqual(Board.get_last_player(),'O')

    def test_undo_last_move(self):
        Board = board(4, 4)
        Board.set_move(2, 2, 'X')
        self.assertEqual(Board[1][1],'-')

        Board.undo_last_move()
        self.assertEqual(Board[1][1],' ')

