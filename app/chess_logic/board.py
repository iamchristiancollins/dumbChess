class chessBoard():
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.board[0] = [5, 3, 4, 9, 10, 4, 3, 5]
        self.board[1] = [1, 1, 1, 1, 1, 1, 1, 1]
        self.board[6] = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.board[7] = [-5, -3, -4, -9, -10, -4, -3, -5]
        self.turn = 1
        self.move = 0
        self.moveList = []
        self.moveList.append(self.board)
        
    def get_board(self):
        return self.board
    
    def get_turn(self):
        return self.turn
    
    def get_move(self):
        return self.move
    
    def get_moveList(self):
        return self.moveList
    
    def set_board(self, board):
        self.board = board
    
    def set_turn(self, turn):
        self.turn = turn
        
    def set_move(self, move):
        self.move = move
        
    def set_moveList(self, moveList):
        self.moveList = moveList
        
    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = 0
        self.board[end[0]][end[1]] = piece
        self.turn = -self.turn
        self.move += 1
        self.moveList.append(self.board)
        return self.board
    
    def undo_move(self):
        self.board = self.moveList[-1]
        self.moveList.pop()
        self.turn = -self.turn
        self.move -= 1
        return self.board
    
    def is_valid_move(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece == 0:
            return False
        if piece > 0 and self.turn == -1:
            return False
        if piece < 0 and self.turn == 1:
            return False
        if piece == 1:
            if start[0] == 1:
                if start[1] == end[1] and (end[0] - start[0] == 1 or (end[0] - start[0] == 2 and self.board[start[0] + 1][start[1]] == 0)):
                    return True
                if abs(end[1] - start[1]) == 1 and end[0] - start[0] == 1 and self.board[end[0]][end[1]] < 0:
                    return True
            if start[0] != 1:
                if start[1] == end[1] and end[0] - start[0] == 1:
                    return True
                if abs(end[1] - start[1]) == 1 and end[0] - start[0] == 1 and self.board[end[0]][end[1]] < 0:
                    return True
        if piece == -1:
            if start[0] == 6:
                if start[1] == end[1] and (start[0] - end[0] == 1 or (start[0] - end[0] == 2 and self.board[start[0] - 1][start[1]] == 0)):
                    return True
                if abs(end[1] - start[1]) == 1 and start[0] - end[0] == 1 and self.board[end[0]][end[1]] > 0:
                    return True
            if start[0] != 6:
                if start[1] == end[1] and start[0] - end[0] == 1:
                    return True
                if abs(end[1] - start[1]) == 1 and start[0] - end[0] == 1 and self.board[end[0]][end[1]] > 0:
                    return True
        if piece == 5 or piece == -5:
            if abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
                return True
            if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
                return True
        if piece == 3 or piece == -3:
            if start[0] == end[0] or start[1] == end[1]:
                return True
        if piece == 4 or piece == -4:
            if abs(start[0] - end[0]) == abs(start[1] - end[1]):
                return True
        if piece == 9 or piece == -9:
            if abs(start[0] - end[0]) == abs(start[1] - end[1]) or start[0] == end[0] or start[1] == end[1]:
                return True
        if piece == 10 or piece == -10:
            if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
                return True
        return False
    
    def is_in_check(self, color):
        king = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 10 and color == "white":
                    king = (i, j)
                if self.board[i][j] == -10 and color == "black":
                    king = (i, j)
        for i in range(8):
            for j in range(8):
                if self.board[i][j] > 0 and color == "black":
                    if self.is_valid_move((i, j), king):
                        return True
                if self.board[i][j] < 0 and color == "white":
                    if self.is_valid_move((i, j), king):
                        return True
        return False
    
    def is_in_checkmate(self, color):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] > 0 and color == "white":
                    for k in range(8):
                        for l in range(8):
                            if self.is_valid_move((i, j), (k, l)):
                                if not self.is_in_check(color):
                                    return False
                if self.board[i][j] < 0 and color == "black":
                    for k in range(8):
                        for l in range(8):
                            if self.is_valid_move((i, j), (k, l)):
                                if not self.is_in_check(color):
                                    return False
        return True
    
    def is_in_stalemate(self, color):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] > 0 and color == "white":
                    for k in range(8):
                        for l in range(8):
                            if self.is_valid_move((i, j), (k, l)):
                                if not self.is_in_check(color):
                                    return False
                if self.board[i][j] < 0 and color == "black":
                    for k in range(8):
                        for l in range(8):
                            if self.is_valid_move((i, j), (k, l)):
                                if not self.is_in_check(color):
                                    return False
        return True
    
    def is_in_draw(self, color):
        if self.is_in_stalemate(color):
            return True
        if self.move == 50:
            return True
        return False
    
    def is_valid_promotion(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece == 1 and end[0] == 7:
            return True
        if piece == -1 and end[0] == 0:
            return True
        return False
    
    def promote_pawn(self, start, end, piece):
        self.board[start[0]][start[1]] = 0
        self.board[end[0]][end[1]] = piece
        self.turn = -self.turn
        self.move += 1
        self.moveList.append(self.board)
        return self.board
    
    def is_valid_castling(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece == 5 and start[0] == 0 and start[1] == 4 and end[0] == 0 and end[1] == 6:
            if self.board[0][5] == 0 and self.board[0][6] == 0:
                if self.board[0][7] == 3:
                    return True
        if piece == 5 and start[0] == 0 and start[1] == 4 and end[0] == 0 and end[1] == 2:
            if self.board[0][3] == 0 and self.board[0][2] == 0 and self.board[0][1] == 0:
                if self.board[0][0] == 3:
                    return True
        if piece == -5 and start[0] == 7 and start[1] == 4 and end[0] == 7 and end[1] == 6:
            if self.board[7][5] == 0 and self.board[7][6] == 0:
                if self.board[7][7] == -3:
                    return True
        if piece == -5 and start[0] == 7 and start[1] == 4 and end[0] == 7 and end[1] == 2:
            if self.board[7][3] == 0 and self.board[7][2] == 0 and self.board[7][1] == 0:
                if self.board[7][0] == -3:
                    return True
        return False
    
    def castle(self, start, end):
        piece = self.board[start[0]][start[1]]
        if start[0] == 0 and start[1] == 4 and end[0] == 0 and end[1] == 6:
            self.board[0][4] = 0
            self.board[0][5] = 5
            self.board[0][6] = 3
            self.board[0][7] = 0
        if start[0] == 0 and start[1] == 4 and end[0] == 0 and end[1] == 2:
            self.board[0][4] = 0
            self.board[0][3] = 5
            self.board[0][2] = 3
            self.board[0][0] = 0
        if start[0] == 7 and start[1] == 4 and end[0] == 7 and end[1] == 6:
            self.board[7][4] = 0
            self.board[7][5] = -5
            self.board[7][6] = -3
            self.board[7][7] = 0
        if start[0] == 7 and start[1] == 4 and end[0] == 7 and end[1] == 2:
            self.board[7][4] = 0
            self.board[7][3] = -5
            self.board[7][2] = -3
            self.board[7][0] = 0
        self.turn = -self.turn
        self.move += 1
        self.moveList.append(self.board)
        return self.board
    
    def is_valid_en_passant(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece == 1 and start[0] == 4 and abs(start[1] - end[1]) == 1 and end[0] == 5 and self.board[end[0]][end[1]] == 0:
            if self.board[5][end[1]] == -1:
                return True
        if piece == -1 and start[0] == 3 and abs(start[1] - end[1]) == 1 and end[0] == 2 and self.board[end[0]][end[1]] == 0:
            if self.board[2][end[1]] == 1:
                return True
        return False
    
    def en_passant(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece == 1 and start[0] == 4 and abs(start[1] - end[1]) == 1 and end[0] == 5 and self.board[end[0]][end[1]] == 0:
            self.board[start[0]][end[1]] = 0
            self.board[start[0]][start[1]] = 0
            self.board[end[0]][end[1]] = 1
        if piece == -1 and start[0] == 3 and abs(start[1] - end[1]) == 1 and end[0] == 2 and self.board[end[0]][end[1]] == 0:
            self.board[start[0]][end[1]] = 0
            self.board[start[0]][start[1]] = 0
            self.board[end[0]][end[1]] = -1
        self.turn = -self.turn
        self.move += 1
        self.moveList.append(self.board)
        return self.board
    
    
    def get_all_piece_moves(self):
        all_moves = {}
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None:
                    moves = piece.get_moves(self)
                    all_moves[(piece.name, row, col)] = moves  # Include piece name
        return all_moves