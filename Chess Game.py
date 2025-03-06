def main(): # Launch the environment ##line 126 of the original code
    global selected_piece, dragging # Remember what piece is picked and if it's moved
    turn = 'w'  # White starts

    win = pygame.display.set_mode((WIDTH, HEIGHT)) # Creates the game window with the given size
    pygame.display.set_caption('Chess Game') # Sets the window title to 'Chess Game'
    images = load_images()  # Loads the chess piece images
    board = [row[:] for row in starting_position]  # Creates the starting position of the game

    running = True # Keeps the game running until the player quits
    while running:  # Loop that keeps the game running until the player quits.
        draw_board(win) # Draws the chessboard on the window
        draw_pieces(win, board, images)  # Draws the chess pieces on the board

        # Highlight legal moves of the selected piece
        if selected_piece: #Runs this code only if a piece is selected
            row, col = selected_piece # Extracts the row and column of the piece
            piece = board[row][col] # Use row and column to find what piece was selected.

            #Only highlight if it's the current player's turn
            if piece and piece[0] == turn: # Checks if a piece is selected and if the piece belongs to the player
                legal_moves = get_legal_moves(board, row, col, piece) # Finds all valid moves for the selected piece
                draw_legal_moves(win, legal_moves)  # Highlights the possible moves on the board

        for event in pygame.event.get(): # Detects player actions (clicks, key presses, closing the game)
            if event.type == pygame.QUIT: # Checks if the player closes the game window
                pygame.quit()  # Properly closes Pygame
                sys.exit() # Exits the whole program.

            elif event.type == pygame.MOUSEBUTTONDOWN: # Checks if the player clicks the mouse
                x, y = pygame.mouse.get_pos() # Gets the mouse position (x, y) on the screen
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE #Converts the mouse position into a chessboard square

                #Ensure player can only select their own pieces
                if board[row][col] and board[row][col][0] == turn: # Checks if there's a piece in that square and if it's the player's turn
                    selected_piece = (row, col) # Remembers what piece is being selected
                    dragging = True #Marks that the player is currently moving a piece