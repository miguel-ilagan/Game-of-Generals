import pygame

# Board dimensions
WIDTH, HEIGHT = 540, 840
ROWS, COLS = 14, 9
GRID_DIM = WIDTH//COLS
PADDING = 1

# FPS
FPS = 60

# RGB Colour
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ALMOND = (234, 221, 202)
BLUE = (0, 0, 255)
GREY = (129, 133, 137)

# RESET BUTTON COORDINATES
finished_positioning_row = 2
finished_positioning_col = 8

# GRAVEYARD WHITE
GYWR1 = 3
GYWR2 = ROWS - 3

# GRAVEYARD BLACK
GYBR1 = ROWS - 3

# total number of pieces in the game
total_pieces = 42

# Assets
# Black pieces
FirstLieutBlack = pygame.transform.scale(pygame.image.load('assets/1stLieutBlack.png'), (45, 37.5))
SecondLieutBlack = pygame.transform.scale(pygame.image.load('assets/2ndLieutBlack.png'), (45, 37.5))
CaptainBlack = pygame.transform.scale(pygame.image.load('assets/CaptainBlack.png'), (45, 37.5))
Colonel3Black = pygame.transform.scale(pygame.image.load('assets/Colonel3Black.png'), (45, 37.5))
FlagBlack = pygame.transform.scale(pygame.image.load('assets/FlagBlack.png'), (45, 37.5))
General1Black = pygame.transform.scale(pygame.image.load('assets/General1Black.png'), (45, 37.5))
General2Black = pygame.transform.scale(pygame.image.load('assets/General2Black.png'), (45, 37.5))
General3Black = pygame.transform.scale(pygame.image.load('assets/General3Black.png'), (45, 37.5))
General4Black = pygame.transform.scale(pygame.image.load('assets/General4Black.png'), (45, 37.5))
General5Black = pygame.transform.scale(pygame.image.load('assets/General5Black.png'), (45, 37.5))
LtColBlack = pygame.transform.scale(pygame.image.load('assets/LtColBlack.png'), (45, 37.5))
MajorBlack = pygame.transform.scale(pygame.image.load('assets/MajorBlack.png'), (45, 37.5))
PrivateBlack = pygame.transform.scale(pygame.image.load('assets/PrivateBlack.png'), (45, 37.5))
SgtBlack = pygame.transform.scale(pygame.image.load('assets/SgtBlack.png'), (45, 37.5))
SpyBlack = pygame.transform.scale(pygame.image.load('assets/SpyBlack.png'), (45, 37.5))

# White pieces
FirstLieutWhite = pygame.transform.scale(pygame.image.load('assets/1stLieutWhite.png'), (45, 37.5))
SecondLieutWhite = pygame.transform.scale(pygame.image.load('assets/2ndLieutWhite.png'), (45, 37.5))
CaptainWhite = pygame.transform.scale(pygame.image.load('assets/CaptainWhite.png'), (45, 37.5))
Colonel3White = pygame.transform.scale(pygame.image.load('assets/Colonel3White.png'), (45, 37.5))
FlagWhite = pygame.transform.scale(pygame.image.load('assets/FlagWhite.png'), (45, 37.5))
General1White = pygame.transform.scale(pygame.image.load('assets/General1White.png'), (45, 37.5))
General2White = pygame.transform.scale(pygame.image.load('assets/General2White.png'), (45, 37.5))
General3White = pygame.transform.scale(pygame.image.load('assets/General3White.png'), (45, 37.5))
General4White = pygame.transform.scale(pygame.image.load('assets/General4White.png'), (45, 37.5))
General5White = pygame.transform.scale(pygame.image.load('assets/General5White.png'), (45, 37.5))
LtColWhite = pygame.transform.scale(pygame.image.load('assets/LtColWhite.png'), (45, 37.5))
MajorWhite = pygame.transform.scale(pygame.image.load('assets/MajorWhite.png'), (45, 37.5))
PrivateWhite = pygame.transform.scale(pygame.image.load('assets/PrivateWhite.png'), (45, 37.5))
SgtWhite = pygame.transform.scale(pygame.image.load('assets/SgtWhite.png'), (45, 37.5))
SpyWhite = pygame.transform.scale(pygame.image.load('assets/SpyWhite.png'), (45, 37.5))

done = pygame.transform.scale(pygame.image.load('assets/done.jpg'), (45, 37.5))