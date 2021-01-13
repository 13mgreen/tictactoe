# whos turn x/o
x_turn = True
state = [" "] * 9


def check_winner():

    if x_turn:
        winner = "X"
    else:
        winner = "O"

    # horizontal win
    if state[0] == winner and state[1] == winner and state[2] == winner:
        return winner

    if state[3] == winner and state[4] == winner and state[5] == winner:
        return winner

    if state[6] == winner and state[7] == winner and state[8] == winner:
        return winner

    # vertical win
    if state[0] == winner and state[3] == winner and state[6] == winner:
        return winner

    if state[1] == winner and state[4] == winner and state[7] == winner:
        return winner

    if state[2] == winner and state[5] == winner and state[8] == winner:
        return winner

    # diagonal win
    if state[0] == winner and state[4] == winner and state[8] == winner:
        return winner

    if state[2] == winner and state[4] == winner and state[6] == winner:
        return winner

    return "N"


# keep running until game is over
is_playing = True
while is_playing:

    # get p1 input X
    position = int(input("Enter board position from 0-8: "))

    if x_turn == True:
        state[position] = "X"
    else:
        state[position] = "O"

    # print board
    print(
        f" {state[0]} | {state[1]} | {state[2]} \n"
        f"-----------\n"
        f" {state[3]} | {state[4]} | {state[5]} \n"
        f"-----------\n"
        f" {state[6]} | {state[7]} | {state[8]} \n"
    )

    # check if win/loss
    winner = check_winner()

    if winner != "N":
        is_playing = False
        print(f"{winner} won the game!")
    else:
        x_turn = not x_turn
