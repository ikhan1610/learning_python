import pprint
'''Steps

-> Define the set of all chess pieces
-> Define the valid count range of pieces by type
-> Count the pieces on the board
-> Check pieces counts in a valid range
-> Check that positions are valid
-> Check that pieces names are valid'''

def isValidChessBoard(board):
    #Validate counts and positions of pieces on board

    #Define pieces and colors
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen','king']
    colors = ['b','w']

    #Set of all chess pieces
    all_pieces = set(color+piece for color in colors for piece in pieces)
    #print(all_pieces)
    #Define valid range for count of chess pieces by type (low,high) tuple
    validCounts = {'king':(1,1),
                    'queen':(0,1),
                    'knight':(0,2),
                    'bishop':(0,2),
                    'rook':(0,2),
                    'pawn':(0,8)
                    }

    #Get count of pieces on the board
    countPieces = {}
    for v in board.values():
        if v in all_pieces:
            countPieces.setdefault(v,0)
            countPieces[v] += 1

    # Check if there are a valid number of pieces
    for piece in board.values():
        count = countPieces.get(piece,0)
        lo,hi = validCounts[piece[1:]]
        if not lo <= count <= hi:
            if lo != hi:
                print(f"The count should be between {lo} and {hi}, but the count is {count}")
            else:
                print(f"The count should be {lo} of {piece}, but the count is {count}")
            return False

    #Check if locations are valid
    for location in board.keys():
        row = int(location[:1])
        column = location[1:]
        if not ((1 <= row <= 8) and ('a' <= column <= 'h')):
            print(f"Invalid to have {board[location]} at the position {location}")
            return False

    #Check if piece names are valid
    for location,pieceName in board.items():
        if pieceName:
            if not pieceName in all_pieces:
                print(f"{pieceName} in not a valid piece at the postion {location}")

    return True



print(isValidChessBoard({'1b': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
print(isValidChessBoard({'1z': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
print(isValidChessBoard({'1b': 'wking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
print(isValidChessBoard({'1b': 'wqueen', '6c': 'wqueen', '2g': 'bbishop', '5h': 'wqueen', '3e': 'wqueen'}))
