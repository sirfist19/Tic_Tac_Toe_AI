from board import *
import copy

class Node:
    def __init__(self, board, move = "none"):
        self.eval = "none" #the evaluation of the Node's position
        self.board = board
        self.move = move #the move it took to get to this node
        self.next_nodes = []
        self.set_next_nodes()

    def set_next_nodes(self):
        #if a player has already won the board then set next nodes to []
        self.board.win_condition() #check for win conditions
        if self.board.x_won:
            self.eval = 1
            return []
        elif self.board.o_won:
            self.eval = -1
            return []
        elif self.board.tie:
            self.eval = 0
            return []

        #generates all possible boards 1 move in advance
        next_nodes = []
        for i in range(1,10): #i is the square to try placing a piece
            new_board = copy.deepcopy(self.board)
            coord = square_ind_to_coord(i)
            if new_board.place_piece(coord):
                new_board.x_turn = not new_board.x_turn
                next_nodes.append(Node(new_board, i))
        self.next_nodes = next_nodes
        self.set_eval()

    def set_eval(self):
        if not self.next_nodes:
            return

        #sets the evaluation value based on the next_nodes
        evals = [next_node.eval for next_node in self.next_nodes]
        if self.board.x_turn:
            #maximize toward positive
            self.eval = max(evals)
        else:
            self.eval = min(evals)

    def find_AI_move(self):
        if not self.next_nodes:
            return #no move is needed if the game is already over

        if self.board.x_turn:
            max_val = -100
            for next_node in self.next_nodes:
                #maximize
                if next_node.eval > max_val:
                    max_val = next_node.eval
                    self.move = next_node.move
        else: #o's turn
            min_val = 100
            for next_node in self.next_nodes:
                #minimize
                if next_node.eval < min_val:
                    min_val = next_node.eval
                    self.move = next_node.move

    def display(self):
        #clear()
        print("Displaying self:")
        print(self.eval)
        print("Move:", end = " ")
        print(self.move)
        self.board.display()
        
        print("Display next states")
        for node in self.next_nodes:
            node.display()
            print()
        print("Done")

    
#the AI
class AI:
    def __init__(self, root_board):
        self.search_tree = self.generate_search_tree(root_board)
        self.cur_board = root_board
    
    def generate_search_tree(self, root_board):
        root_board_copy = copy.deepcopy(root_board)
        root = Node(root_board_copy)
        root.find_AI_move()
        return root

    def display_search_tree(self):
        self.search_tree.display()
    
    def make_AI_move(self):
        coord = square_ind_to_coord(self.search_tree.move)
        placed_piece = self.cur_board.place_piece(coord)
        if placed_piece:
            self.cur_board.x_turn = not self.cur_board.x_turn

        #generate the new search tree based on the new board
        self.search_tree = self.generate_search_tree(self.cur_board)

    def print_top_level_eval(self):
        print("Top level eval is ", end = " ")
        print(self.search_tree.eval)

    def print_top_level_move(self):
        print("The AI moved to", end = " ")
        print(self.search_tree.move)
    