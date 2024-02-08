class ChessPiece:
    def __init__(self, color, piece_type, position):
        self.color = color
        self.piece_type = piece_type
        self.position = position

    def __str__(self):
        return f"{self.color} {self.piece_type} at {self.position}"

    def __repr__(self):
        return f"{self.color} {self.piece_type} at {self.position}"

    def move(self, new_position):
        self.position = new_position

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
        
    def get_moves(self, board):
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