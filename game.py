from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Player:
  def __init__(self, name, piece):
    self.name = name
    self.piece = piece

players = [
    Player(input("Player 1's name (X) ? "), 'X'),
    Player(input("Player 2's name (O) ? "), 'O')
]
playersTurn = randint(0, 1)
winner = None

board: list = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]

keyBindings = {}
bindingNo = 1
for line in range(0, len(board)):
    for row in range(0, len(board)):
        keyBindings[str(bindingNo)] = [ line, row ]
        bindingNo += 1

def printBoard(boardData: board):
    print('\n +---+---+---+')
    for line in boardData:
        print(' | ', end='')
        for row in line:
            if row == 'X':
                colouredRow = bcolors.OKBLUE + row + bcolors.ENDC
            elif row == 'O':
                colouredRow = bcolors.OKGREEN + row + bcolors.ENDC
            else:
                colouredRow = row
            print(colouredRow, end=' | ')
        print('\n +---+---+---+')

def beginTurn(player: Player):
    global playersTurn
    printBoard(board)
    move = input('\n' + player.name + ", It\'s your turn (1-9): ")
    try:
        key = keyBindings[move]
    except KeyError:
        print(bcolors.WARNING + 'Invalid Key, please use numbers from 1 - 9 !' + bcolors.ENDC)
        return
    if (board[key[0]][key[1]] != ' '):
        print(bcolors.WARNING + 'That space on the board is occupied! Choose another!' + bcolors.ENDC)
        return
    board[key[0]][key[1]] = player.piece
    checkForVictory(player)
    playersTurn = 1 - playersTurn

def checkForVictory(player: Player):
    global winner
    winningPattern = player.piece * len(board)
    for x in range(0, len(board)):    
        if (board[x][0] + board[x][1] + board[x][2] == winningPattern or # rows
            board[0][x] + board[1][x] + board[2][x] == winningPattern or # cols 
            board[0][0] + board[1][1] + board[2][2] == winningPattern or # diag
            board[0][2] + board[1][1] + board[2][0] == winningPattern):  # diag
                winner = player.name
    # tie
    for line in board:
        for row in line:
            if row == ' ':
                return
    winner = 'Nobody'

while winner == None:
    beginTurn(players[playersTurn])

printBoard(board)
print(bcolors.HEADER + winner + ' is the winner!' + bcolors.ENDC)
