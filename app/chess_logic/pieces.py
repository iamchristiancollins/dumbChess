class ChessPiece:
    def __init__(self, color, piece_type, position):
        self.color = color
        self.piece_type = piece_type
        self.position = position
        self.custom_moves = []  # Add a custom_moves attribute

    def __str__(self):
        return f"{self.color} {self.piece_type} at {self.position}"

    def __repr__(self):
        return f"{self.color} {self.piece_type} at {self.position}"

    def move(self, new_position):
        self.position = new_position
    
    def set_custom_moves(self, moves):
        self.custom_moves = moves
        
    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def get_piece_type(self):
        return self.piece_type

    def get_moves(self, board):
        pass

    def is_valid_move(self, board, new_position):
        pass

    def is_valid_capture(self, board, new_position):
        pass
    
class Pawn(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, "Pawn", position)
        self.first_move = True
        
    def set_custom_moves(self, moves):
        self.custom_moves = moves
        
    def get_moves(self, board):
        if self.custom_moves:
            return self.custom_moves
        moves = []
        if self.color == "white":
            if self.first_move:
                moves.append((self.position[0], self.position[1] + 2))
            moves.append((self.position[0], self.position[1] + 1))
        else:
            if self.first_move:
                moves.append((self.position[0], self.position[1] - 2))
            moves.append((self.position[0], self.position[1] - 1))
        return moves
    
    def is_valid_move(self, board, new_position):
        moves = self.get_moves(board)
        if new_position in moves:
            return True
        return False
    
    def is_valid_capture(self, board, new_position):
        if self.color == "white":
            if (new_position[0] == self.position[0] + 1 or new_position[0] == self.position[0] - 1) and new_position[1] == self.position[1] + 1:
                return True
        else:
            if (new_position[0] == self.position[0] + 1 or new_position[0] == self.position[0] - 1) and new_position[1] == self.position[1] - 1:
                return True
        return False
    
    def move(self, new_position):
        self.position = new_position
        self.first_move = False
        
class Rook(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, "Rook", position)
        
    def get_moves(self, board):
        if self.custom_moves:
            return self.custom_moves
        moves = []
        for i in range(1, 8):
            moves.append((self.position[0] + i, self.position[1]))
            moves.append((self.position[0] - i, self.position[1]))
            moves.append((self.position[0], self.position[1] + i))
            moves.append((self.position[0], self.position[1] - i))
        return moves
    
    def is_valid_move(self, board, new_position):
        moves = self.get_moves(board)
        if new_position in moves:
            return True
        return False
    
    def is_valid_capture(self, board, new_position):
        return self.is_valid_move(board, new_position)
    
class Knight(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, "Knight", position)
        
    def get_moves(self, board):
        if self.custom_moves:
            return self.custom_moves
        moves = []
        moves.append((self.position[0] + 2, self.position[1] + 1))
        moves.append((self.position[0] + 2, self.position[1] - 1))
        moves.append((self.position[0] - 2, self.position[1] + 1))
        moves.append((self.position[0] - 2, self.position[1] - 1))
        moves.append((self.position[0] + 1, self.position[1] + 2))
        moves.append((self.position[0] + 1, self.position[1] - 2))
        moves.append((self.position[0] - 1, self.position[1] + 2))
        moves.append((self.position[0] - 1, self.position[1] - 2))
        return moves
    
    def is_valid_move(self, board, new_position):
        moves = self.get_moves(board)
        if new_position in moves:
            return True
        return False
    
    def is_valid_capture(self, board, new_position):
        return self.is_valid_move(board, new_position)
    
class Bishop(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, "Bishop", position)
        
    def get_moves(self, board):
        if self.custom_moves:
            return self.custom_moves
        moves = []
        for i in range(1, 8):
            moves.append((self.position[0] + i, self.position[1] + i))
            moves.append((self.position[0] + i, self.position[1] - i))
            moves.append((self.position[0] - i, self.position[1] + i))
            moves.append((self.position[0] - i, self.position[1] - i))
        return moves
    
    def is_valid_move(self, board, new_position):
        moves = self.get_moves(board)
        if new_position in moves:
            return True
        return False
    
    def is_valid_capture(self, board, new_position):
        return self.is_valid_move(board, new_position)
    
class Queen(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, "Queen", position)
        
    def get_moves(self, board):
        if self.custom_moves:
            return self.custom_moves
        moves = []
        for i in range(1, 8):
            moves.append((self.position[0] + i, self.position[1]))
            moves.append((self.position[0] - i, self.position[1]))
            moves.append((self.position[0], self.position[1] + i))
            moves.append((self.position[0], self.position[1] - i))
            moves.append((self.position[0] + i, self.position[1] + i))
            moves.append((self.position[0] + i, self.position[1] - i))
            moves.append((self.position[0] - i, self.position[1] + i))
            moves.append((self.position[0] - i, self.position[1] - i))
        return moves
    
    def is_valid_move(self, board, new_position):
        moves = self.get_moves(board)
        if new_position in moves:
            return True
        return False
    
    def is_valid_capture(self, board, new_position):
        return self.is_valid_move(board, new_position)
    
class King(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, "King", position)
        
    def get_moves(self, board):
        if self.custom_moves:
            return self.custom_moves
        moves = []
        moves.append((self.position[0] + 1, self.position[1]))
        moves.append((self.position[0] - 1, self.position[1]))
        moves.append((self.position[0], self.position[1] + 1))
        moves.append((self.position[0], self.position[1] - 1))
        moves.append((self.position[0] + 1, self.position[1] + 1))
        moves.append((self.position[0] + 1, self.position[1] - 1))
        moves.append((self.position[0] - 1, self.position[1] + 1))
        moves.append((self.position[0] - 1, self.position[1] - 1))
        return moves
    
    def is_valid_move(self, board, new_position):
        moves = self.get_moves(board)
        if new_position in moves:
            return True
        return False
    
    def is_valid_capture(self, board, new_position):
        return self.is_valid_move(board, new_position)
    