# whos turn x/o

# keep running until game is over

# get p1 input X

# print board

# check if win/loss


class TicTacToeBoard:
    def __init__(self):
        self.state = [" "] * 9

    def print(self):
        print(
            f" {self.state[0]} | {self.state[1]} | {self.state[2]} \n"
            f"-----------\n"
            f" {self.state[3]} | {self.state[4]} | {self.state[5]} \n"
            f"-----------\n"
            f" {self.state[6]} | {self.state[7]} | {self.state[8]} \n"
        )

    def choose_square(self, position, value):
        self.state[position] = value


class TicTacToeGame:
    def __init__(self):
        self.board = TicTacToeBoard()
        self.x_turn = True
        self.is_playing = True

    def play_turn(self):
        position = int(input("Enter board position from 0-8: "))

        if self.x_turn == True:
            self.board.choose_square(position, "X")
        else:
            self.board.choose_square(position, "O")

        self.board.print()
        winner = self.check_winner()

        if winner != "N":
            self.is_playing = False
            print(f"{winner} won the game!")
        else:
            self.x_turn = not self.x_turn

    def check_winner(self):

        if self.x_turn:
            winner = "X"
        else:
            winner = "O"

        # horizontal win
        if (
            self.board.state[0] == winner
            and self.board.state[1] == winner
            and self.board.state[2] == winner
        ):
            return winner

        if (
            self.board.state[3] == winner
            and self.board.state[4] == winner
            and self.board.state[5] == winner
        ):
            return winner

        if (
            self.board.state[6] == winner
            and self.board.state[7] == winner
            and self.board.state[8] == winner
        ):
            return winner

        # vertical win
        if (
            self.board.state[0] == winner
            and self.board.state[3] == winner
            and self.board.state[6] == winner
        ):
            return winner

        if (
            self.board.state[1] == winner
            and self.board.state[4] == winner
            and self.board.state[7] == winner
        ):
            return winner

        if (
            self.board.state[2] == winner
            and self.board.state[5] == winner
            and self.board.state[8] == winner
        ):
            return winner

        # diagonal win
        if (
            self.board.state[0] == winner
            and self.board.state[4] == winner
            and self.board.state[8] == winner
        ):
            return winner

        if (
            self.board.state[2] == winner
            and self.board.state[4] == winner
            and self.board.state[6] == winner
        ):
            return winner

        return "N"


game = TicTacToeGame()

while game.is_playing:
    game.play_turn()