the_board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}


def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0

    have_game = True

    while have_game:
        print_board(the_board)
        print(f"It`s your turn, {turn}. Move to which place?")

        try:
            move = int(input())
        except ValueError:
            print("Pressed a wrong key.\n")
            continue

        if move >= 10 or move <= 0:
            print("Pressed a number too high.\n")
            continue

        move = str(move)

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled. \n Move to which place?")
            continue

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ': #top
                who_won(turn)
                break

            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                who_won(turn)
                break

            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                who_won(turn)
                break

            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                who_won(turn)
                break

            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                who_won(turn)
                break

            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                who_won(turn)
                break

            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                who_won(turn)
                break

            elif the_board['3'] == the_board['5'] == the_board['7'] != ' ':
                who_won(turn)
                break

        if count == 9:
            print("\nGame Over.\n")
            print("Its a tie.")
            have_game = False

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


def who_won(winner):
    print_board(the_board)
    print("\nGame Over.\n")
    print(f" **** {winner} Won. ****")
    have_game = False


game()
