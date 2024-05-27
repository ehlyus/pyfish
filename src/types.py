# Define types used in the chess engine

# Define constants for square indices
A1, B1, C1, D1, E1, F1, G1, H1 = range(8)
A2, B2, C2, D2, E2, F2, G2, H2 = range(8, 16)
A3, B3, C3, D3, E3, F3, G3, H3 = range(16, 24)
A4, B4, C4, D4, E4, F4, G4, H4 = range(24, 32)
A5, B5, C5, D5, E5, F5, G5, H5 = range(32, 40)
A6, B6, C6, D6, E6, F6, G6, H6 = range(40, 48)
A7, B7, C7, D7, E7, F7, G7, H7 = range(48, 56)
A8, B8, C8, D8, E8, F8, G8, H8 = range(56, 64)

# Define constants for piece types
PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING = range(6)

# Define constants for colors
WHITE, BLACK = range(2)

# Define a square type
Square = int

# Define a bitboard type
Bitboard = int

# Define a rank type
Rank = int

# Define a file type
File = int

# Define a piece type
PieceType = int

# Define a color type
Color = int
