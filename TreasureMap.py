import random
def create_board(width, height):
    board = []
    numberOfUndiscoveredTreasures = 0

    for row in range(height):
        board_row = []
        for col in range(width):
            if random.random() >= 0.7:
                board_row.append('T')
                numberOfUndiscoveredTreasures += 1
            else:
                board_row.append('O')
        board.append(board_row)

    return board, numberOfUndiscoveredTreasures

def show_board(board):
    for row in board:
        print(" ".join(row))

def treasure_hunt():
    height = int(input("Enter dungeon width: "))
    width = int(input("Enter dungeon height: "))

    board, numberOfUndiscoveredTreasures = create_board(width, height)
    print("There are", numberOfUndiscoveredTreasures, "treasures hidden on the board.")

    while numberOfUndiscoveredTreasures > 0:
        row = int(input("Enter row to check (0-" + str(height - 1) + "): "))
        col = int(input("Enter column to check (0-" + str(width - 1) + "): "))

        if row < 0 or row >= height or col < 0 or col >= width:
            print("Invalid coordinates, try again.")
            continue

        if board[row][col] == 'T':
            print("You found a treasure at (" + str(row) + ", " + str(col) + ")!")
            board[row][col] = 'X'
            numberOfUndiscoveredTreasures -= 1
        elif board[row][col] == 'O':
            print("No treasure found at (" + str(row) + ", " + str(col) + ")")

        show_board(board)