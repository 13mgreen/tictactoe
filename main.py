# whos turn x/o

# keep running until game is over

# get p1 input X

# print board

# check if win/loss


class TicTacToeBoard:
    def __init__(self):
        self.board = [" "] * 9

    def print(self):
        print(
            f" {self.board[0]} | {self.board[1]} | {self.board[2]} \n"
            f"-----------\n"
            f" {self.board[3]} | {self.board[4]} | {self.board[5]} \n"
            f"-----------\n"
            f" {self.board[6]} | {self.board[7]} | {self.board[8]} \n"
        )


board = TicTacToeBoard()

board.print()
