import pygame
from .constants import *
from .board import *
from .piece import *

class Game:
    # Initiliase a new game
    def __init__(self, win):
        self._init()
        self.win = win
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    # Update the state of the game
    def update(self):
        self.board.draw(self.win, self.turn)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # Reset the game
    def reset(self):
        self._init()
    
    # function to check the number of pieces on the board
    def count_board(self):
        count = 0
        for row in range(GYWR1, ROWS - 3):
            for col in range(COLS):
                if self.board.board[row][col] != 0:
                    count += 1
        return count

    # Select something and determine whether we can do anything after
    def select(self, row, col, positioning):
        if self.selected:
            result = self._move(row, col, positioning)
            if not result:
                self.selected = None
                self.select(row, col, positioning)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.colour == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece, positioning)
            return True
        
        # If the done button is selected then change turn
        # Note that this is only available during the positioning stage of the game
        if positioning and (row == finished_positioning_row and col == finished_positioning_col):
            self.change_turn()

        return False
    
    def move_to_graveyard(self, piece):
        pass
        # if piece.colour == WHITE:
        #     for row in range(GYWR1):
        #         for col in range(COLS):
        #             if self.board.board[row][col] == 0:
        #                 self.board.board[row][col] = piece
        #                 return
        # elif piece.colour == BLACK:
        #     for row in range(GYBR1, ROWS):
        #         for col in range(COLS):
        #             if self.board.board[row][col] == 0:
        #                 self.board.board[row][col] = piece
        #                 return
    
    def dead_piece(self, piece):
        self.board.board[piece.row][piece.col] = 0

        if piece != 0:
            if piece.colour == WHITE:
                self.board.num_white_pieces -= 1
            else:
                self.board.num_black_pieces -= 1
            if piece.power_level == 1 and piece.colour == BLACK:
                self.board.num_black_flag -= 1
            elif piece.power_level == 1 and piece.colour == WHITE:
                self.board.num_white_flag -= 1

    def winner(self):
        if self.board.num_white_pieces <= 0:
            print("Black wins")
            return True
        elif self.board.num_black_pieces <= 0:
            print("White wins")
            return True
        if self.board.num_white_flag <= 0:
            print("Black wins")
            return True
        elif self.board.num_black_flag <= 0:
            print("White wins")
            return True
        for col in range(COLS):
            if self.board.board[3][col] != 0 and  self.board.board[3][col].rank == FlagBlack:
                print("Black wins")
                return True
            
            if self.board.board[ROWS - 4][col] != 0 and  self.board.board[ROWS - 4][col].rank == FlagWhite:
                print("White wins")
                return True

        
        
        return False

    def _move(self, row, col, positioning):
        # note that row, col are the coords of the position we want to move to
        opponent_piece = self.board.get_piece(row, col) # this is the new position we want to move to.
        
        # Can only move to a spot that is in valid_moves
        # note that self.selected is the current piece we want to move
        if self.selected and (row, col) in self.valid_moves:
            # the case where there is an empty spot, meaning you can freely move there
            if opponent_piece == 0:
                self.board.move(self.selected, row, col)
        
            # the case where there is an enemy piece in the way
            # check the outcome of battle
            else:
                # The case where they are both the flag
                if self.selected.power_level == 1 and opponent_piece.power_level == 1:
                    self.move_to_graveyard(opponent_piece)
                    self.dead_piece(opponent_piece) # opponent piece dies
                    self.board.move(self.selected, row, col)
                
                # The case where they are both the same piece, both of them get eliminated
                elif self.selected.power_level == opponent_piece.power_level:
                    self.move_to_graveyard(opponent_piece)
                    self.move_to_graveyard(self.selected)
                    self.dead_piece(opponent_piece) # opponent piece dies
                    self.dead_piece(self.selected) # selected piece dies

                # Check the case where it is spy vs private
                elif self.selected.power_level == 15 and opponent_piece.power_level == 2:
                    self.move_to_graveyard(self.selected)
                    self.dead_piece(self.selected) # selected piece dies

                elif self.selected.power_level == 2 and opponent_piece.power_level == 15:
                    self.move_to_graveyard(opponent_piece)
                    self.dead_piece(opponent_piece) # opponent piece dies
                    self.board.move(self.selected, row, col)
                
                # Check the case where the piece is higher rank
                elif self.selected.power_level > opponent_piece.power_level:
                    self.move_to_graveyard(opponent_piece)
                    self.dead_piece(opponent_piece) # opponent piece dies
                    self.board.move(self.selected, row, col)
                
                # The case where the opponent piece is a higher rank
                elif self.selected.power_level < opponent_piece.power_level:
                    self.move_to_graveyard(self.selected)
                    self.dead_piece(self.selected) # selected piece dies
        else:
            return False
        
        if not positioning:
            self.change_turn()

        return True
    
    def change_turn(self):
        self.valid_moves = {} # reset the valid_moves dictionary
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * GRID_DIM + GRID_DIM // 2, row * GRID_DIM + GRID_DIM // 2), 15)
