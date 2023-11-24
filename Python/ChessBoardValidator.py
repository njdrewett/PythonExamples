# Chess board validator
#We can use the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
#Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.
#A valid board will have exactly one black king and exactly one white
# king. Each player can only have at most 16 pieces, at most 8 pawns, and
# all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t
# be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or
# 'king'. This function should detect when a bug has resulted in an improper
#chess board.

pieceColours = ['W','B']
pieceTypes = ['king','queen','bishop','rook','knight','pawn']

pieces = []

maxPieces = 16
maxPawns = 8

boardWidth = 8
boardHeight = 8

boardCoords = []

boardHeightLetter = ['A','B','C','D','E','F','G','H']

board =  {'1H': 'Bking', '6C': 'Wqueen', '2G': 'Bbishop', '5H': 'Bqueen', '3E': 'Wking'}

for pieceColour in pieceColours:
    for pieceType in pieceTypes:
        pieces.append(pieceColour+pieceType)
print(pieces)

for pieceWidth in range(1, boardWidth+1):
    for pieceHeight in range(0, boardHeight):
        boardCoords.append(str(pieceWidth)+boardHeightLetter[pieceHeight])
print(boardCoords)

def validatePresent(board,piece, ofEach):
    print('validatePresent'+piece)
    for pieceColour in pieceColours:
        occurances = list(board.values()).count(str(pieceColour+piece))
        print(piece + ': occurances : ' + str(occurances))
        if occurances <= ofEach:
            print('All present')
        else :
            print('Not Present')
            return False
    return True

def validateCells(board):
    for cell in board.keys():
        if( cell in boardCoords):
            print('Cell is present')
        else:
            print('Cell not present')
            return False
    return True


def validateChessBoard(board):
    print('Validating board')
    kingsOfEach = validatePresent(board,'king',1)
    queensOfEach = validatePresent(board,'queen',1)
    bishopOfEach = validatePresent(board,'bishop',2)
    knightOfEach = validatePresent(board,'knight',2)
    rookOfEach = validatePresent(board,'rook',2)
    pawnOfEach = validatePresent(board,'pawn',8)

    validCells = validateCells(board)

    return kingsOfEach & queensOfEach & bishopOfEach & knightOfEach & rookOfEach & pawnOfEach

valid = validateChessBoard(board)
print('Valid: ' + str(valid))



