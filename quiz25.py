
def drawboard(board):
    board1=int(board)+int((board-1))
    for i in range(5):
        if i%2==0:
            print("|  " * int(board1-1))
        else:
            print("-- "*4)
print(drawboard(3))


