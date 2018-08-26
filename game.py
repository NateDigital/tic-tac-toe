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
for row in range(0, len(board)):
    for place in range(0, len(board)):
        keyBindings[str(bindingNo)] = [ row, place ]
        bindingNo += 1

def printBoard(boardData: board):
    print('\n +---+---+---+')
    for row in boardData:
        print(' | ', end='')
        for place in row:
            if place == 'X':
                colouredPlace = bcolors.OKBLUE + place + bcolors.ENDC
            elif place == 'O':
                colouredPlace = bcolors.OKGREEN + place + bcolors.ENDC
            else:
                colouredPlace = place
            print(colouredPlace, end=' | ')
        print('\n +---+---+---+')

def beginTurn(player: Player):
    global playersTurn
    global winner
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
    winner = getWinner(player)
    playersTurn = 1 - playersTurn

def getWinner(player: Player):
    diag1, diag2 = '', ''
    for x in range(0, len(board)):    
        diag1 += board[x][x]
        diag2 += board[x][(len(board)-1) - x]

        rows, cols = '', ''
        for y in range(0, len(board)):  
            rows += board[x][y]
            cols += board[y][x]

        if player.piece * len(board) in { rows, cols, diag1, diag2 }:
            return player.name

    for row in board:
        for place in row:
            if place == ' ':
                return None
    return 'Nobody'

while winner == None:
    beginTurn(players[playersTurn])

printBoard(board)
print(bcolors.HEADER + winner + ' is the winner!' + bcolors.ENDC)
