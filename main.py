import pygame
from GoG.constants import *
from GoG.game import *

# Set up pygame display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game of Generals') # this is just the name of the game that appears at the top of the bar

# Function to get the row and column of the current mouse position
def mouse_pos_row_col(mouse_pos):
    row = mouse_pos[1] // GRID_DIM
    col = mouse_pos[0] // GRID_DIM
    return row, col
    
# Main function that is used to run the game
def main():
    run = True
    clock = pygame.time.Clock() # Let game run at a constant rate.
    game = Game(WIN)
    positioning = True
    
    while positioning:
        clock.tick(FPS)
        

        if game.winner():
            break

        for event in pygame.event.get(): # check if any events have happened at the current time
            # The case where the user closes the application
            if event.type == pygame.QUIT:
                run = False
                positioning = False
            
            # The case where the user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() # This gets the mouse position
                row, col = mouse_pos_row_col(mouse_pos) # This gets the coordinates of the mouse position
                game.select(row,col, positioning)
                
                # If the done button is clicked and all pieces are on the board, then positioning is done
                if row == finished_positioning_row and col == finished_positioning_col and game.count_board() == total_pieces:
                    positioning = False

        game.update()
    
    game.change_turn()
    
    while run:
        clock.tick(FPS)
        

        if game.winner():
            break
        
        for event in pygame.event.get(): # check if any events have happened at the current time
            # The case where the user closes the application
            if event.type == pygame.QUIT:
                run = False
            
            # The case where the user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() # This gets the mouse position
                row, col = mouse_pos_row_col(mouse_pos) # This gets the coordinates of the mouse position
                game.select(row,col, positioning)

        game.update()
    
    # Quits the game
    pygame.quit()

main()