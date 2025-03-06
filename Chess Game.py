
def main():
    global selected_piece, dragging
    turn = 'w'  # White starts

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess Game')
    images = load_images()
    board = [row[:] for row in starting_position]  # Ensure board is a mutable copy

    running = True
    while running:
        draw_board(win)
        draw_pieces(win, board, images)

        # Highlight legal moves of the selected piece
        if selected_piece:
            row, col = selected_piece
            piece = board[row][col]

            #Only highlight if it's the current player's turn
            if piece and piece[0] == turn:
                legal_moves = get_legal_moves(board, row, col, piece)
                draw_legal_moves(win, legal_moves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

                #Ensure player can only select their own pieces
                if board[row][col] and board[row][col][0] == turn:
                    selected_piece = (row, col)
                    dragging = True
