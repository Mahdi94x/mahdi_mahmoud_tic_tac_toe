# Reference Used:
# https://electropi.ai/lessons/python-programming-master/lessons-3-functions/capstone-tic-tac-toe
# https://www.youtube.com/watch?v=dK6gJw4-NCo&t=1276s
# https://www.youtube.com/watch?v=Q6CCdCBVypg&t=192s

board = ["1", "2", "3",
              "4", "5", "6",
              "7", "8", "9"]
player = "X"
playing = True
theWinner = None
symbols = ["X", "O"]


def print_board(board):
    print("  |  " + board[0] + "  |  " + board[1] +
          "  |  " + board[2] + "  |  " + "\n")
    print("  |  " + board[3] + "  |  " + board[4] +
          "  |  " + board[5] + "  |  " + "\n")
    print("  |  " + board[6] + "  |  " +
          board[7] + "  |  " + board[8] + "  |  ")


def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def tic_tac_toe(board):
    try:
        print(f"The next move belongs to player {player}...")
        question = int(input("Please Enter a number between 1 to 9 => "))   
        if question >= 1 and question <= 9 and board[question-1] not in symbols:
            board[question-1] = player
            switch_player()
        else:
            print(f"Error, spot {question} is taken, please choose another spot")
    except ValueError:  
        print("Error, the input is not a number, Please Enter a number between 1 to 9 => ")  

     
def check_win_tie(board):

    # Horizontal

    global theWinner
    global playing

    if board[0] in symbols:
        if board[0] == board[1] == board[2]:
            theWinner = board[0]
            print_board(board)
            print(f"The winner is player {board[0]}, Congratulations.")
            playing = False

        if board[3] in symbols:
            if board[3] == board[4] == board[5]:
                theWinner = board[3]
                print_board(board)
                print(f"The winner is player {board[3]}, Congratulations.")
                playing = False

        if board[6] in symbols:
            if board[6] == board[7] == board[8]:
                theWinner = board[6]
                print_board(board)
                print(f"The winner is player {board[6]}, Congratulations.")
                playing = False

    # Vertical

        if board[0] in symbols:
            if board[0] == board[3] == board[6]:
                theWinner = board[0]
                print_board(board)
                print(f"The winner is player {board[0]}, Congratulations.")
                playing = False

        if board[1] in symbols:
            if board[1] == board[4] == board[7]:
                theWinner = board[1]
                print_board(board)
                print(f"The winner is player {board[1]}, Congratulations.")
                playing = False

        if board[2] in symbols:
            if board[2] == board[5] == board[8]:
                theWinner = board[2]
                print_board(board)
                print(f"The winner is player {board[2]}, Congratulations.")
                playing = False

    # Diagonal

        if board[0] in symbols:
            if board[0] == board[4] == board[8]:
                theWinner = board[0]
                print_board(board)
                print(f"The winner is player {board[0]}, Congratulations.")
                playing = False

        if board[2] in symbols:
            if board[2] == board[4] == board[6]:
                theWinner = board[2]
                print_board(board)
                print(f"The winner is player {board[2]}, Congratulations.")
                playing = False

    else:  # Tie Case
        print_board(board)
        print("It is a Tie")
        playing = False


def master_function():
    while playing:
        print_board(board)
        tic_tac_toe(board)
        check_win_tie(board)
    else:
        print("Thank you for playing! ")

master_function()
