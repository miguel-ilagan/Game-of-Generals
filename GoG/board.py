import pygame
from .constants import *
from .piece import *

class Board:
    def __init__(self):
        self.board = [] # Board is a 2D matrix
        self.selected_piece = None
        self.num_white_pieces = self.num_black_pieces = 21 # Each player starts with 21 pieces.
        self.initialise_board_num = total_pieces # total number of pieces on the board
        self.num_white_flag = self.num_black_flag = 1 # Each player has a flag
        self.create_board()
    
    # Function to draw the board with the squares
    def draw_board(self, win):
        win.fill(BLACK) # Fill the entire window with BLACK
        # Draw the graveyard for white
        for row in range(GYWR1):
            for col in range(COLS):
                # Draw rectangles on the window:
                pygame.draw.rect(win, GREY, (col * GRID_DIM + PADDING, row * GRID_DIM + PADDING, GRID_DIM - 2 * PADDING, GRID_DIM - 2 * PADDING))
        
        for row in range(GYWR1, GYWR2):
            for col in range(COLS):
                # Draw rectangles on the window:
                pygame.draw.rect(win, ALMOND, (col * GRID_DIM + PADDING, row * GRID_DIM + PADDING, GRID_DIM - 2 * PADDING, GRID_DIM - 2 * PADDING))

        for row in range(GYBR1, ROWS):
            for col in range(COLS):
                # Draw rectangles on the window:
                pygame.draw.rect(win, GREY, (col * GRID_DIM + PADDING, row * GRID_DIM + PADDING, GRID_DIM - 2 * PADDING, GRID_DIM - 2 * PADDING))
    
    # Function that will create the internal representation of the board which will add the pieces to the list
    # At the start of the game, pieces will be in the graveyard where the players will select where to put their pieces
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                # White pieces are at the top of the board
                if row < 3:
                    for rank in num_pieces_white:
                        if num_pieces_white[rank] != 0:
                            self.board[row].append(Piece(row, col, WHITE, rank))
                            num_pieces_white[rank] -= 1
                            self.initialise_board_num -= 1
                            break
                    if self.initialise_board_num == self.num_white_pieces:
                        self.board[row].append(0)
        
                # Black pieces are at the bottom of the board
                elif row > GYBR1 - 1:
                    for rank in num_pieces_black:
                        if num_pieces_black[rank] != 0:
                            self.board[row].append(Piece(row, col, BLACK, rank))
                            num_pieces_black[rank] -= 1
                            self.initialise_board_num -= 1
                            break
                    if self.initialise_board_num == 0:
                        self.board[row].append(0)

                # 0 indicates that there is no piece at this location
                else:
                    self.board[row].append(0)
    
    # This function will draw all of the pieces and the board
    def draw(self, win, turn):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 and piece.colour == turn:
                    # Draw the piece on the board when it is your turn
                    piece.draw_piece(win, piece.rank)
                elif piece != 0 and piece.colour != turn:
                    pygame.draw.rect(win, BLACK, (col * GRID_DIM + PADDING, row * GRID_DIM + PADDING, GRID_DIM - 2 * PADDING, GRID_DIM - 2 * PADDING))
                
                # Draw the "DONE button" which is used during the positioning stage of the game
                if row == finished_positioning_row and col == finished_positioning_col:
                    x = GRID_DIM * col + GRID_DIM // 2
                    y = GRID_DIM * row + GRID_DIM // 2
                    win.blit(done, (x - done.get_width() // 2, y - done.get_height() // 2)) 

    # This function will move the piece
    # This function will swap the piece from where it is to the new position
    # note that row, col are the new positions that we want to move to
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    # This function will return the piece at a certain location of the board
    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece, positioning):
        moves = {} # {coord : opponent_piece}
        # moves is a dictionary which will store all the valid moves that a piece can make (key). The value is the opposing teams piece (if any)
        
        # This is the case where the user positions the pieces at the start of the game
        if positioning:
            if piece.colour == WHITE:
                for row in range(GYWR1, GYWR1 + 3):
                    for col in range(COLS):
                        if self.board[row][col] == 0:
                            moves[(row, col)] = None

            if piece.colour == BLACK:
                for row in range(GYWR2 - 3, GYWR2):
                    for col in range(COLS):
                        if self.board[row][col] == 0:
                            moves[(row, col)] = None
        
        # This is the case for the rest of the game
        else:
            # pieces can only move up, down, left, right
            up = (piece.row + 1, piece.col)
            down = (piece.row - 1, piece.col)
            left = (piece.row, piece.col - 1)
            right = (piece.row, piece.col + 1)

            valid_directions = [up, down, left, right]

            for direction in valid_directions:
                
                # You cannot go outside the board
                if direction[0] < GYWR1 or direction[0] >= GYBR1 or direction[1] < 0 or direction[1] >= COLS:
                    continue

                # If the square is empty then it is a valid move
                if self.board[direction[0]][direction[1]] == 0:
                    moves[direction] = None

                # If the square is not empty
                else:
                    check_piece = self.get_piece(direction[0], direction[1])

                    # If the piece is the opposite colour then it is a valid move
                    if piece.colour != check_piece.colour:
                        moves[direction] = check_piece
        
        return moves
    
