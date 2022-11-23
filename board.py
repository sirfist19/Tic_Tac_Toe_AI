import os 

class Board:
    def __init__(self):
        self.empty_char = '.'
        self.contents = [[self.empty_char for i in range(3)] for j in range(3)]
        self.x_turn = True
        self.x_won = False
        self.o_won = False
        self.tie = False

    def place_piece(self, coord):
        if self.x_turn:
            piece_to_place = 'X'
        else:
            piece_to_place = 'O'
        
        if self.square_is_empty(coord):
            #place the piece
            self.contents[coord[0]][coord[1]] = piece_to_place
            return True
        return False
    def display(self):
        for i in range(3):
            for j in range(3):
                print(self.contents[i][j], end = " ")
            print()

    def win_condition(self):
        if self.board_is_full():
            self.tie = True
        
        #check to see if either player has 3 in a row
        lines = [
            self.contents[0],
            self.contents[1], 
            self.contents[2],
            [self.contents[i][0] for i in range(3)],
            [self.contents[i][1] for i in range(3)],
            [self.contents[i][2] for i in range(3)],
            [self.contents[i][i] for i in range(3)],
            [self.contents[2-i][i] for i in range(3)]
            ]
        #print(lines)
        for line in lines:
            res = self.check_line(line)
            
            if res == "none":
                continue
            elif res == "X wins":
                self.x_won = True
                self.tie = False
                break
            elif res == "O wins":
                self.o_won = True
                self.tie = False
                break

    def board_is_full(self):
        for i in range(3):
            for j in range(3):
                if self.contents[i][j] == self.empty_char:
                    return False
        return True

    def check_line(self, line):
        if line == ['X', 'X', 'X']:
            return "X wins"
        elif line == ['O', 'O', 'O']:
            return "O wins"
        return "none"

    def square_is_empty(self, coord):
        contents = self.contents[coord[0]][coord[1]]
        if contents == self.empty_char:
            return True
        return False

#essential functions ________________________________________________________________________________________________________
def square_ind_to_coord(square_ind):
    #takes in indices 1 to 9
    #1 is the top left square
    #9 is the bottom right square
    #3 is the top right square
    return [(square_ind - 1) // 3, (square_ind - 1) % 3]

def valid_input(text):
    if text.isnumeric() and int(text) > 0 and int(text) < 10:
        return True
    return False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')