# This program only runs in IPython,  Juyper Notebook is the best way to do it


from IPython.display import clear_output


def display_board(board):
    #clear_output()  # Remember, this only works in jupyter!
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('--------------')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('--------------')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])


def win(board, mark):
    '''
    check win status
    return True then win
    '''
    # check the row to verify if it is connected
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            # check the column to verify if it is connected
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            # check the diagonal to verify if it is connected
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


import math
import random


def who_is_first():
    if random.randint(0, 1) == 0:
        return ('Player 1')
    else:
        return ('Player 2')


def board_poistion(board, poistion, mark):
    board[poistion] = mark


def there_is_space(board):
    if (' ' in board):
        return True
    else:
        return False


def check_poistion(board):
    poistion = 0
    while (there_is_space(board)):
        P = input()
        if P in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            poistion = int(P)
            if board[poistion] != ' ':
                print(f'{poistion} is occupied, Please select other place ')
                continue
            else:
                break
        else:
            print('Please Input Number 1 to 9')

    return poistion


#-----------------------------------------------------------
def PlayGame():
    '''
    Main program to execute
    '''
    print('Welcome to Game\n')
    print('Do you wanna play ?')
    game_on = False
    while (input().lower() != 'yes'):
        print('If you want to play, Please input Yes')

    game_on = True

    while game_on:
        first_play = who_is_first()
        print(f'{first_play} go first')
        game_board = [' '] * 10
        game_board[0] = '#'
        display_board(game_board)
    # while True:
        while(True):
            # Player1's Turn
            if (there_is_space(game_board)):
                print('Please Player 1 input position\n')
                #poistion = int(input())
                game_poistion = check_poistion(game_board)
                board_poistion(game_board, game_poistion, 'X')
                display_board(game_board)
                if (win(game_board, 'X')):
                    print('Player 1 Win')
                    break
            else:
                print('Tie Game')
                break

        # Player2's Turn
            if (there_is_space(game_board)):
                print('Please Player 2 input position')
                #poistion = int(input())
                board_poistion(game_board, check_poistion(game_board), 'O')
                display_board(game_board)
                if(win(game_board, 'O')):
                    print('Player 2 Win')
                    break
            else:
                print('Tie Game')
                break

        print('Do You Wanna Play Again ?')
        if (input().lower() != 'yes'):
            break



# Game Start
PlayGame()
