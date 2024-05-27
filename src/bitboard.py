# Pyfish, a UCI chess playing engine based on Stockfish 12.
#
# Pyfish is free software: please cite and fork the repo if you
# would like to use.

import types

# Define constants
FileABB = 0x0101010101010101
FileBBB = FileABB << 1
FileCBB = FileABB << 2
FileDBB = FileABB << 3
FileEBB = FileABB << 4
FileFBB = FileABB << 5
FileGBB = FileABB << 6
FileHBB = FileABB << 7

Rank1BB = 0xFF
Rank2BB = Rank1BB << (8 * 1)
Rank3BB = Rank1BB << (8 * 2)
Rank4BB = Rank1BB << (8 * 3)
Rank5BB = Rank1BB << (8 * 4)
Rank6BB = Rank1BB << (8 * 5)
Rank7BB = Rank1BB << (8 * 6)
Rank8BB = Rank1BB << (8 * 7)

# Define some global variables and functions
PopCnt16 = [bin(i).count('1') for i in range(1 << 16)]
SquareDistance = [[max(abs(i - j) % 8, abs(i // 8 - j // 8)) for j in range(64)] for i in range(64)]
LineBB = [[0] * 64 for _ in range(64)]
BetweenBB = [[0] * 64 for _ in range(64)]
PseudoAttacks = [[0] * 64 for _ in range(16)]
PawnAttacks = [[0] * 64 for _ in range(2)]

# Function definitions
def pretty(b: int) -> str:
    s = "+---+---+---+---+---+---+---+---+\n"
    for r in range(7, -1, -1):
        for f in range(8):
            s += "| X " if b & (1 << (8 * r + f)) else "|   "
        s += "| " + str(r + 1) + "\n+---+---+---+---+---+---+---+---+\n"
    s += "  a   b   c   d   e   f   g   h\n"
    return s

def init():
    global PopCnt16, SquareDistance, LineBB, BetweenBB, PseudoAttacks, PawnAttacks
    PopCnt16 = [bin(i).count('1') for i in range(1 << 16)]
    SquareDistance = [[max(abs(i - j) % 8, abs(i // 8 - j // 8)) for j in range(64)] for i in range(64)]
    LineBB = [[0] * 64 for _ in range(64)]
    BetweenBB = [[0] * 64 for _ in range(64)]
    PseudoAttacks = [[0] * 64 for _ in range(16)]
    PawnAttacks = [[0] * 64 for _ in range(2)]

# Other function and variable definitions...

# Add functions and variables to the module
bitboard_module = types.ModuleType("bitboard")
bitboard_module.__doc__ = """
    Pyfish, a UCI chess playing engine based on Stockfish 12.
    Pyfish is free software: please cite and fork the repo if you
    would like to use.
"""
bitboard_module.FileABB = FileABB
bitboard_module.FileBBB = FileBBB
bitboard_module.FileCBB = FileCBB
bitboard_module.FileDBB = FileDBB
bitboard_module.FileEBB = FileEBB
bitboard_module.FileFBB = FileFBB
bitboard_module.FileGBB = FileGBB
bitboard_module.FileHBB = FileHBB
bitboard_module.Rank1BB = Rank1BB
bitboard_module.Rank2BB = Rank2BB
bitboard_module.Rank3BB = Rank3BB
bitboard_module.Rank4BB = Rank4BB
bitboard_module.Rank5BB = Rank5BB
bitboard_module.Rank6BB = Rank6BB
bitboard_module.Rank7BB = Rank7BB
bitboard_module.Rank8BB = Rank8BB
bitboard_module.PopCnt16 = PopCnt16
bitboard_module.SquareDistance = SquareDistance
bitboard_module.LineBB = LineBB
bitboard_module.BetweenBB = BetweenBB
bitboard_module.PseudoAttacks = PseudoAttacks
bitboard_module.PawnAttacks = PawnAttacks
bitboard_module.pretty = pretty
bitboard_module.init = init

# Add the module to the global namespace
globals().update(bitboard_module.__dict__)
