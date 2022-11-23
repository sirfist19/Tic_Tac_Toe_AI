#from board import *
from ai import *

#main game loop section ______________________________________________________________________________________________________
print("Welcome to Tic Tac Toe with AI!")
print("Do you want to play X or O?")
input_valid = False
player_is_x = True #default value
while not input_valid:
    text = input()
    if text == 'X' or text == 'x':
        #player_is_x = True
        input_valid = True
    elif text == 'o' or text == 'O':
        player_is_x = False
        input_valid = True
    else:
        #invalid input
        print("Please type either 'X' or 'O'")
        
board = Board()
#board.contents = [
#    ['O', 'O', 'X'],
#    ['.', 'X', '.'],
#    ['.', 'X', 'O']
#]
#board.x_turn = False
#board.contents = [
#    ['O', '.', '.'],
#    ['.', 'X', '.'],
#    ['.', '.', 'O']
#]

while (not board.x_won) and (not board.o_won) and (not board.tie):
    #clear()
    board.display()

    if (board.x_turn and player_is_x) or (not board.x_turn and not player_is_x): #player's turn
        if board.x_turn:
            print("Place an X by typing the square you want to put a piece on")
        else:
            print("Place an O by typing the square you want to put a piece on")

        text = input()
        
        if valid_input(text):
            text = int(text)
            coord = square_ind_to_coord(text)
            placed_piece = board.place_piece(coord)
            if placed_piece:
                board.x_turn = not board.x_turn
    else: #AI's turn
        ai = AI(board)
        ai.print_top_level_move()
        ai.make_AI_move()
        ai.print_top_level_eval()

    board.win_condition()

clear()
board.display()
if board.x_won:
    print("X got 3 in a row!")
elif board.o_won:
    print("O got 3 in a row!")
else:
    print("Tied game.")

