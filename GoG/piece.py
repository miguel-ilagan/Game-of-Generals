from .constants import *

num_pieces_white = {FlagWhite:1, PrivateWhite: 6, SgtWhite: 1, SecondLieutWhite: 1, FirstLieutWhite: 1, CaptainWhite: 1, 
                        MajorWhite: 1, LtColWhite: 1, Colonel3White: 1, General1White: 1, General2White: 1, General3White: 1, 
                        General4White: 1, General5White: 1, SpyWhite: 2}

num_pieces_black = {FlagBlack:1, PrivateBlack: 6, SgtBlack: 1, SecondLieutBlack: 1, FirstLieutBlack: 1, CaptainBlack: 1, 
                        MajorBlack: 1, LtColBlack: 1, Colonel3Black: 1, General1Black: 1, General2Black: 1, General3Black: 1, 
                        General4Black: 1, General5Black: 1, SpyBlack: 2}

class Piece:
    # Dictionary which contains the power levels of each rank
    def __init__(self, row, col, colour, rank):
        self.power_level_dict = {FlagWhite:1, PrivateWhite: 2, SgtWhite: 3, SecondLieutWhite: 4, FirstLieutWhite: 5, CaptainWhite: 6, 
                        MajorWhite: 7, LtColWhite: 8, Colonel3White: 9, General1White: 10, General2White: 11, General3White: 12, 
                        General4White: 13, General5White: 14, SpyWhite: 15,
                        FlagBlack:1, PrivateBlack: 2, SgtBlack: 3, SecondLieutBlack: 4, FirstLieutBlack: 5, CaptainBlack: 6, 
                        MajorBlack: 7, LtColBlack: 8, Colonel3Black: 9, General1Black: 10, General2Black: 11, General3Black: 12, 
                        General4Black: 13, General5Black: 14, SpyBlack: 15}
        self.row = row
        self.col = col
        self.colour = colour
        self.rank = rank
        self.power_level = self.power_level_dict[rank]

        # Initialise variables x and y
        self.x = 0
        self.y = 0

        # Calculate the position of the piece
        self.calc_pos()

    # Calculate the x and y position based on row and col of the piece
    # Note that the position of the piece is in the centre of the square.
    def calc_pos(self):
        self.x = GRID_DIM * self.col + GRID_DIM // 2
        self.y = GRID_DIM * self.row + GRID_DIM // 2

    # Function to draw the piece
    def draw_piece(self, win, rank):
        win.blit(rank, (self.x - rank.get_width() // 2, self.y - rank.get_height() // 2)) 
    
    # This will give the internal representation of the object which is useful for debugging
    def __repr__(self):
        return str(self.colour, self.rank)
    
    # This function will change the coordinates of the piece
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()