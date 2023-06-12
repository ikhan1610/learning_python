# Write your code here :-)
def isValidChessBoard(userChessBoard):
    countBlackQueen = 0
    countBlackKing = 0
    countWhiteQueen = 0
    countWhiteKing = 0
    countBlackPawn = 0
    countWhitePawn = 0
    countPieces = {}
    validSpaces = ['1a','1b','1c','1d','1e','1f','1g','1h',
               '2a','2b','2c','2d','2e','2f','2g','2h',
               '3a','3b','3c','3d','3e','3f','3g','3h',
               '4a','4b','4c','4d','4e','4f','4g','4h',
               '5a','5b','5c','5d','5e','5f','5g','5h',
               '6a','6b','6c','6d','6e','6f','6g','6h',
               '7a','7b','7c','7d','7e','7f','7g','7h',
               '8a','8b','8c','8d','8e','8f','8g','8h']

    validPieces = ['wpawn','wknight','wbishop','wrook','wqueen','wking',
               'bpawn','bknight','bbishop','brook','bqueen','bking']

    #Check if the number of pawns are 8 or less
    for k,v in userChessBoard.items():
        if userChessBoard[k] == 'bpawn':
            countBlackPawn += 1
        elif userChessBoard[k] == 'wpawn':
            countWhitePawn += 1
    if countBlackPawn > 8 or countWhitePawn > 8:
        return False


    #Check if Black & White, Queen & King are less than 2
    for k,v in userChessBoard.items():
        if userChessBoard[k] == 'bqueen':
            countBlackQueen += 1
        elif userChessBoard[k] == 'bking':
            countBlackKing += 1
        elif userChessBoard[k] == 'wqueen':
            countWhiteQueen += 1
        elif userChessBoard[k] == 'wking':
            countWhiteKing += 1
    if countBlackQueen > 1 or countBlackKing > 1 or countWhiteQueen > 1 or countWhiteKing > 1:
        return False

    #Check if there are only 16 pieces or less
    for k,v in userChessBoard.items():
        if userChessBoard[k] in validPieces:
            countPieces.setdefault(userChessBoard[k],0)
            countPieces[k] += 1


    for k,v in userChessBoard.items():
        if k in validSpaces and userChessBoard[k] in validPieces:
            flag = 1
        else:
            flag = 0
            break

    if flag == 1:
        return True
    else:
        return False


print(isValidChessBoard({'1a': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
print(isValidChessBoard({'1h': 'wking', '6c': 'wking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
