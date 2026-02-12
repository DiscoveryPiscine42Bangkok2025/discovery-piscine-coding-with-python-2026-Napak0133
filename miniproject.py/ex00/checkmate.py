#!/usr/bin/env python3

def checkmate(board):
    
    Board2D = setBoard(board)
    # print(setBoard(board))

    if len(Board2D) != len(Board2D[0]):
        print("Erorr")  # not square
        return
    
    king = findKing(Board2D)

    n = len(board)

    for i in range(n):
        for j in range(n):
            piece = board[i][j]

            if piece == "P" and Pawn():
                print("Success")
                return

            if piece == "B" and Bishop():
                print("Success")
                return

            if piece == "R" and Rook():
                print("Success")
                return

            if piece == "Q" and Queen():
                print("Success")
                return          

    print("Fail")
    
def setBoard(board):
    rowsList = []
    for row in board.split("\n"):
        cleanRow = row.strip()
        rowsList.append(cleanRow)
    # print(rowsList)

    Board2D = []
    for r in rowsList:
        Board2D.append(list(r))
    # print(Board2D)

    return Board2D


def findKing(board):
    king = None
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == "K":
                if king is not None: 
                    print("Error")
                    return
                else: 
                    king = (i, j)
    return king


def Pawn():



def Bishop():



def Rook():



def Queen():



