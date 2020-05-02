# CH5 AutomateTheBorinStuff: ChessBoardValidation
# Version 1: I used functions wo check wvery condition

"""
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen',
'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
Write a function named isValidChessBoard() that takes a dictionary argument
and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces, at most 8 pawns, and all pieces
must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space
'9z'. The piece names begin with either a 'w' or 'b' to represent white or
black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
This function should detect when a bug has resulted in an improper chess board.
"""
import re


def kingsPresence(board):
    if list(board.values()).count('bking') == 1 and \
        list(board.values()).count('wking') == 1:
        return True
    else:
        return False

def validNumPieces(board):
    numPieces = 0
    for space in board:
        if board[space].startswith('b'):
            numPieces += 1
    if numPieces > 8:
        return False

    numPieces = 0
    for space in board:
        if board[space].startswith('w'):
            numPieces += 1
    if numPieces > 8:
        return False
    
    return True


def validPawns(board):
    if list(board.values()).count("bpawn") > 8:
        return False
    if list(board.values()).count("wpawn") > 8:
        return False

    return True

def validNamePieces(board):
    allowedNames = ['bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking',
                    'wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking']
    for piece in list(board.values()):
        if not piece in allowedNames: return False
    
    return True

def validPosPieces(board):
    allowedPos = re.compile(r"[1-8][a-h]")
    for pos in board:
        if not allowedPos.search(pos):
            return False
    return True


def isValidChessBoard(board):
    if not kingsPresence(board):
        print("Too many kings or absent")
        return False

    if not validPawns(board):
        print("Too many pawns on one or both sides")
        return False
    
    if not validNumPieces(board):
        print("Too many pieces on one or both sides")
        return False
    
    if not validNamePieces(board):
        print("There are invalid names of pieces")
        return False
    
    if not validPosPieces(board):
        print("Pieces in invalid spaces")
        return False
        
    return True

#________________________TEST_____________________________

chessBoard0 = {'1h': 'bking',
               '6c': 'wqueen',
               '2g': 'bbishop',
               '5h': 'bqueen',
               '3e': 'wking'}

chessBoard1 = { #False
               '6c': 'wqueen', 
               '2g': 'bbishop',
               '5h': 'bqueen',
               '3e': 'wking'}

chessBoard2 = {'1c': 'bpawn',
               '2c': 'bpawn',
               '3c': 'bpawn',
               '4c': 'bpawn',
               '5c': 'bpawn',
               '6c': 'bpawn',
               '7c': 'bpawn',
               '8c': 'bpawn',
               '1d': 'bpawn', #False
               '8a': 'bking',
               '2g': 'bbishop',
               '5h': 'bqueen',
               '3e': 'wking'}

chessBoard3 = {'1h': 'bking',
               '6z': 'wqueen', #False
               '2g': 'bbishop',
               '5h': 'bqueen',
               '3e': 'wking'}

chessBoard4 = {'1h': 'bking',
               '6c': 'queen', #False
               '2g': 'bbishop',
               '5h': 'bqueen',
               '3e': 'wking'}

print("chessBoard0 valid:", isValidChessBoard(chessBoard0), '\n') #True
print("chessBoard1 valid:", isValidChessBoard(chessBoard1), '\n') #False
print("chessBoard1 valid:", isValidChessBoard(chessBoard2), '\n') #False
print("chessBoard1 valid:", isValidChessBoard(chessBoard3), '\n') #False
print("chessBoard1 valid:", isValidChessBoard(chessBoard4), '\n') #False
